from __future__ import annotations

import argparse
import ast
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from hashlib import sha256
import importlib.util
from io import StringIO
import json
import logging
from pathlib import Path
import platform
import re
import sys
from time import perf_counter
from types import ModuleType
from typing import Iterator

from python_basic.source_checks import CHECK_DESCRIPTIONS, failed_source_checks
from bank_inventory import find_managed_problem


ROOT = Path(__file__).resolve().parent
PROOF_ROOT = ROOT / "proofs"
ID_PATTERN = re.compile(r"^(PB|CI)(\d{4})$")
MAX_CAPTURED_OUTPUT_CHARS = 20_000


class ProofFailure(RuntimeError):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.output_records: list[OutputRecord] = []


@dataclass(frozen=True)
class OutputRecord:
    phase: str
    stdout: str
    stderr: str


def clipped_output(text: str) -> str:
    if len(text) <= MAX_CAPTURED_OUTPUT_CHARS:
        return text
    omitted = len(text) - MAX_CAPTURED_OUTPUT_CHARS
    return (
        text[:MAX_CAPTURED_OUTPUT_CHARS]
        + f"\n... 출력 {omitted}자가 생략되었습니다.\n"
    )


class OutputCollector:
    def __init__(self) -> None:
        self.records: list[OutputRecord] = []

    @contextmanager
    def capture(self, phase: str) -> Iterator[None]:
        stdout_buffer = StringIO()
        stderr_buffer = StringIO()
        root_logger = logging.getLogger()
        previous_handlers = list(root_logger.handlers)
        previous_level = root_logger.level
        log_handler = logging.StreamHandler(stderr_buffer)
        log_handler.setFormatter(
            logging.Formatter("%(levelname)s:%(name)s:%(message)s")
        )
        root_logger.handlers = [log_handler]
        root_logger.setLevel(logging.DEBUG)
        try:
            with redirect_stdout(stdout_buffer), redirect_stderr(stderr_buffer):
                yield
        finally:
            root_logger.handlers = previous_handlers
            root_logger.setLevel(previous_level)
            stdout = clipped_output(stdout_buffer.getvalue())
            stderr = clipped_output(stderr_buffer.getvalue())
            if stdout or stderr:
                self.records.append(OutputRecord(phase, stdout, stderr))


def print_output_records(records: list[OutputRecord]) -> None:
    if not records:
        print("user_output=none", flush=True)
        return
    print(f"user_output_records={len(records)}", flush=True)
    print("USER_OUTPUT_BEGIN", flush=True)
    for record in records:
        if record.stdout:
            print(f"[{record.phase} stdout]", flush=True)
            print(record.stdout, end="" if record.stdout.endswith("\n") else "\n", flush=True)
        if record.stderr:
            print(f"[{record.phase} stderr/log]", flush=True)
            print(record.stderr, end="" if record.stderr.endswith("\n") else "\n", flush=True)
    print("USER_OUTPUT_END", flush=True)


def problem_root(problem_id: str) -> Path:
    if problem_id.startswith("PB"):
        return ROOT / "python_basic"
    if problem_id.startswith("CI"):
        return ROOT / "python_coding"
    raise ProofFailure(f"지원하지 않는 문제 ID입니다: {problem_id}")


def find_problem(problem_id: str) -> Path:
    match = ID_PATTERN.fullmatch(problem_id)
    if match is None:
        raise ProofFailure("문제 ID는 PB0001 또는 CI0001 형식이어야 합니다.")
    try:
        return find_managed_problem(ROOT, problem_id)
    except (ValueError, OSError, KeyError) as error:
        raise ProofFailure(f"문제 목록 확인 실패: {error}") from error


def parse_source(path: Path) -> tuple[str, ast.Module]:
    source = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(source, filename=str(path))
    except SyntaxError as error:
        raise ProofFailure(f"Python 문법 오류: {error}") from error
    return source, tree


def is_not_implemented_raise(node: ast.Raise) -> bool:
    exception = node.exc
    if isinstance(exception, ast.Name):
        return exception.id == "NotImplementedError"
    if isinstance(exception, ast.Call) and isinstance(exception.func, ast.Name):
        return exception.func.id == "NotImplementedError"
    return False


def unfinished_lines(tree: ast.Module) -> list[int]:
    return sorted(
        node.lineno
        for node in ast.walk(tree)
        if isinstance(node, ast.Raise) and is_not_implemented_raise(node)
    )


def extract_examples(tree: ast.Module) -> list[str]:
    docstring = ast.get_docstring(tree) or ""
    bullet_match = re.search(
        r"예시 및 필수 테스트\n-+\n(?P<body>.*?)\n\n완료 조건",
        docstring,
        re.DOTALL,
    )
    if bullet_match is not None:
        examples = [
            line.removeprefix("- ").strip()
            for line in bullet_match.group("body").splitlines()
            if line.strip().startswith("- ")
        ]
        if examples:
            return examples
    match = re.search(
        r"공개 예시\n-+\n(?P<body>.*?)\n\n(?:전용 테스트|필수 검증식)",
        docstring,
        re.DOTALL,
    )
    if match is None:
        match = re.search(r"예시\n-+\n(?P<body>.*?)\n\n완료 조건", docstring, re.DOTALL)
    if match is None:
        raise ProofFailure("문제 docstring에서 예시를 찾을 수 없습니다.")
    examples = [part.strip() for part in match.group("body").split(";") if part.strip()]
    if not examples:
        raise ProofFailure("실행할 공개 예시가 없습니다.")
    return examples


