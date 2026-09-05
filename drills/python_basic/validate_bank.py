from __future__ import annotations

import argparse
import ast
import builtins
from pathlib import Path
import re

from generate_bank import SEEDS
from regenerate_problems import build_catalog, render_docstring, render_self_test
from source_checks import CHECK_DESCRIPTIONS, checks_for_seed


ROOT = Path(__file__).resolve().parent
PROBLEM_PATTERN = re.compile(r"PB(\d{4})_.*\.py")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="820개 문제 계약과 현재 사용자 코드 상태를 검사합니다."
    )
    parser.add_argument(
        "--strict-user-code",
        action="store_true",
        help="사용자가 편집 중인 파일의 Python 문법 오류도 전체 검증 실패로 처리합니다.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    builds = build_catalog()
    problems = [ROOT / build.relative_path for build in builds]
    missing = [str(path.relative_to(ROOT)) for path in problems if not path.is_file()]
    if missing:
        raise SystemExit(f"missing managed problems: {missing}")
    extras = sorted(
        path for path in ROOT.rglob("PB*.py")
        if path.is_file() and path not in set(problems)
        and "_preserved_answers" not in path.parts
    )

    ids: list[int] = []
    failures: list[str] = []
    function_names: list[str] = []
    problem_statements: list[str] = []
    test_suites: list[tuple[str, ...]] = []
    total_asserts = 0
    total_documented_examples = 0
    source_checked_problems = 0
    user_syntax_errors: list[str] = []
    for path in problems:
        match = PROBLEM_PATTERN.fullmatch(path.name)
        if match is None:
            failures.append(f"invalid filename: {path.relative_to(ROOT)}")
            continue
        ids.append(int(match.group(1)))
        numeric_id = int(match.group(1))
        build = builds[numeric_id - 1]
        source = path.read_text(encoding="utf-8")
        expected_path = ROOT / build.relative_path
        if path != expected_path:
            failures.append(
                f"unexpected path for PB{numeric_id:04d}: "
                f"{path.relative_to(ROOT)}; expected={build.relative_path}"
            )
        if not source.startswith(render_docstring(build) + "\n"):
            failures.append(f"generated problem contract differs: {path.relative_to(ROOT)}")
        if not source.rstrip().endswith(render_self_test(build)):
            failures.append(f"generated self_test differs: {path.relative_to(ROOT)}")
        try:
            module = ast.parse(source, filename=str(path))
        except SyntaxError as error:
            user_syntax_errors.append(f"PB{numeric_id:04d}")
            module = ast.parse(build.starter_source, filename=str(path))

        docstring = ast.get_docstring(module) or ""
        documented_assertions: tuple[str, ...] = ()
        examples_match = re.search(
            r"예시 및 필수 테스트\n-+\n(?P<body>.*?)\n\n완료 조건",
            docstring,
            re.DOTALL,
        )
        if examples_match is None:
            failures.append(f"missing documented examples: {path.relative_to(ROOT)}")
        else:
            example_expressions = [
                line.removeprefix("- ").strip()
                for line in examples_match.group("body").splitlines()
                if line.startswith("- ")
            ]
            if len(example_expressions) != 3:
                failures.append(
                    f"expected 3 documented examples, found {len(example_expressions)}: "
                    f"{path.relative_to(ROOT)}"
                )
            parsed_examples: list[str] = []
            for expression in example_expressions:
                try:
                    parsed = ast.parse(expression, mode="eval")
                except SyntaxError as error:
                    failures.append(
                        f"invalid documented example {expression!r}: "
                        f"{path.relative_to(ROOT)}: {error}"
                    )
                else:
                    parsed_examples.append(ast.dump(parsed.body, include_attributes=False))
            documented_assertions = tuple(parsed_examples)
            total_documented_examples += len(example_expressions)

        hinted_signature: tuple[str, str] | None = None
        signature_match = re.search(
            r"구현할 함수\n-+\n(?P<signature>def [^\n]+:)",
            docstring,
        )
        if signature_match is None:
            failures.append(f"missing hinted signature: {path.relative_to(ROOT)}")
        else:
            try:
                hinted_node = ast.parse(
                    f"{signature_match.group('signature')}\n    pass"
                ).body[0]
            except SyntaxError as error:
                failures.append(
                    f"invalid hinted signature: {path.relative_to(ROOT)}: {error}"
                )
            else:
                if isinstance(hinted_node, ast.FunctionDef):
                    hinted_signature = (
                        ast.dump(hinted_node.args, include_attributes=False),
                        ast.dump(hinted_node.returns, include_attributes=False),
                    )
        statement_match = re.search(
            r"문제\n-+\n(?P<body>.*?)\n\n구현할 함수",
            docstring,
            re.DOTALL,
        )
        if statement_match is None:
            failures.append(f"missing concrete problem statement: {path.relative_to(ROOT)}")
        else:
            problem_statements.append(statement_match.group("body").strip())
        for required in (
            "Chapter:",
            "Topic:",
            "Seed:",
            "Variant:",
            "Time cap:",
            "Source checks:",
            "문제",
            "연습 초점",
            "구현할 함수",
            "예시 및 필수 테스트",
            "완료 조건",
        ):
            if required not in docstring:
                failures.append(f"missing {required!r}: {path.relative_to(ROOT)}")
        source_check_match = re.search(
            r"^Source checks:[ \t]*(?P<checks>.*)$",
            docstring,
            re.MULTILINE,
        )
        documented_checks = (
            tuple(
                part.strip()
                for part in source_check_match.group("checks").split(",")
                if part.strip()
            )
            if source_check_match is not None
            else ()
        )
        seed = SEEDS[(numeric_id - 1) // 10]
        expected_checks = checks_for_seed(seed.slug)
        if documented_checks != expected_checks:
            failures.append(
                f"source checks differ from seed policy: {path.relative_to(ROOT)}; "
                f"expected={expected_checks}, documented={documented_checks}"
            )
        unknown_checks = set(documented_checks) - CHECK_DESCRIPTIONS.keys()
        if unknown_checks:
            failures.append(
                f"unknown source checks {sorted(unknown_checks)}: {path.relative_to(ROOT)}"
            )
        if documented_checks:
            source_checked_problems += 1
        if "# DIRECT_PROOF_RUNNER" in source:
            failures.append(f"embedded proof runner must be removed: {path.relative_to(ROOT)}")
        self_tests = [
            node
            for node in module.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and node.name == "self_test"
        ]
        if len(self_tests) != 1:
            failures.append(f"expected one self_test: {path.relative_to(ROOT)}")
        else:
            assert_count = sum(
                isinstance(node, ast.Assert)
                for node in ast.walk(self_tests[0])
            )
            if assert_count != 3:
                failures.append(
                    f"expected exactly 3 asserts, found {assert_count}: {path.relative_to(ROOT)}"
                )
            total_asserts += assert_count
            assertions = [
                ast.dump(node.test, include_attributes=False)
                for node in ast.walk(self_tests[0])
                if isinstance(node, ast.Assert)
            ]
            if len(set(assertions)) != 3:
                failures.append(f"dedicated asserts are duplicated: {path.relative_to(ROOT)}")
            if documented_assertions != tuple(assertions):
                failures.append(
                    f"documented examples differ from self_test: {path.relative_to(ROOT)}"
                )
            test_suites.append(tuple(assertions))
            primary_functions = [
                node
                for node in module.body
                if isinstance(node, ast.FunctionDef) and node.name != "self_test"
            ]
            if len(primary_functions) != 1:
                failures.append(f"expected one hinted function: {path.relative_to(ROOT)}")
            else:
                primary_name = primary_functions[0].name
                function_names.append(primary_name)
                actual_signature = (
                    ast.dump(primary_functions[0].args, include_attributes=False),
                    ast.dump(primary_functions[0].returns, include_attributes=False),
                )
                if hinted_signature != actual_signature:
                    failures.append(
                        f"hinted signature differs from implementation stub: "
                        f"{path.relative_to(ROOT)}"
                    )
                defined_names = {primary_name, "self_test"}
                called_names = {
                    node.func.id
                    for node in ast.walk(self_tests[0])
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                }
                unknown_calls = called_names - defined_names - set(dir(builtins))
                if unknown_calls:
                    failures.append(
                        f"undefined test calls {sorted(unknown_calls)}: {path.relative_to(ROOT)}"
                    )

    if ids != list(range(1, 821)):
        failures.append("problem IDs are not exactly PB0001..PB0820")
    if len(set(function_names)) != 820:
        failures.append(f"expected 820 unique function names, found {len(set(function_names))}")
    if len(set(problem_statements)) != 820:
        failures.append(
            f"expected 820 unique problem statements, found {len(set(problem_statements))}"
        )
    if len(set(test_suites)) != 820:
        failures.append(f"expected 820 unique test suites, found {len(set(test_suites))}")

    index_path = ROOT / "INDEX.md"
    index_links = re.findall(
        r"^- \[(PB\d{4})[^\]]*\]\(([^)]+)\)$",
        index_path.read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    if len(index_links) != 820:
        failures.append(f"expected 820 INDEX links, found {len(index_links)}")
    if [problem_id for problem_id, _ in index_links] != [f"PB{number:04d}" for number in range(1, 821)]:
        failures.append("INDEX IDs are not exactly PB0001..PB0820")
    missing_links = [relative for _, relative in index_links if not (ROOT / relative).is_file()]
    if missing_links:
        failures.append(f"INDEX contains missing files: {missing_links[:3]}")

    chapter_counts = {
        directory.name: len(list(directory.glob("PB*.py")))
        for directory in sorted(ROOT.iterdir())
        if directory.is_dir() and re.match(r"\d{2}_", directory.name)
    }
    if len(chapter_counts) != 12:
        failures.append(f"expected 12 chapter directories, found {len(chapter_counts)}")
    if args.strict_user_code and user_syntax_errors:
        failures.append(
            "user code syntax errors: " + ", ".join(user_syntax_errors)
        )

    if failures:
        raise SystemExit("\n".join(failures))

    print("problems=820")
    print(f"unmanaged_drafts_preserved={len(extras)}")
    print("ids=PB0001..PB0820")
    print("chapters=12")
    print("unique_function_names=820")
    print("unique_problem_statements=820")
    print("unique_test_suites=820")
    print(f"asserts={total_asserts}")
    print(f"documented_examples={total_documented_examples}")
    print("index_links=820")
    print(f"source_checked_problems={source_checked_problems}")
    print(f"user_syntax_errors={len(user_syntax_errors)}")
    if user_syntax_errors:
        print(f"unfinished_user_files={','.join(user_syntax_errors)}")
    for chapter, count in chapter_counts.items():
        managed_count = sum(path.parent.name == chapter for path in problems)
        print(f"{chapter}={managed_count}")


if __name__ == "__main__":
    main()
