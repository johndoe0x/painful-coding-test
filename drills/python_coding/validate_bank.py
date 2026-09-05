from __future__ import annotations

import argparse
import ast
import builtins
from collections import Counter
import inspect
from pathlib import Path
import re
import sys


WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from python_basic.source_checks import CHECK_DESCRIPTIONS
from quality_regenerate import (
    ROOT,
    build_catalog,
    function_name,
    normalized_test_suite,
    render_docstring,
    render_self_test,
)


PROBLEM_PATTERN = re.compile(r"CI(\d{4})_.*\.py")
REQUIRED_LIBRARY_CHECKS = (
    "counter_call",
    "defaultdict_call",
    "deque_call",
    "heapq_call",
    "bisect_call",
    "itertools_call",
    "cache_decorator",
    "lru_cache_decorator",
    "cmp_to_key_call",
    "math_call",
    "itemgetter_call",
    "re_call",
    "pathlib_call",
    "json_call",
    "csv_call",
    "iter_call",
    "next_call",
    "yield",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Python Coding 800의 계약·테스트·표준 라이브러리 커버리지를 검사합니다."
    )
    parser.add_argument(
        "--strict-user-code",
        action="store_true",
        help="사용자가 편집 중인 파일의 Python 문법 오류도 실패로 처리합니다.",
    )
    return parser.parse_args()


def signature_shape(function: ast.FunctionDef) -> tuple[str, str]:
    return (
        ast.dump(function.args, include_attributes=False),
        ast.dump(function.returns, include_attributes=False),
    )


def argument_binding_errors(function: ast.FunctionDef, tree: ast.AST) -> list[str]:
    """Bind public call shapes without importing or executing a learner solution."""
    arguments = function.args
    positional = [*arguments.posonlyargs, *arguments.args]
    required_count = len(positional) - len(arguments.defaults)
    parameters = [
        inspect.Parameter(
            argument.arg,
            inspect.Parameter.POSITIONAL_ONLY
            if index < len(arguments.posonlyargs)
            else inspect.Parameter.POSITIONAL_OR_KEYWORD,
            default=inspect.Parameter.empty if index < required_count else None,
        )
        for index, argument in enumerate(positional)
    ]
    if arguments.vararg:
        parameters.append(inspect.Parameter(arguments.vararg.arg, inspect.Parameter.VAR_POSITIONAL))
    parameters.extend(
        inspect.Parameter(
            argument.arg,
            inspect.Parameter.KEYWORD_ONLY,
            default=inspect.Parameter.empty if default is None else None,
        )
        for argument, default in zip(arguments.kwonlyargs, arguments.kw_defaults)
    )
    if arguments.kwarg:
        parameters.append(inspect.Parameter(arguments.kwarg.arg, inspect.Parameter.VAR_KEYWORD))
    signature = inspect.Signature(parameters)
    failures = []
    for call in ast.walk(tree):
        if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                and call.func.id == function.name):
            continue
        if any(isinstance(value, ast.Starred) for value in call.args) or any(
            keyword.arg is None for keyword in call.keywords
        ):
            failures.append(f"cannot statically bind unpacked example: {ast.unparse(call)}")
            continue
        try:
            signature.bind(*[None for _ in call.args], **{key.arg: None for key in call.keywords})
        except TypeError as error:
            failures.append(f"{ast.unparse(call)}: {error}")
    return failures