def extract_source_checks(tree: ast.Module) -> tuple[str, ...]:
    docstring = ast.get_docstring(tree) or ""
    match = re.search(
        r"^Source checks:[ \t]*(?P<checks>.*)$",
        docstring,
        re.MULTILINE,
    )
    if match is None or not match.group("checks").strip():
        return ()
    checks = tuple(
        part.strip()
        for part in match.group("checks").split(",")
        if part.strip()
    )
    unknown = set(checks) - CHECK_DESCRIPTIONS.keys()
    if unknown:
        raise ProofFailure(f"알 수 없는 소스 검사입니다: {sorted(unknown)}")
    return checks


def primary_function_name(tree: ast.Module) -> str:
    functions = [
        node.name
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name != "self_test"
    ]
    if len(functions) != 1:
        raise ProofFailure(f"구현할 함수가 정확히 하나여야 합니다. 현재 {len(functions)}개입니다.")
    return functions[0]


def self_test_metadata(tree: ast.Module) -> tuple[bool, int]:
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "self_test":
            assert_count = sum(isinstance(child, ast.Assert) for child in ast.walk(node))
            return True, assert_count
    return False, 0


def load_module(
    path: Path,
    problem_id: str,
    output: OutputCollector,
) -> ModuleType:
    module_name = f"_neetcode_proof_{problem_id.lower()}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ProofFailure(f"모듈을 불러올 수 없습니다: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    previous_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    try:
        with output.capture("import"):
            spec.loader.exec_module(module)
    except Exception as error:
        raise ProofFailure(f"파일 import 중 오류가 발생했습니다: {type(error).__name__}: {error}") from error
    finally:
        sys.dont_write_bytecode = previous_dont_write_bytecode
        sys.modules.pop(module_name, None)
    return module


def run_examples(
    module: ModuleType,
    examples: list[str],
    path: Path,
    output: OutputCollector,
) -> list[dict[str, object]]:
    results: list[dict[str, object]] = []
    namespace = vars(module)
    for index, expression in enumerate(examples, start=1):
        started = perf_counter()
        try:
            with output.capture(f"public_example_{index}"):
                value = eval(compile(expression, str(path), "eval"), namespace)
        except Exception as error:
            raise ProofFailure(
                f"공개 예시 실행 실패: {expression}\n"
                f"{type(error).__name__}: {error}"
            ) from error
        elapsed_ms = (perf_counter() - started) * 1000
        if value is not True:
            raise ProofFailure(f"공개 예시가 True가 아닙니다: {expression} -> {value!r}")
        results.append(
            {
                "expression": expression,
                "passed": True,
                "elapsed_ms": round(elapsed_ms, 3),
            }
        )
    return results


def run_self_test(
    module: ModuleType,
    strict: bool,
    present: bool,
    assert_count: int,
    output: OutputCollector,
) -> dict[str, object]:
    if not present:
        if strict:
            raise ProofFailure(
                "--strict 증명을 위해 문제 파일에 self_test()와 assert 두 개 이상을 추가하세요."
            )
        return {"present": False, "assert_count": 0, "passed": None, "elapsed_ms": 0.0}
    if strict and assert_count < 2:
        raise ProofFailure(
            f"--strict 증명에는 self_test() 안의 assert가 두 개 이상 필요합니다. 현재 {assert_count}개입니다."
        )

    test_function = getattr(module, "self_test", None)
    if not callable(test_function):
        raise ProofFailure("self_test 이름이 있지만 호출 가능한 함수가 아닙니다.")
    started = perf_counter()
    try:
        with output.capture("self_test"):
            result = test_function()
    except Exception as error:
        raise ProofFailure(f"self_test 실패: {type(error).__name__}: {error}") from error
    elapsed_ms = (perf_counter() - started) * 1000
    if result not in (None, True):
        raise ProofFailure(f"self_test()는 None 또는 True를 반환해야 합니다: {result!r}")
    return {
        "present": True,
        "assert_count": assert_count,
        "passed": True,
        "elapsed_ms": round(elapsed_ms, 3),
    }


def source_digest(source: str) -> str:
    return sha256(source.encode("utf-8")).hexdigest()


def receipt_path(problem_id: str) -> Path:
    return PROOF_ROOT / f"{problem_id}.json"


def write_receipt(receipt: dict[str, object]) -> Path:
    PROOF_ROOT.mkdir(parents=True, exist_ok=True)
    problem_id = str(receipt["problem_id"])
    destination = receipt_path(problem_id)
    temporary = destination.with_suffix(".json.tmp")
    payload = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temporary.write_text(payload, encoding="utf-8")
    temporary.replace(destination)
    with (PROOF_ROOT / "history.jsonl").open("a", encoding="utf-8") as history:
        history.write(json.dumps(receipt, ensure_ascii=False, sort_keys=True) + "\n")
    return destination


