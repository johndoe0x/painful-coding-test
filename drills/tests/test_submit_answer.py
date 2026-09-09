from __future__ import annotations

import base64
from contextlib import redirect_stdout, redirect_stderr
from copy import deepcopy
from hashlib import sha256
from io import StringIO
import json
from pathlib import Path
import shutil
import shlex
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import submit_answer as submit


ROOT = Path(__file__).resolve().parents[1]
EXERCISE = '''"""
PB0001 — 테스트 전용
Source checks:

예시 및 필수 테스트
-------------------
- solve(0) == 1
- solve(4) == 5
- solve(-1) == 0

완료 조건
---------
세 예시를 통과합니다.
"""

def solve(value):
    print("LOCAL_DEBUG", value)
    return value + 1

def self_test():
    assert solve(0) == 1
    assert solve(4) == 5
    assert solve(-1) == 0
'''


class FakeGitHub:
    """An in-memory ref/tree/contents endpoint, never a network transport."""
    def __init__(self):
        self.calls = []
        self.head = 'a' * 40
        self.base_tree = 'b' * 40
        self.files = {}
        self.pending = []
        self.can_push = True
        self.conflict = False
        self.repo = 'johndoe0x/painful-coding-test'

    def request(self, method, endpoint, payload=None, *, missing_ok=False):
        self.calls.append((method, endpoint, deepcopy(payload)))
        prefix = f'repos/{self.repo}'
        if endpoint == prefix:
            return {'permissions': {'push': self.can_push}, 'default_branch': 'master'}
        if endpoint == 'user':
            return {'login': 'learner', 'id': 7}
        if endpoint == prefix + '/git/ref/heads/master':
            return {'ref': 'refs/heads/master', 'object': {'sha': self.head, 'type': 'commit'}}
        if endpoint == prefix + '/git/commits/' + self.head:
            return {'tree': {'sha': self.base_tree}}
        if '/contents/' in endpoint:
            path = endpoint.split('/contents/', 1)[1].split('?', 1)[0]
            if path in self.files:
                return {'encoding': 'base64', 'content': base64.b64encode(self.files[path].encode()).decode()}
            rows = [{'name': name.rsplit('/', 1)[1], 'type': 'file', 'sha': submit.git_blob_hash(content)}
                    for name, content in self.files.items() if name.rsplit('/', 1)[0] == path]
            if rows:
                return rows
            if missing_ok:
                return None
            raise AssertionError('unexpected missing content')
        if method == 'POST' and endpoint == prefix + '/git/trees':
            assert payload['base_tree'] == self.base_tree
            self.pending = payload['tree']
            return {'sha': 'c' * 40}
        if method == 'POST' and endpoint == prefix + '/git/commits':
            assert payload['parents'] == [self.head]
            assert payload['tree'] == 'c' * 40
            assert payload['author']['email'] == '7+learner@users.noreply.github.com'
            return {'sha': 'd' * 40}
        if method == 'PATCH' and endpoint == prefix + '/git/refs/heads/master':
            assert payload['force'] is False
            if self.conflict:
                raise submit.SubmissionError('remote conflict')
            for row in self.pending:
                assert row['path'].startswith('answers/') and row['type'] == 'blob'
                self.files[row['path']] = row['content']
            self.head, self.base_tree = payload['sha'], 'c' * 40
            return {'object': {'sha': self.head}}
        raise AssertionError((method, endpoint))