def main() -> None:
    args = parse_args()
    builds = build_catalog()
    problems = sorted(
        path
        for path in ROOT.rglob("CI*.py")
        if path.is_file() and "_preserved_answers" not in path.parts
    )
    failures: list[str] = []
    if len(problems) != 800:
        failures.append(f"expected 800 problems, found {len(problems)}")

    ids: list[int] = []
    function_names: list[str] = []
    problem_statements: list[str] = []
    test_suites: list[tuple[str, ...]] = []
    total_asserts = 0
    documented_examples = 0
    user_syntax_errors: list[str] = []
    source_check_counts = {name: 0 for name in CHECK_DESCRIPTIONS}

    for path in problems:
        match = PROBLEM_PATTERN.fullmatch(path.name)
        if match is None:
            failures.append(f"invalid filename: {path.relative_to(ROOT)}")
            continue
        number = int(match.group(1))
        ids.append(number)
        if not 1 <= number <= len(builds):
            failures.append(f"out-of-range ID: {path.relative_to(ROOT)}")
            continue
        build = builds[number - 1]
        source = path.read_text(encoding="utf-8")
        expected_path = ROOT / build.relative_path
        if path != expected_path:
            failures.append(
                f"unexpected path for CI{number:04d}: {path.relative_to(ROOT)}; "
                f"expected={build.relative_path}"
            )
        if not source.startswith(render_docstring(build) + "\n"):
            failures.append(f"generated contract differs: {path.relative_to(ROOT)}")
        if not source.rstrip().endswith(render_self_test(build)):
            failures.append(f"generated self_test differs: {path.relative_to(ROOT)}")

        try:
            module = ast.parse(source, filename=str(path))
        except SyntaxError:
            user_syntax_errors.append(build.problem_id)
            module = ast.parse(build.starter_source, filename=str(path))

        docstring = ast.get_docstring(module) or ""
        for required in (
            "Chapter:",
            "Seed:",
            "Variant:",
            "Time cap:",
            "Source checks:",
            "문제",
            "연습 초점",
            "구현할 함수",
            "예시 및 필수 테스트",
            "완료 조건",
            "시간·공간복잡도",
        ):
            if required not in docstring:
                failures.append(f"missing {required!r}: {path.relative_to(ROOT)}")

        statement = re.search(
            r"문제\n-+\n(?P<body>.*?)\n\n연습 초점",
            docstring,
            re.DOTALL,
        )
        if statement is None:
            failures.append(f"missing problem statement: {path.relative_to(ROOT)}")
        else:
            problem_statements.append(statement.group("body").strip())

        examples = re.search(
            r"예시 및 필수 테스트\n-+\n(?P<body>.*?)\n\n완료 조건",
            docstring,
            re.DOTALL,
        )
        parsed_examples: list[str] = []
        if examples is None:
            failures.append(f"missing examples: {path.relative_to(ROOT)}")
        else:
            expressions = [
                line.removeprefix("- ").strip()
                for line in examples.group("body").splitlines()
                if line.startswith("- ")
            ]
            if len(expressions) != 3:
                failures.append(
                    f"expected 3 examples, found {len(expressions)}: "
                    f"{path.relative_to(ROOT)}"
                )
            for expression in expressions:
                try:
                    parsed = ast.parse(expression, mode="eval")
                except SyntaxError as error:
                    failures.append(
                        f"invalid example {expression!r}: {path.relative_to(ROOT)}: {error}"
                    )
                else:
                    parsed_examples.append(
                        ast.dump(parsed.body, include_attributes=False)
                    )
            documented_examples += len(expressions)

        hinted = re.search(r"구현할 함수\n-+\n(?P<signature>def [^\n]+:)", docstring)
        hinted_shape: tuple[str, str] | None = None
        if hinted is None:
            failures.append(f"missing signature hint: {path.relative_to(ROOT)}")
        else:
            hinted_module = ast.parse(f"{hinted.group('signature')}\n    pass")
            hinted_function = hinted_module.body[0]
            assert isinstance(hinted_function, ast.FunctionDef)
            hinted_shape = signature_shape(hinted_function)

        check_match = re.search(
            r"^Source checks:[ \t]*(?P<checks>.*)$",
            docstring,
            re.MULTILINE,
        )
        documented_checks = (
            tuple(
                part.strip()
                for part in check_match.group("checks").split(",")
                if part.strip()
            )
            if check_match
            else ()
        )
        if documented_checks != build.exercise.source_checks:
            failures.append(
                f"source checks differ: {path.relative_to(ROOT)}; "
                f"expected={build.exercise.source_checks}, actual={documented_checks}"
            )
        unknown_checks = set(documented_checks) - CHECK_DESCRIPTIONS.keys()
        if unknown_checks:
            failures.append(
                f"unknown source checks {sorted(unknown_checks)}: {path.relative_to(ROOT)}"
            )
        for check in documented_checks:
            source_check_counts[check] += 1

        primary = [
            node
            for node in module.body
            if isinstance(node, ast.FunctionDef) and node.name != "self_test"
        ]
        if len(primary) != 1:
            failures.append(
                f"expected one primary function, found {len(primary)}: "
                f"{path.relative_to(ROOT)}"
            )
        else:
            function_names.append(primary[0].name)
            if primary[0].name != function_name(build.exercise.signature):
                failures.append(f"wrong function name: {path.relative_to(ROOT)}")
            if hinted_shape != signature_shape(primary[0]):
                failures.append(f"hinted signature differs: {path.relative_to(ROOT)}")

        self_tests = [
            node
            for node in module.body
            if isinstance(node, ast.FunctionDef) and node.name == "self_test"
        ]
        if len(self_tests) != 1:
            failures.append(f"expected one self_test: {path.relative_to(ROOT)}")
        else:
            assertions = [
                node for node in ast.walk(self_tests[0]) if isinstance(node, ast.Assert)
            ]
            if len(assertions) != 3:
                failures.append(
                    f"expected 3 asserts, found {len(assertions)}: {path.relative_to(ROOT)}"
                )
            assertion_shapes = tuple(
                ast.dump(node.test, include_attributes=False) for node in assertions
            )
            total_asserts += len(assertions)
            test_suites.append(assertion_shapes)
            if tuple(parsed_examples) != assertion_shapes:
                failures.append(
                    f"documented examples differ from self_test: {path.relative_to(ROOT)}"
                )
            primary_name = function_name(build.exercise.signature)
            contract_function = ast.parse(build.exercise.signature + "\n    pass").body[0]
            assert isinstance(contract_function, ast.FunctionDef)
            for binding_error in argument_binding_errors(contract_function, self_tests[0]):
                failures.append(f"invalid public call: {path.relative_to(ROOT)}: {binding_error}")
            defined = {primary_name, "self_test"}
            calls = {
                node.func.id
                for node in ast.walk(self_tests[0])
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            }
            unknown_calls = calls - defined - set(dir(builtins))
            if unknown_calls:
                failures.append(
                    f"undefined test calls {sorted(unknown_calls)}: {path.relative_to(ROOT)}"
                )

        if "DIRECT_PROOF_RUNNER" in source or "def _run_proof" in source:
            failures.append(f"embedded runner found: {path.relative_to(ROOT)}")

    if ids != list(range(1, 801)):
        failures.append("problem IDs are not exactly CI0001..CI0800")
    if len(set(function_names)) != 800:
        failures.append(
            f"expected 800 unique function names, found {len(set(function_names))}"
        )
    if len(set(problem_statements)) != 800:
        failures.append(
            f"expected 800 unique problem statements, found {len(set(problem_statements))}"
        )
    if len(set(test_suites)) != 800:
        failures.append(
            f"expected 800 unique test suites, found {len(set(test_suites))}"
        )

    index_links = re.findall(
        r"^- \[(CI\d{4})[^\]]*\]\(([^)]+)\)$",
        (ROOT / "INDEX.md").read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    if len(index_links) != 800:
        failures.append(f"expected 800 INDEX links, found {len(index_links)}")
    if [problem_id for problem_id, _ in index_links] != [
        f"CI{number:04d}" for number in range(1, 801)
    ]:
        failures.append("INDEX IDs are not CI0001..CI0800")
    missing_links = [relative for _, relative in index_links if not (ROOT / relative).is_file()]
    if missing_links:
        failures.append(f"INDEX contains missing files: {missing_links[:3]}")

    chapter_counts = {
        directory.name: len(list(directory.glob("CI*.py")))
        for directory in sorted(ROOT.iterdir())
        if directory.is_dir() and re.match(r"\d{2}_", directory.name)
    }
    if len(chapter_counts) != 8:
        failures.append(f"expected 8 chapters, found {len(chapter_counts)}")
    for check in REQUIRED_LIBRARY_CHECKS:
        if source_check_counts[check] == 0:
            failures.append(f"required library/tool coverage is zero: {check}")
    if args.strict_user_code and user_syntax_errors:
        failures.append("user syntax errors: " + ", ".join(user_syntax_errors))

    if failures:
        raise SystemExit("\n".join(failures))

    normalized_counts = Counter(
        normalized_test_suite(function_name(build.exercise.signature), build.exercise.tests)
        for build in builds
    )
    source_checked_problems = sum(bool(build.exercise.source_checks) for build in builds)
    print("problems=800")
    print("ids=CI0001..CI0800")
    print("chapters=8")
    print("unique_function_names=800")
    print("unique_problem_statements=800")
    print("unique_test_suites=800")
    print(f"normalized_test_suites={len(normalized_counts)}")
    print(f"repeated_test_suite_slots={len(builds) - len(normalized_counts)}")
    print("diversity_metric=exact AST after target-name normalization; not unique algorithms")
    print("source_checks_scope=instructional syntax/API evidence; not complexity or correctness proof")
    print(f"asserts={total_asserts}")
    print(f"documented_examples={documented_examples}")
    print(f"source_checked_problems={source_checked_problems}")
    print(f"user_syntax_errors={len(user_syntax_errors)}")
    for check in REQUIRED_LIBRARY_CHECKS:
        print(f"coverage_{check}={source_check_counts[check]}")
    for chapter, count in chapter_counts.items():
        print(f"{chapter}={count}")


if __name__ == "__main__":
    main()
