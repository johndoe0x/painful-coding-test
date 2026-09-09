"""Verify selected answers and upload them to a GitHub answers/ directory."""

from __future__ import annotations

import argparse
import base64
from dataclasses import dataclass
from datetime import datetime
import errno
from hashlib import sha1, sha256
import json
import os
from pathlib import Path
import re
import shlex
import subprocess
import sys
from urllib.parse import quote
from uuid import uuid4

from bank_inventory import find_managed_problem
from run_problem import OutputRecord, print_output_records


ROOT = Path(__file__).resolve().parent
DEFAULT_REPO = "johndoe0x/painful-coding-test"
ID_RE = re.compile(r"(?:PB|CI)\d{4}\Z")
HASH_RE = re.compile(r"[0-9a-f]{64}\Z")
SUMMARY_FIELDS = {
    "schema_version", "problem_id", "source_sha256", "checked_at_utc",
    "python_version", "verification", "status", "public_examples_passed",
    "self_test_asserts", "source_checks",
}
MAX_SOURCE_BYTES = 512_000


class SubmissionError(RuntimeError):
    pass


@dataclass(frozen=True)
class Answer:
    problem_id: str
    source: bytes
    summary: dict
    directory: Path

    @property
    def remote_path(self) -> str:
        return f"answers/{self.problem_id}/{self.summary['source_sha256']}"

    def files(self) -> dict[str, str]:
        return {
            "solution.py": self.source.decode("utf-8"),
            "result.json": json.dumps(self.summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        }


def problem_id(value: str) -> str:
    value = value.upper()
    if not ID_RE.fullmatch(value):
        raise SubmissionError("문제 ID는 PB0001 또는 CI0022 형식이어야 합니다.")
    return value


def ensure_directory(root: Path, *parts: str) -> Path:
    current = root
    for part in parts:
        if part in {"", ".", ".."} or "/" in part or "\\" in part:
            raise SubmissionError("허용되지 않는 답안 경로입니다.")
        current = current / part
        if current.is_symlink():
            raise SubmissionError(f"심볼릭 링크 경로에는 답안을 저장하지 않습니다: {current}")
        current.mkdir(mode=0o700, exist_ok=True)
    return current


def validate_summary(summary: dict, identity: str, digest: str) -> None:
    if not ID_RE.fullmatch(identity) or not HASH_RE.fullmatch(digest):
        raise SubmissionError("저장된 답안 ID 또는 해시가 올바르지 않습니다.")
    if not isinstance(summary, dict) or set(summary) != SUMMARY_FIELDS:
        raise SubmissionError("저장된 결과 요약의 형식이 올바르지 않습니다.")
    if (type(summary["schema_version"]) is not int or summary["schema_version"] != 1 or summary["status"] != "PASS"
            or summary["verification"] != "PUBLIC_EXAMPLES_AND_SELF_TEST"
            or summary["problem_id"] != identity or summary["source_sha256"] != digest):
        raise SubmissionError("답안 ID·소스 해시·검증 결과가 일치하지 않습니다.")
    for key in ("public_examples_passed", "self_test_asserts"):
        minimum = 2 if key == "self_test_asserts" else 1
        if type(summary[key]) is not int or summary[key] < minimum:
            raise SubmissionError("저장된 테스트 개수가 올바르지 않습니다.")
    if not isinstance(summary["source_checks"], list) or not all(
        isinstance(value, str) for value in summary["source_checks"]
    ):
        raise SubmissionError("저장된 소스 검사 목록이 올바르지 않습니다.")
    try:
        timestamp = datetime.fromisoformat(summary["checked_at_utc"].replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            raise ValueError("missing timezone")
    except (ValueError, TypeError, AttributeError) as error:
        raise SubmissionError("저장된 검증 시각이 올바르지 않습니다.") from error
    if not isinstance(summary["python_version"], str):
        raise SubmissionError("저장된 Python 버전이 올바르지 않습니다.")


def selected_version(value: dict) -> str:
    if (not isinstance(value, dict) or set(value) != {"schema_version", "source_sha256"}
            or type(value["schema_version"]) is not int or value["schema_version"] != 1
            or not isinstance(value["source_sha256"], str)
            or not HASH_RE.fullmatch(value["source_sha256"])):
        raise SubmissionError("마지막 답안 선택 기록이 올바르지 않습니다. --version으로 지정하세요.")
    return value["source_sha256"]


def load_answer(root: Path, identity: str, version: str | None = None) -> Answer:
    identity = problem_id(identity)
    parent = root / "answers" / identity
    if (root / "answers").is_symlink() or parent.is_symlink():
        raise SubmissionError("심볼릭 링크 답안 경로를 읽지 않습니다.")
    if version is None:
        pointer = parent / "latest.json"
        if pointer.is_symlink():
            raise SubmissionError("심볼릭 링크 답안 선택 기록을 읽지 않습니다.")
        if pointer.exists():
            try:
                selected = json.loads(pointer.read_text(encoding="utf-8"))
                return load_answer(root, identity, selected_version(selected))
            except (ValueError, TypeError, KeyError) as error:
                raise SubmissionError("마지막 답안 선택 기록이 올바르지 않습니다. --version으로 지정하세요.") from error
        candidates = []
        if parent.is_dir():
            for path in parent.iterdir():
                if HASH_RE.fullmatch(path.name):
                    candidates.append(load_answer(root, identity, path.name))
        if not candidates:
            raise SubmissionError(f"{identity}: 저장된 답안이 없습니다. 먼저 문제를 검증하세요.")
        return max(candidates, key=lambda answer: answer.summary["checked_at_utc"])
    if not HASH_RE.fullmatch(version):
        raise SubmissionError("답안 버전은 64자리 소스 SHA-256이어야 합니다.")
    directory = parent / version
    paths = [directory, directory / "solution.py", directory / "result.json"]
    if any(path.is_symlink() for path in paths):
        raise SubmissionError("심볼릭 링크 답안 파일을 읽지 않습니다.")
    try:
        source = paths[1].read_bytes()
        summary = json.loads(paths[2].read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise SubmissionError(f"{identity}: 저장된 답안이 불완전하거나 손상됐습니다.") from error
    if len(source) > MAX_SOURCE_BYTES or sha256(source).hexdigest() != version:
        raise SubmissionError(f"{identity}: 저장된 답안의 해시가 일치하지 않습니다.")
    validate_summary(summary, identity, version)
    return Answer(identity, source, summary, directory)


def select_latest(root: Path, answer: Answer) -> Answer:
    """Select the last prepared version, even when it reuses an older snapshot."""
    pointer = answer.directory.parent / "latest.json"
    if pointer.is_symlink():
        raise SubmissionError("심볼릭 링크 선택 기록을 덮어쓰지 않습니다.")
    if pointer.exists():
        existing = json.loads(pointer.read_text(encoding="utf-8"))
        selected_version(existing)
    stage = ensure_directory(root, ".tmp", f"submit-selection-{uuid4().hex}")
    temporary = stage / "latest.json"
    try:
        temporary.write_text(json.dumps({"schema_version": 1, "source_sha256": answer.summary["source_sha256"]}) + "\n", encoding="utf-8")
        temporary.replace(pointer)
    finally:
        temporary.unlink(missing_ok=True)
        stage.rmdir()
    return answer


def save_answer(root: Path, identity: str, source: bytes, summary: dict) -> Answer:
    digest = sha256(source).hexdigest()
    validate_summary(summary, identity, digest)
    parent = ensure_directory(root, "answers", identity)
    destination = parent / digest
    if destination.exists() or destination.is_symlink():
        return select_latest(root, load_answer(root, identity, digest))
    stage = ensure_directory(root, ".tmp", f"submit-{uuid4().hex}")
    answer = Answer(identity, source, summary, destination)
    try:
        for name, content in answer.files().items():
            with (stage / name).open("x", encoding="utf-8", newline="\n") as output:
                output.write(content)
                output.flush()
                os.fsync(output.fileno())
        try:
            os.rename(stage, destination)
        except OSError as error:
            if error.errno not in (errno.EEXIST, errno.ENOTEMPTY):
                raise
            return select_latest(root, load_answer(root, identity, digest))
    finally:
        if stage.exists():
            for name in ("solution.py", "result.json"):
                (stage / name).unlink(missing_ok=True)
            stage.rmdir()
    return select_latest(root, answer)


def prepare_answer(root: Path, identity: str, timeout: float = 30) -> Answer:
    identity = problem_id(identity)
    path = find_managed_problem(root, identity)
    source = path.read_bytes()
    if len(source) > MAX_SOURCE_BYTES:
        raise SubmissionError(f"{identity}: 답안은 {MAX_SOURCE_BYTES:,}바이트 이하여야 합니다.")
    try:
        completed = subprocess.run(
            [sys.executable, "-B", str(root / "run_problem.py"), identity,
             "--strict", "--no-receipt", "--json"],
            cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=timeout,
        )
    except subprocess.TimeoutExpired as error:
        raise SubmissionError(f"{identity}: 실행이 {timeout:g}초를 넘었습니다. 답안은 업로드하지 않았습니다.") from error
    try:
        receipt = json.loads(completed.stdout)
    except ValueError as error:
        raise SubmissionError(f"{identity}: 실행 결과를 읽을 수 없습니다. 기존 runner로 코드를 확인하세요.") from error
    if not isinstance(receipt, dict):
        raise SubmissionError(f"{identity}: 실행 결과 형식이 올바르지 않습니다.")
    print(f"{receipt.get('status', 'FAIL')} {identity}")
    print(f"SOURCE {path.relative_to(root).as_posix()}")
    print_output_records([OutputRecord(**row) for row in receipt.get("execution_output", [])])
    if completed.returncode != 0 or receipt.get("status") != "PASS":
        raise SubmissionError(f"{identity}: {receipt.get('error', '검증 실패')}")
    digest = sha256(source).hexdigest()
    if path.read_bytes() != source or receipt.get("source_sha256") != digest:
        raise SubmissionError(f"{identity}: 검증 중 코드가 변경됐습니다. 저장 후 다시 실행하세요.")
    if (receipt.get("problem_id") != identity or receipt.get("strict") is not True
            or receipt.get("self_test", {}).get("passed") is not True
            or receipt.get("source_checks", {}).get("passed") is not True
            or not receipt.get("public_examples")
            or not all(row.get("passed") is True for row in receipt["public_examples"])):
        raise SubmissionError(f"{identity}: 완전한 검증 결과가 아닙니다.")
    summary = {
        "schema_version": 1, "problem_id": identity, "source_sha256": digest,
        "checked_at_utc": receipt["verified_at_utc"], "python_version": receipt["python_version"],
        "verification": "PUBLIC_EXAMPLES_AND_SELF_TEST", "status": "PASS",
        "public_examples_passed": len(receipt["public_examples"]),
        "self_test_asserts": receipt["self_test"]["assert_count"],
        "source_checks": receipt["source_checks"]["required"],
    }
    answer = save_answer(root, identity, source, summary)
    print(f"SAVED {answer.directory}")
    return answer


class GitHub:
    def request(self, method: str, endpoint: str, payload: dict | None = None,
                *, missing_ok: bool = False):
        command = ["gh", "api", "--hostname", "github.com", "--include", "--method", method,
                   "-H", "Accept: application/vnd.github+json",
                   "-H", "X-GitHub-Api-Version: 2026-03-10", endpoint]
        if payload is not None:
            command += ["--input", "-"]
        try:
            result = subprocess.run(command, input=json.dumps(payload) if payload is not None else None,
                                    capture_output=True, text=True, encoding="utf-8", timeout=45)
        except FileNotFoundError as error:
            raise SubmissionError("GitHub CLI(gh)를 설치하고 gh auth login을 실행하세요.") from error
        except subprocess.TimeoutExpired as error:
            raise SubmissionError("GitHub 응답이 지연됐습니다. --retry로 완료 여부를 확인하고 재시도하세요.") from error
        headers, separator, body = result.stdout.replace("\r\n", "\n").partition("\n\n")
        match = re.match(r"HTTP/\S+\s+(\d{3})", headers)
        status = int(match[1]) if match else 0
        if status == 404 and missing_ok:
            return None
        if result.returncode or not 200 <= status < 300:
            reason = {401: "gh auth login으로 로그인하세요.", 403: "권한 또는 API 사용 한도를 확인하세요.",
                      404: "저장소·브랜치 또는 접근 권한을 확인하세요.",
                      409: "원격 변경과 충돌했습니다. --retry로 재시도하세요.",
                      422: "원격 변경 또는 브랜치 규칙을 확인한 뒤 --retry로 재시도하세요."}.get(
                          status, "gh auth status와 네트워크 연결을 확인하세요.")
            raise SubmissionError(f"GitHub HTTP {status or '응답 없음'}: {reason}")
        try:
            return json.loads(body) if separator and body.strip() else {}
        except ValueError as error:
            raise SubmissionError("GitHub JSON 응답을 읽을 수 없습니다. --retry로 재시도하세요.") from error


def git_blob_hash(content: str) -> str:
    data = content.encode("utf-8")
    return sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def object_sha(value: str) -> str:
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{40}", value):
        raise SubmissionError("GitHub의 commit/tree SHA를 확인할 수 없습니다.")
    return value


def upload_answers(answers: list[Answer], repo: str, branch: str | None = None,
                   client: GitHub | None = None) -> tuple[str, bool]:
    if (not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_.-]+", repo)
            or repo.rsplit('/', 1)[-1] in {'.', '..'} or repo.endswith('.git')):
        raise SubmissionError("저장소는 OWNER/REPO 형식이어야 합니다.")
    if not answers:
        raise SubmissionError("업로드할 답안이 없습니다.")
    for answer in answers:
        validate_summary(answer.summary, answer.problem_id, sha256(answer.source).hexdigest())
    client = client or GitHub()
    endpoint = f"repos/{repo}"
    info = client.request("GET", endpoint)
    if info.get("permissions", {}).get("push") is not True:
        raise SubmissionError(f"{repo}: 현재 GitHub 계정에 쓰기 권한이 없습니다.")
    branch = branch or info.get("default_branch")
    if not branch:
        raise SubmissionError("먼저 GitHub 저장소에 README를 만들어 기본 브랜치를 준비하세요.")
    ref_path = f"heads/{quote(branch, safe='')}"
    ref = client.request("GET", f"{endpoint}/git/ref/{ref_path}")
    if ref.get("ref") != f"refs/heads/{branch}" or ref.get("object", {}).get("type") != "commit":
        raise SubmissionError("대상 브랜치를 정확히 확인할 수 없습니다.")
    head = object_sha(ref["object"]["sha"])
    commit = client.request("GET", f"{endpoint}/git/commits/{head}")
    base_tree = object_sha(commit["tree"]["sha"])
    entries = []
    for answer in answers:
        validate_summary(answer.summary, answer.problem_id, sha256(answer.source).hexdigest())
        files = answer.files()
        existing = client.request("GET", f"{endpoint}/contents/{answer.remote_path}?ref={head}", missing_ok=True)
        if existing is not None:
            if not isinstance(existing, list):
                raise SubmissionError(f"{answer.problem_id}: 원격 답안 경로가 폴더가 아닙니다.")
            by_name = {row["name"]: row for row in existing}
            if (not {"solution.py", "result.json"} <= by_name.keys()
                    or any(by_name[name].get("type") != "file" for name in files)
                    or by_name["solution.py"]["sha"] != git_blob_hash(files["solution.py"])):
                raise SubmissionError(f"{answer.problem_id}: 기존 원격 답안이 다르거나 불완전합니다. 덮어쓰지 않았습니다.")
            metadata = client.request("GET", f"{endpoint}/contents/{answer.remote_path}/result.json?ref={head}")
            if metadata.get("encoding") != "base64":
                raise SubmissionError("기존 원격 결과의 인코딩을 확인할 수 없습니다.")
            summary = json.loads(base64.b64decode(metadata["content"]))
            validate_summary(summary, answer.problem_id, answer.summary["source_sha256"])
            continue
        entries.extend({"path": f"{answer.remote_path}/{name}", "mode": "100644", "type": "blob", "content": content}
                       for name, content in files.items())
    if not entries:
        return f"https://github.com/{repo}/tree/{head}/answers", False
    profile = client.request("GET", "user")
    tree = client.request("POST", f"{endpoint}/git/trees", {"base_tree": base_tree, "tree": entries})
    new_commit = client.request("POST", f"{endpoint}/git/commits", {
        "message": "answers: " + ", ".join(answer.problem_id for answer in answers),
        "tree": object_sha(tree["sha"]), "parents": [head],
        "author": {"name": profile["login"], "email": f"{profile['id']}+{profile['login']}@users.noreply.github.com"},
    })
    new_sha = object_sha(new_commit["sha"])
    updated = client.request("PATCH", f"{endpoint}/git/refs/{ref_path}", {"sha": new_sha, "force": False})
    if updated.get("object", {}).get("sha") != new_commit["sha"]:
        raise SubmissionError("업로드 완료 응답을 확인할 수 없습니다. --retry로 확인하세요.")
    return f"https://github.com/{repo}/commit/{new_commit['sha']}", True


def main() -> None:
    parser = argparse.ArgumentParser(description="검증한 PB/CI 답안을 GitHub answers/에 올립니다.")
    parser.add_argument("problem_ids", nargs="+", help="예: PB0001 CI0022")
    parser.add_argument("--local-only", action="store_true", help="로컬 이력만 저장하며 네트워크를 사용하지 않습니다.")
    parser.add_argument("--retry", action="store_true", help="현재 코드 대신 마지막으로 저장한 답안을 업로드합니다.")
    parser.add_argument("--version", help="--retry 시 업로드할 소스 SHA-256 (문제 한 개만)")
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"기본 공개 저장소: {DEFAULT_REPO}")
    parser.add_argument("--branch", help="생략하면 저장소의 기본 브랜치")
    parser.add_argument("--timeout", type=float, default=30, help="문제별 검증 제한 초 (기본 30)")
    args = parser.parse_args()
    if args.version and (not args.retry or len(args.problem_ids) != 1):
        parser.error("--version은 문제 한 개의 --retry에서만 사용합니다.")
    if not 0 < args.timeout <= 300:
        parser.error("--timeout은 0보다 크고 300 이하여야 합니다.")
    upload_started = False
    answers = []
    try:
        identities = list(dict.fromkeys(problem_id(value) for value in args.problem_ids))
        answers = [load_answer(ROOT, identity, args.version) if args.retry else
                   prepare_answer(ROOT, identity, args.timeout) for identity in identities]
        if args.local_only:
            print("LOCAL_ONLY: 답안이 저장됐습니다. 업로드하려면 같은 ID에 --retry를 사용하세요.")
            return
        print(f"UPLOAD TARGET: {args.repo}/answers/")
        upload_started = True
        url, changed = upload_answers(answers, args.repo, args.branch)
        print(("UPLOADED " if changed else "ALREADY_UPLOADED ") + url)
    except (SubmissionError, OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        if upload_started:
            print("저장된 답안은 유지됩니다. 다음 명령으로 같은 버전을 재시도할 수 있습니다.", file=sys.stderr)
            for answer in answers:
                retry = ["python3", "submit_answer.py", answer.problem_id, "--retry", "--version",
                         answer.summary["source_sha256"], "--repo", args.repo]
                if args.branch:
                    retry += ["--branch", args.branch]
                print(shlex.join(retry), file=sys.stderr)
        else:
            print("GitHub 업로드는 실행하지 않았습니다. 코드를 확인한 뒤 기본 명령을 다시 실행하세요.", file=sys.stderr)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