class SubmissionTests(unittest.TestCase):
    def setUp(self):
        scratch = ROOT / '.tmp'
        scratch.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='submit-test-', dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('run_problem.py', 'bank_inventory.py'):
            shutil.copyfile(ROOT / name, self.root / name)
        bank = self.root / 'python_basic'
        (bank / 'catalog').mkdir(parents=True)
        (bank / '__init__.py').write_text('')
        shutil.copyfile(ROOT / 'python_basic/source_checks.py', bank / 'source_checks.py')
        self.source_path = bank / 'PB0001_demo.py'
        self.source_path.write_text(EXERCISE, encoding='utf-8')
        (bank / 'catalog/generated_manifest.json').write_text(json.dumps({
            'problems': {'PB0001': {'path': 'PB0001_demo.py'}}
        }))
        (self.root / 'proofs').mkdir()
        (self.root / 'proofs/PB0001.json').write_text('existing learner receipt')

    def prepare(self):
        output = StringIO()
        with redirect_stdout(output):
            answer = submit.prepare_answer(self.root, 'pb0001')
        self.assertIn('PASS PB0001', output.getvalue())
        self.assertIn('LOCAL_DEBUG', output.getvalue())
        return answer

    def test_fresh_verification_saves_exact_answer_and_summary_only(self):
        original = self.source_path.read_bytes()
        answer = self.prepare()
        self.assertEqual((answer.directory / 'solution.py').read_bytes(), original)
        self.assertEqual(self.source_path.read_bytes(), original)
        self.assertEqual(set(answer.summary), submit.SUMMARY_FIELDS)
        self.assertEqual(answer.summary['source_sha256'], sha256(original).hexdigest())
        self.assertNotIn('LOCAL_DEBUG', (answer.directory / 'result.json').read_text())
        self.assertNotIn(str(self.root), (answer.directory / 'result.json').read_text())
        self.assertEqual((self.root/'proofs/PB0001.json').read_text(), 'existing learner receipt')
        self.assertEqual(list((self.root/'.tmp').iterdir()), [])

    def test_failed_and_unfinished_code_are_not_saved(self):
        for body in ('return 0', 'raise NotImplementedError("TODO")'):
            with self.subTest(body=body):
                self.source_path.write_text(EXERCISE.replace('return value + 1', body))
                with redirect_stdout(StringIO()), self.assertRaises(submit.SubmissionError):
                    submit.prepare_answer(self.root, 'PB0001')
                self.assertFalse((self.root/'answers').exists())

    def test_runner_json_and_regular_output_are_both_supported(self):
        base = [sys.executable, '-B', str(self.root/'run_problem.py'), 'PB0001', '--strict', '--no-receipt']
        human = subprocess.run(base, cwd=self.root, capture_output=True, text=True)
        machine = subprocess.run(base+['--json'], cwd=self.root, capture_output=True, text=True)
        self.assertEqual((human.returncode, machine.returncode), (0, 0))
        self.assertTrue(human.stdout.startswith('PASS PB0001'))
        receipt = json.loads(machine.stdout)
        self.assertEqual(receipt['status'], 'PASS')
        self.assertTrue(receipt['execution_output'])

    def test_crlf_source_bytes_match_the_checked_and_saved_hash(self):
        self.source_path.write_bytes(EXERCISE.replace('\n', '\r\n').encode())
        answer = self.prepare()
        self.assertEqual(answer.source, self.source_path.read_bytes())
        self.assertEqual((answer.directory/'solution.py').read_bytes(), answer.source)

    def test_source_edit_during_validation_cannot_be_uploaded(self):
        real_run = subprocess.run
        def run_then_edit(*args, **kwargs):
            result = real_run(*args, **kwargs)
            self.source_path.write_text(EXERCISE+'\n# edit during check\n')
            return result
        with patch.object(submit.subprocess, 'run', side_effect=run_then_edit):
            with redirect_stdout(StringIO()), self.assertRaisesRegex(submit.SubmissionError, '변경'):
                submit.prepare_answer(self.root, 'PB0001')
        self.assertFalse((self.root/'answers').exists())

    def test_timeout_does_not_save_or_use_an_old_receipt(self):
        with patch.object(submit.subprocess, 'run', side_effect=subprocess.TimeoutExpired('runner', 1)):
            with self.assertRaisesRegex(submit.SubmissionError, '넘었'):
                submit.prepare_answer(self.root, 'PB0001', 1)
        self.assertFalse((self.root/'answers').exists())

    def test_same_source_reuses_bundle_and_changed_source_keeps_both(self):
        first = self.prepare()
        first_metadata = (first.directory/'result.json').read_bytes()
        second = self.prepare()
        self.assertEqual(first.directory, second.directory)
        self.assertEqual((first.directory/'result.json').read_bytes(), first_metadata)
        self.source_path.write_text(EXERCISE+'\n# another attempt\n')
        third = self.prepare()
        self.assertNotEqual(first.directory, third.directory)
        self.assertEqual(len([p for p in (self.root/'answers/PB0001').iterdir() if p.is_dir()]), 2)
        self.assertEqual(submit.load_answer(self.root, 'PB0001').directory, third.directory)
        self.assertEqual(submit.load_answer(self.root, 'PB0001', first.summary['source_sha256']).source, first.source)
        self.source_path.write_text(EXERCISE)
        returned_to_first = self.prepare()
        self.assertEqual(returned_to_first.directory, first.directory)
        self.assertEqual(submit.load_answer(self.root, 'PB0001').directory, first.directory)
        self.assertEqual((first.directory/'result.json').read_bytes(), first_metadata)

    def test_symlinks_and_corrupted_saved_answers_fail_closed(self):
        answer = self.prepare()
        (answer.directory/'solution.py').write_text('different source')
        with self.assertRaisesRegex(submit.SubmissionError, '해시'):
            submit.load_answer(self.root, 'PB0001')
        other = self.root / 'outside-answers'
        other.mkdir()
        (self.root/'answers/CI0001').symlink_to(other, target_is_directory=True)
        with self.assertRaisesRegex(submit.SubmissionError, '심볼릭'):
            submit.load_answer(self.root, 'CI0001')
        for value in ('../PB0001', 'PB0001/../x', 'ZZ0001'):
            with self.assertRaises(submit.SubmissionError):
                submit.problem_id(value)

    def test_corrupt_selection_fails_without_recursion_and_explicit_version_recovers(self):
        answer = self.prepare()
        (answer.directory.parent/'latest.json').write_text('{"schema_version":1,"source_sha256":null}')
        with self.assertRaisesRegex(submit.SubmissionError, '선택 기록'):
            submit.load_answer(self.root, 'PB0001')
        self.assertEqual(submit.load_answer(self.root, 'PB0001', answer.summary['source_sha256']).source, answer.source)

    def test_retry_guidance_preserves_version_repository_and_branch(self):
        answer = self.prepare()
        error_output = StringIO()
        argv = ['submit_answer.py', 'PB0001', '--retry', '--repo', 'owner/repo', '--branch', 'devan/answers']
        with patch.object(sys, 'argv', argv), patch.object(submit, 'ROOT', self.root), \
             patch.object(submit, 'upload_answers', side_effect=submit.SubmissionError('network')), \
             redirect_stdout(StringIO()), redirect_stderr(error_output), self.assertRaises(SystemExit):
            submit.main()
        retry_line = next(line for line in error_output.getvalue().splitlines() if line.startswith('python3 '))
        self.assertEqual(shlex.split(retry_line), ['python3', 'submit_answer.py', 'PB0001', '--retry', '--version',
                         answer.summary['source_sha256'], '--repo', 'owner/repo', '--branch', 'devan/answers'])

    def test_upload_is_one_commit_and_preserves_other_files(self):
        answer = self.prepare()
        client = FakeGitHub()
        client.files['README.md'] = 'untouched'
        url, changed = submit.upload_answers([answer], client.repo, client=client)
        self.assertTrue(changed)
        self.assertIn('/commit/', url)
        self.assertEqual(client.files['README.md'], 'untouched')
        self.assertEqual(set(client.files)-{'README.md'}, {answer.remote_path+'/solution.py', answer.remote_path+'/result.json'})
        self.assertEqual([method for method, _, _ in client.calls if method != 'GET'], ['POST', 'POST', 'PATCH'])
        self.assertEqual(client.files[answer.remote_path+'/solution.py'], answer.source.decode())

    def test_duplicate_upload_performs_no_remote_write(self):
        answer = self.prepare()
        client = FakeGitHub()
        submit.upload_answers([answer], client.repo, client=client)
        client.calls.clear()
        url, changed = submit.upload_answers([answer], client.repo, client=client)
        self.assertFalse(changed)
        self.assertTrue(all(method == 'GET' for method, _, _ in client.calls))
        self.assertIn('/answers', url)

    def test_permission_failure_happens_before_sending_answer_contents(self):
        answer = self.prepare()
        client = FakeGitHub()
        client.can_push = False
        with self.assertRaisesRegex(submit.SubmissionError, '쓰기 권한'):
            submit.upload_answers([answer], client.repo, client=client)
        self.assertTrue(all(method == 'GET' and payload is None for method, _, payload in client.calls))

    def test_retry_keeps_saved_version_even_if_current_code_is_unfinished(self):
        answer = self.prepare()
        self.source_path.write_text(EXERCISE.replace('return value + 1', 'raise NotImplementedError'))
        saved = submit.load_answer(self.root, 'PB0001')
        self.assertEqual(saved.source, answer.source)
        client = FakeGitHub()
        _, changed = submit.upload_answers([saved], client.repo, client=client)
        self.assertTrue(changed)

    def test_invalid_repository_name_makes_no_network_request(self):
        answer = self.prepare()
        client = FakeGitHub()
        for repo in ('owner/..', '../repo', 'owner/repo.git', 'https://github.com/a/b'):
            with self.subTest(repo=repo), self.assertRaises(submit.SubmissionError):
                submit.upload_answers([answer], repo, client=client)
        self.assertEqual(client.calls, [])

    def test_different_remote_contents_are_not_overwritten(self):
        answer = self.prepare()
        client = FakeGitHub()
        client.files[answer.remote_path+'/solution.py'] = 'someone edited this'
        client.files[answer.remote_path+'/result.json'] = json.dumps(answer.summary)
        with self.assertRaisesRegex(submit.SubmissionError, '기존 원격 답안'):
            submit.upload_answers([answer], client.repo, client=client)
        self.assertTrue(all(method == 'GET' for method, _, _ in client.calls))

    def test_conflict_keeps_local_snapshot_for_retry(self):
        answer = self.prepare()
        client = FakeGitHub()
        client.conflict = True
        with self.assertRaisesRegex(submit.SubmissionError, 'conflict'):
            submit.upload_answers([answer], client.repo, client=client)
        self.assertTrue((answer.directory/'solution.py').is_file())
        self.assertFalse(client.files)
        client.conflict = False
        _, changed = submit.upload_answers([submit.load_answer(self.root, 'PB0001')], client.repo, client=client)
        self.assertTrue(changed)

    def test_local_only_cli_never_requires_github(self):
        shutil.copyfile(ROOT/'submit_answer.py', self.root/'submit_answer.py')
        result = subprocess.run([sys.executable, '-B', str(self.root/'submit_answer.py'), 'PB0001', '--local-only'],
                                cwd=self.root, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('LOCAL_ONLY', result.stdout)
        self.assertTrue((self.root/'answers/PB0001').is_dir())

    def enable_batch_fixture(self):
        coding = self.root/'python_coding'
        coding.mkdir()
        (coding/'generated_manifest.json').write_text('{"problems":{}}')
        manifest_path = self.root/'python_basic/catalog/generated_manifest.json'
        manifest = json.loads(manifest_path.read_text())
        starter = EXERCISE.replace('return value + 1', 'raise NotImplementedError("TODO")')
        manifest['problems']['PB0001']['starter_sha256'] = sha256(starter.encode()).hexdigest()
        manifest_path.write_text(json.dumps(manifest))

    def add_batch_problem(self, identity, source, *, pristine=False):
        source = source.replace('PB0001', identity)
        path = self.root/'python_basic'/f'{identity}_demo.py'
        path.write_text(source)
        starter = (source if pristine else EXERCISE.replace('PB0001', identity).replace(
            'return value + 1', 'raise NotImplementedError("TODO")'))
        manifest_path = self.root/'python_basic/catalog/generated_manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['problems'][identity] = {'path': path.name, 'starter_sha256': sha256(starter.encode()).hexdigest()}
        manifest_path.write_text(json.dumps(manifest))
        return path

    def test_batch_discovery_skips_starters_and_unfinished_but_reports_real_errors(self):
        self.enable_batch_fixture()
        self.add_batch_problem('PB0002', EXERCISE, pristine=True)
        self.add_batch_problem('PB0003', EXERCISE.replace('return value + 1', 'raise NotImplementedError("TODO")')+'\n# working\n')
        self.add_batch_problem('PB0004', 'def broken(:\n')
        self.add_batch_problem('PB0005', EXERCISE+'\n# NotImplementedError in a comment is not unfinished\n')
        missing = self.add_batch_problem('PB0006', EXERCISE)
        missing.unlink()
        (self.root/'python_basic/PB0001_personal_copy.py').write_text('raise AssertionError("private draft")')
        archived = self.root/'python_basic/_preserved_answers'
        archived.mkdir()
        (archived/'PB9999_old.py').write_text(EXERCISE)
        selected = submit.discover_answers(self.root)
        self.assertEqual(selected.candidates, ['PB0001', 'PB0004', 'PB0005'])
        self.assertEqual(selected.skipped_starters, 1)
        self.assertEqual(selected.skipped_unfinished, 1)
        self.assertEqual(set(selected.failures), {'PB0006'})
        self.assertFalse((self.root/'answers').exists())

    def test_all_uploads_only_passed_answers_in_one_commit_and_reports_failure(self):
        self.enable_batch_fixture()
        self.add_batch_problem('PB0002', EXERCISE)
        self.add_batch_problem('PB0003', EXERCISE.replace('return value + 1', 'return 0'))
        self.add_batch_problem('PB0004', EXERCISE.replace('return value + 1', 'raise NotImplementedError("TODO")')+'\n# working\n')
        self.add_batch_problem('PB0005', EXERCISE, pristine=True)
        client, output, errors = FakeGitHub(), StringIO(), StringIO()
        with patch.object(submit, 'ROOT', self.root), patch.object(sys, 'argv', ['submit_answer.py', '--all']), \
             patch.object(submit, 'GitHub', return_value=client), redirect_stdout(output), redirect_stderr(errors):
            with self.assertRaises(SystemExit) as exit_result:
                submit.main()
        self.assertEqual(exit_result.exception.code, 2)
        self.assertIn('BATCH_SUMMARY passed=2 failed=1 untouched=1 unfinished=1', output.getvalue())
        self.assertIn('UPLOADED', output.getvalue())
        self.assertIn('FAILED PB0003', errors.getvalue())
        self.assertEqual(len(client.files), 4)
        self.assertEqual({path.split('/')[1] for path in client.files}, {'PB0001', 'PB0002'})
        self.assertEqual([method for method, _, _ in client.calls if method != 'GET'], ['POST', 'POST', 'PATCH'])

    def test_explicit_id_batch_remains_all_or_nothing_on_verification_failure(self):
        self.enable_batch_fixture()
        self.add_batch_problem('PB0002', EXERCISE.replace('return value + 1', 'return 0'))
        with patch.object(submit, 'ROOT', self.root), \
             patch.object(sys, 'argv', ['submit_answer.py', 'PB0001', 'PB0002']), \
             patch.object(submit, 'GitHub') as client, redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            with self.assertRaises(SystemExit) as exit_result:
                submit.main()
        self.assertEqual(exit_result.exception.code, 1)
        client.assert_not_called()
        self.assertTrue((self.root/'answers/PB0001/latest.json').is_file())

    def test_empty_all_does_not_contact_github(self):
        self.enable_batch_fixture()
        self.add_batch_problem('PB0001', EXERCISE, pristine=True)
        output = StringIO()
        with patch.object(submit, 'ROOT', self.root), patch.object(sys, 'argv', ['submit_answer.py', '--all']), \
             patch.object(submit, 'GitHub') as client, redirect_stdout(output):
            submit.main()
        client.assert_not_called()
        self.assertIn('NOTHING_TO_UPLOAD', output.getvalue())
        self.assertFalse((self.root/'answers').exists())

    def test_crlf_only_changes_do_not_select_untouched_runnable_starters(self):
        self.enable_batch_fixture()
        path = self.add_batch_problem('PB0001', EXERCISE, pristine=True)
        path.write_bytes(EXERCISE.replace('\n', '\r\n').encode())
        selected = submit.discover_answers(self.root)
        self.assertEqual(selected.candidates, [])
        self.assertEqual(selected.skipped_starters, 1)

    def test_all_local_only_then_all_retry_uses_saved_versions(self):
        self.enable_batch_fixture()
        second = self.add_batch_problem('PB0002', EXERCISE)
        with patch.object(submit, 'ROOT', self.root), \
             patch.object(sys, 'argv', ['submit_answer.py', '--all', '--local-only']), \
             patch.object(submit, 'GitHub') as client, redirect_stdout(StringIO()):
            submit.main()
        client.assert_not_called()
        second.write_text('def still_editing(:')
        (self.root/'answers/personal-notes.txt').write_text('never upload me')
        client = FakeGitHub()
        with patch.object(submit, 'ROOT', self.root), \
             patch.object(sys, 'argv', ['submit_answer.py', '--all', '--retry']), \
             patch.object(submit, 'GitHub', return_value=client), redirect_stdout(StringIO()):
            submit.main()
        self.assertEqual(len(client.files), 4)
        self.assertFalse(any('personal-notes' in path for path in client.files))
        self.assertFalse(any('still_editing' in content for content in client.files.values()))

    def test_all_retry_reports_corrupt_snapshot_and_still_uploads_valid_one(self):
        self.enable_batch_fixture()
        self.add_batch_problem('PB0002', EXERCISE)
        with redirect_stdout(StringIO()):
            good = submit.prepare_answer(self.root, 'PB0001')
            bad = submit.prepare_answer(self.root, 'PB0002')
        (bad.directory/'solution.py').write_text('corrupted')
        client = FakeGitHub()
        with patch.object(submit, 'ROOT', self.root), \
             patch.object(sys, 'argv', ['submit_answer.py', '--all', '--retry']), \
             patch.object(submit, 'GitHub', return_value=client), redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            with self.assertRaises(SystemExit) as exit_result:
                submit.main()
        self.assertEqual(exit_result.exception.code, 2)
        self.assertEqual(set(client.files), {good.remote_path+'/solution.py', good.remote_path+'/result.json'})

    def test_all_invalid_combinations_are_rejected_before_network(self):
        for arguments in ([], ['--all', 'PB0001'], ['--all', '--retry', '--version', 'a'*64]):
            with self.subTest(arguments=arguments), patch.object(sys, 'argv', ['submit_answer.py', *arguments]), \
                 patch.object(submit, 'GitHub') as client, redirect_stderr(StringIO()):
                with self.assertRaises(SystemExit) as exit_result:
                    submit.main()
                self.assertEqual(exit_result.exception.code, 2)
                client.assert_not_called()


class GitHubTransportTests(unittest.TestCase):
    def test_gh_uses_json_stdin_and_does_not_embed_source_in_argv(self):
        response = subprocess.CompletedProcess([], 0, 'HTTP/2.0 201 Created\nContent-Type: application/json\n\n{"sha":"abc"}', '')
        payload = {'tree': [{'content': 'sensitive-source-marker'}]}
        with patch.object(submit.subprocess, 'run', return_value=response) as run:
            self.assertEqual(submit.GitHub().request('POST', 'repos/a/b/git/trees', payload), {'sha': 'abc'})
        command = run.call_args.args[0]
        self.assertNotIn('sensitive-source-marker', ' '.join(command))
        self.assertEqual(json.loads(run.call_args.kwargs['input']), payload)
        self.assertIn('github.com', command)

    def test_only_explicit_404_reads_are_optional(self):
        response = subprocess.CompletedProcess([], 1, 'HTTP/2.0 404 Not Found\n\n{"message":"Not Found"}', '')
        with patch.object(submit.subprocess, 'run', return_value=response):
            self.assertIsNone(submit.GitHub().request('GET', 'repos/a/b/contents/answers', missing_ok=True))
            with self.assertRaisesRegex(submit.SubmissionError, '404'):
                submit.GitHub().request('GET', 'repos/a/b')


if __name__ == '__main__':
    unittest.main()
