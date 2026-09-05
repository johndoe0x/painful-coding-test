"""Reproducible, read-only-by-default audit of every manifest-managed drill.

No learner code is executed. Name-normalized tests measure repeated test
contracts, not the number of distinct algorithms or the correctness of answers.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter, defaultdict
from hashlib import sha256
import inspect
import json
from pathlib import Path
import re

from bank_inventory import BANKS, managed_paths


ROOT = Path(__file__).resolve().parent


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


class NormalizeFunction(ast.NodeTransformer):
    def __init__(self, name: str):
        self.name = name

    def visit_Name(self, node: ast.Name) -> ast.AST:
        if node.id == self.name:
            return ast.copy_location(ast.Name(id="__target__", ctx=node.ctx), node)
        return node


def signature_for(definition: ast.FunctionDef) -> inspect.Signature:
    arguments = definition.args
    positional = arguments.posonlyargs + arguments.args
    required = len(positional) - len(arguments.defaults)
    params = []
    for index, arg in enumerate(positional):
        kind = (inspect.Parameter.POSITIONAL_ONLY if index < len(arguments.posonlyargs)
                else inspect.Parameter.POSITIONAL_OR_KEYWORD)
        default = inspect.Parameter.empty if index < required else None
        params.append(inspect.Parameter(arg.arg, kind, default=default))
    if arguments.vararg:
        params.append(inspect.Parameter(arguments.vararg.arg, inspect.Parameter.VAR_POSITIONAL))
    for arg, default_node in zip(arguments.kwonlyargs, arguments.kw_defaults):
        default = inspect.Parameter.empty if default_node is None else None
        params.append(inspect.Parameter(arg.arg, inspect.Parameter.KEYWORD_ONLY, default=default))
    if arguments.kwarg:
        params.append(inspect.Parameter(arguments.kwarg.arg, inspect.Parameter.VAR_KEYWORD))
    return inspect.Signature(params)


def call_errors(definition: ast.FunctionDef, examples: list[str]) -> list[str]:
    errors = []
    signature = signature_for(definition)
    for index, expression in enumerate(examples, 1):
        for call in ast.walk(ast.parse(expression, mode="eval")):
            if not isinstance(call, ast.Call) or not isinstance(call.func, ast.Name):
                continue
            if call.func.id != definition.name:
                continue
            if any(isinstance(arg, ast.Starred) for arg in call.args) or any(
                keyword.arg is None for keyword in call.keywords
            ):
                continue  # Dynamic unpacking is not claimed to have been checked.
            try:
                signature.bind(*([None] * len(call.args)), **{
                    keyword.arg: None for keyword in call.keywords
                })
            except TypeError as error:
                errors.append(f"example {index}: {error}")
    return errors


def inspect_problem(problem_id: str, path: Path) -> dict:
    source = path.read_text(encoding="utf-8")
    syntax_error = None
    try:
        tree = ast.parse(source)
        doc = ast.get_docstring(tree) or ""
    except SyntaxError as error:
        syntax_error = f"line {error.lineno}: {error.msg}"
        # Inspect the unchanged statement without executing or fixing a learner draft.
        end = source.find('"""', 3)
        doc = ast.literal_eval(source[:end + 3])
    signature = re.search(r"구현할 함수\n-+\n(def [^\n]+:)", doc).group(1)
    definition = ast.parse(signature + "\n    pass").body[0]
    examples_section = re.search(
        r"예시 및 필수 테스트\n-+\n(.*?)\n\n완료 조건", doc, re.S
    ).group(1)
    examples = [line[2:] for line in examples_section.splitlines() if line.startswith("- ")]
    normalized = [ast.dump(NormalizeFunction(definition.name).visit(
        ast.parse(expression, mode="eval")), include_attributes=False) for expression in examples]
    task = re.search(r"문제\n-+\n(.*?)\n\n연습 초점", doc, re.S).group(1).strip()
    task = re.sub(r" 이 파일은 .*? 챕터의 반복 세트 \d+이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다\.$", "", task)
    check_match = re.search(r"^Source checks:[ \t]*(.*)$", doc, re.M)
    checks = sorted(filter(None, (part.strip() for part in
                    (check_match.group(1) if check_match else "").split(","))))
    suite = sha256(json.dumps(normalized, ensure_ascii=False).encode()).hexdigest()
    # Keep pedagogically different required implementations as separate exercises.
    learning = sha256(json.dumps([normalized, checks, task], ensure_ascii=False).encode()).hexdigest()
    raw_tests = sha256(json.dumps(examples, ensure_ascii=False).encode()).hexdigest()
    title = doc.splitlines()[0].split("—", 1)[-1].strip()
    time_cap = int(re.search(r"Time cap: (\d+)", doc).group(1))
    return {
        "id": problem_id, "path": str(path.relative_to(ROOT)), "title": title,
        "chapter": path.parent.name, "function": definition.name,
        "public_asserts": len(examples), "source_checks": checks, "time_cap": time_cap,
        "test_sha256": raw_tests, "normalized_test_sha256": suite,
        "learning_group_sha256": learning, "call_errors": call_errors(definition, examples),
        "user_syntax_error": syntax_error,
        "verification": "structural_all; semantic_review_by_family; not_all_reference_solved",
    }


