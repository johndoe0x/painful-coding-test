from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

from bank_inventory import find_managed_problem, managed_paths
from review_bank import NormalizeFunction, ROOT, call_errors
from export_public import PUBLIC_SOURCE_FILES, PUBLIC_DOCUMENTS
import run_problem


class InventoryTests(unittest.TestCase):
    def test_duplicate_personal_draft_does_not_ambiguate_managed_problem(self):
        # Resolving an ID must not scan drafts or historical answer directories.
        with patch.object(Path, "rglob", side_effect=AssertionError("must use manifest")):
            path = run_problem.find_problem("PB0003")
        self.assertEqual(path.name, "PB0003_hello_world_many_greetings_v03.py")

    def test_missing_canonical_file_never_falls_back_to_another_answer(self):
        with patch("bank_inventory.Path.is_file", return_value=False):
            with self.assertRaisesRegex(ValueError, "missing"):
                find_managed_problem(ROOT, "PB0003")

    def test_manifest_cannot_select_outside_bank_or_wrong_problem(self):
        paths = ("../../README.md", "/tmp/PB0003_test.py", "01/PB0004_other.py",
                 "_preserved_answers/PB0003_old.py")
        for path in paths:
            with self.subTest(path=path):
                data = json.dumps({"problems": {"PB0003": {"path": path}}})
                with patch.object(Path, "read_text", return_value=data):
                    with self.assertRaisesRegex(ValueError, "Invalid managed problem path"):
                        managed_paths(ROOT, "PB")

    def test_regeneration_leaves_sole_draft_when_canonical_is_missing(self):
        code = '''
from pathlib import Path
from unittest.mock import patch
from regenerate_problems import build_catalog, load_manifest, plan_actions, ROOT
build = build_catalog()[2]
draft = ROOT / "01_introduction/PB0003_personal.py"
with patch("regenerate_problems.existing_problems", return_value={"PB0003": [draft]}):
    action = plan_actions([build], load_manifest())[0]
assert action.previous_path is None
assert action.reason == "created"
assert action.archive_source is None
'''
        result = subprocess.run([sys.executable, "-B", "-c", code], cwd=ROOT / "python_basic",
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_publication_uses_explicit_inputs_without_personal_data(self):
        files = (*PUBLIC_SOURCE_FILES, *PUBLIC_DOCUMENTS)
        self.assertEqual(len(files), len(set(files)))
        self.assertNotIn("python_basic/my_solution.py", files)
        self.assertNotIn("tests/test_private_quality.py", files)
        for name in files:
            self.assertFalse(any(token in name for token in ("*", "proofs/", "_preserved_answers/", ".zed/")))

    def test_basic_unmanifested_partial_answer_is_preserved(self):
        code = '''
from pathlib import Path
from unittest.mock import patch
from regenerate_problems import build_catalog, plan_actions, ROOT
build = build_catalog()[0]
path = ROOT / build.relative_path
partial = build.starter_source.replace("    raise NotImplementedError", "    progress = 1\\n    raise NotImplementedError")
with patch("regenerate_problems.existing_problems", return_value={build.problem_id: [path]}), patch.object(Path, "read_text", return_value=partial):
    action = plan_actions([build], {"problems": {}})[0]
assert action.reason == "preserved_user_work", action.reason
assert action.archive_source.endswith("\\0" + partial)
assert "progress = 1" in action.source
'''
        result = subprocess.run([sys.executable, "-B", "-c", code], cwd=ROOT / "python_basic",
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)


class CallContractTests(unittest.TestCase):
    def test_missing_required_parameter_is_rejected(self):
        definition = ast.parse("def nearest(values, target): pass").body[0]
        self.assertEqual(call_errors(definition, ["nearest([]) is None"]),
                         ["example 1: missing a required argument: 'target'"])

    def test_defaults_and_keyword_only_binding(self):
        definition = ast.parse("def solve(a, /, b=2, *, c): pass").body[0]
        self.assertEqual(call_errors(definition, ["solve(1, c=3) == 4"]), [])
        self.assertTrue(call_errors(definition, ["solve(a=1, c=3) == 4"]))
        self.assertTrue(call_errors(definition, ["solve(1) == 4"]))

    def test_normalization_only_changes_function_identifiers(self):
        tree = NormalizeFunction("foo").visit(ast.parse("foo('foo') == 'foo'", mode="eval"))
        expected = ast.parse("__target__('foo') == 'foo'", mode="eval")
        self.assertEqual(ast.dump(tree), ast.dump(expected))
        different = NormalizeFunction("bar").visit(ast.parse("bar('bar') == 'bar'", mode="eval"))
        self.assertNotEqual(ast.dump(tree), ast.dump(different))


if __name__ == "__main__":
    unittest.main()