def verify_receipt(problem_id: str, source: str) -> None:
    path = receipt_path(problem_id)
    if not path.exists():
        raise ProofFailure(f"증명 영수증이 없습니다: {path.relative_to(ROOT)}")
    receipt = json.loads(path.read_text(encoding="utf-8"))
    expected = receipt.get("source_sha256")
    actual = source_digest(source)
    if expected != actual:
        raise ProofFailure(
            "현재 소스와 마지막 증명 영수증의 SHA-256이 다릅니다. 코드를 수정했다면 다시 실행하세요."
        )
    if receipt.get("status") != "PASS":
        raise ProofFailure("마지막 영수증이 PASS 상태가 아닙니다.")
    print(f"VERIFIED {problem_id}")
    print(f"receipt={path.relative_to(ROOT)}")
    print(f"source_sha256={actual}")


def prove(problem_id: str, strict: bool, no_receipt: bool) -> None:
    path = find_problem(problem_id)
    source, tree = parse_source(path)
    unfinished = unfinished_lines(tree)
    if unfinished:
        lines = ", ".join(str(line) for line in unfinished)
        raise ProofFailure(f"미완성 NotImplementedError가 남아 있습니다. 줄: {lines}")

    examples = extract_examples(tree)
    source_checks = extract_source_checks(tree)
    function_name = primary_function_name(tree) if source_checks else ""
    present, assert_count = self_test_metadata(tree)
    output = OutputCollector()
    try:
        module = load_module(path, problem_id, output)
        started = perf_counter()
        example_results = run_examples(module, examples, path, output)
        self_test_result = run_self_test(
            module,
            strict,
            present,
            assert_count,
            output,
        )
        failed_checks = (
            failed_source_checks(source, function_name, source_checks)
            if source_checks
            else []
        )
        if failed_checks:
            details = "\n".join(
                f"- {name}: {CHECK_DESCRIPTIONS[name]}" for name in failed_checks
            )
            raise ProofFailure(f"필수 구현 방식이 충족되지 않았습니다.\n{details}")
    except ProofFailure as error:
        error.output_records = list(output.records)
        raise
    total_ms = (perf_counter() - started) * 1000
    now = datetime.now(UTC)
    proof_level = "STRICT_SELF_TEST" if strict else "PUBLIC_EXAMPLES"
    if present and not strict:
        proof_level = "PUBLIC_EXAMPLES_AND_SELF_TEST"
    receipt: dict[str, object] = {
        "schema_version": 1,
        "problem_id": problem_id,
        "problem_path": path.relative_to(ROOT).as_posix(),
        "source_sha256": source_digest(source),
        "verified_at_utc": now.isoformat().replace("+00:00", "Z"),
        "python_version": platform.python_version(),
        "proof_level": proof_level,
        "strict": strict,
        "public_examples": example_results,
        "self_test": self_test_result,
        "source_checks": {
            "required": list(source_checks),
            "passed": True,
        },
        "execution_output": [asdict(record) for record in output.records],
        "total_elapsed_ms": round(total_ms, 3),
        "status": "PASS",
    }

    written: Path | None = None
    if not no_receipt:
        written = write_receipt(receipt)

    print(f"PASS {problem_id}", flush=True)
    print_output_records(output.records)
    print(f"file={path.relative_to(ROOT)}")
    print(f"proof_level={proof_level}")
    print(f"source_sha256={receipt['source_sha256']}")
    print(f"public_examples={len(example_results)}")
    print(f"self_test_asserts={assert_count}")
    print(f"source_checks={len(source_checks)}")
    print(f"elapsed_ms={receipt['total_elapsed_ms']}")
    if written is not None:
        print(f"receipt={written.relative_to(ROOT)}")
    if not present:
        print("warning=self_test()가 없어 공개 예시만 증명했습니다. 강한 증명은 --strict를 사용하세요.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PB/CI 문제 구현을 실행하고 SHA-256 증명 영수증을 생성합니다."
    )
    parser.add_argument("problem_id", help="PB0001 또는 CI0001 형식")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="self_test()와 assert 두 개 이상을 요구합니다.",
    )
    parser.add_argument(
        "--verify-receipt",
        action="store_true",
        help="코드를 실행하지 않고 마지막 영수증과 현재 소스 해시를 비교합니다.",
    )
    parser.add_argument(
        "--no-receipt",
        action="store_true",
        help="테스트만 실행하고 증명 영수증은 쓰지 않습니다.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    problem_id = args.problem_id.upper()
    try:
        path = find_problem(problem_id)
        source, _ = parse_source(path)
        if args.verify_receipt:
            verify_receipt(problem_id, source)
        else:
            prove(problem_id, strict=args.strict, no_receipt=args.no_receipt)
    except ProofFailure as error:
        print(f"FAIL {problem_id}", flush=True)
        print_output_records(error.output_records)
        print(error, flush=True)
        raise SystemExit(1) from error


if __name__ == "__main__":
    main()