def collect() -> dict:
    banks = {}
    for prefix, (bank_name, _) in BANKS.items():
        paths = managed_paths(ROOT, prefix)
        rows = [inspect_problem(problem_id, path) for problem_id, path in sorted(paths.items())]
        groups = defaultdict(list)
        for row in rows:
            groups[row["learning_group_sha256"]].append(row["id"])
        for row in rows:
            row["review_of"] = groups[row["learning_group_sha256"]][0]
            row["study_role"] = "automation_drill"
        extras = sorted(str(path.relative_to(ROOT)) for path in (ROOT / bank_name).rglob(prefix + "*.py")
                        if "_preserved_answers" not in path.parts and path not in paths.values())
        banks[prefix] = {
            "count": len(rows), "public_asserts": sum(row["public_asserts"] for row in rows),
            "unique_function_names": len({row["function"] for row in rows}),
            "raw_test_suites": len({row["test_sha256"] for row in rows}),
            "normalized_test_suites": len({row["normalized_test_sha256"] for row in rows}),
            "learning_groups": len(groups),
            "repeated_test_entries": len(rows) - len({row["normalized_test_sha256"] for row in rows}),
            "repeated_learning_entries": len(rows) - len(groups),
            "optional_recall_entries": 0,
            "call_error_problems": [row["id"] for row in rows if row["call_errors"]],
            "syntax_error_problems": [row["id"] for row in rows if row["user_syntax_error"]],
            "chapter_counts": dict(Counter(row["chapter"] for row in rows)),
            "time_caps": dict(Counter(row["time_cap"] for row in rows)),
            "unmanaged_drafts_preserved": extras,
            "problems": rows,
        }
    return {"schema": 1, "banks": banks}


def protected_snapshot() -> dict:
    hashes = {}
    for prefix, (bank_name, manifest_name) in BANKS.items():
        bank = ROOT / bank_name
        entries = json.loads((bank / manifest_name).read_text())["problems"]
        managed = managed_paths(ROOT, prefix)
        for problem_id, path in managed.items():
            if file_hash(path) != entries[problem_id]["starter_sha256"]:
                hashes[str(path.relative_to(ROOT))] = file_hash(path)
        for path in bank.rglob("*.py"):
            if "_preserved_answers" in path.parts or (
                path.name.startswith(prefix) and path not in managed.values()
            ):
                hashes[str(path.relative_to(ROOT))] = file_hash(path)
    for directory in (ROOT / "proofs", ROOT / ".zed"):
        for path in directory.rglob("*"):
            if path.is_file():
                hashes[str(path.relative_to(ROOT))] = file_hash(path)
    return hashes


def write_study_index(report: dict) -> None:
    lines = ["# 문제은행 학습 경로", "",
             "Python Basic은 문법, Python Coding은 코딩테스트용 Python 도구를 빈 화면에서 빠르게 쓰는 훈련입니다.",
             "알고리즘 패턴·트리·그래프·DP 학습과 C 레벨 인증은 후속 NeetCode 250에서 진행합니다.", "",
             "[Python Coding 목적 교정](docs/reviews/2026-09-05-python-coding-purpose-correction.md)",
             "[Basic 전체 820개](python_basic/INDEX.md) · [Coding 전체 800개](python_coding/INDEX.md)", "",
             "## 연습 방법", "",
             "1. 배운 Python 문법·API를 기준으로 현재 챕터의 문제를 10개씩 풉니다.",
             "2. 빈 화면 구현 → 공개 테스트 → 틀린 연산 기록 → 자료를 닫고 재작성합니다.",
             "3. Coding은 기본 150초, 조합 연습은 최대 300초를 복습 목표로 사용합니다.",
             "4. 최초 통과율 85%, 무작위 cold audit 90%와 문서 검색 없이 도구를 쓰는지를 확인합니다.",
             "5. 숫자나 이름이 같은 반복도 인출 훈련에 사용합니다. 문제 수를 새 알고리즘 수로 해석하지 않습니다.", "",
             "이전의 '핵심 240개 + 선택 560개' 분류는 철회했습니다. 아래는 800개 전체 훈련 경로입니다.",
             "동일한 테스트·계약은 복습 대응 ID만 표시하며, 그 이유만으로 선택 문제로 제외하지 않습니다.", ""]
    rows = report["banks"]["CI"]["problems"]
    chapter = None
    for row in rows:
        if row["chapter"] != chapter:
            chapter = row["chapter"]
            lines.extend([f"## {chapter}", ""])
        repetition = f' — {row["review_of"]}와 같은 계약 복습' if row["review_of"] != row["id"] else ""
        lines.append(f'- [{row["id"]} — {row["title"]}]({row["path"]}){repetition}')
    (ROOT / "STUDY_PATH.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", action="store_true", help="Save initial audit and protected hashes in .tmp")
    parser.add_argument("--write", action="store_true", help="Write complete audit JSON and study path")
    parser.add_argument("--verify-preserved", action="store_true")
    args = parser.parse_args()
    if args.verify_preserved:
        before = json.loads((ROOT / ".tmp/review-protected.json").read_text())
        failures = [relative for relative, digest in before.items()
                    if not (ROOT / relative).is_file() or file_hash(ROOT / relative) != digest]
        if failures:
            raise SystemExit(f"Protected files changed: {failures}")
        print(f"protected_files_byte_identical={len(before)}")
        return
    report = collect()
    if args.baseline:
        scratch = ROOT / ".tmp"
        scratch.mkdir(exist_ok=True)
        for name, payload in (("review-before.json", report), ("review-protected.json", protected_snapshot())):
            target = scratch / name
            if target.exists():
                raise SystemExit(f"Refusing to overwrite existing baseline: {target}")
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.write:
        output = ROOT / "docs/reviews"
        output.mkdir(parents=True, exist_ok=True)
        (output / "2026-09-05-problem-bank.json").write_text(
            json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        write_study_index(report)
    print(json.dumps({key: {k: v for k, v in bank.items() if k != "problems"}
                      for key, bank in report["banks"].items()}, ensure_ascii=False, indent=2))
    if any(bank["call_error_problems"] for bank in report["banks"].values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
