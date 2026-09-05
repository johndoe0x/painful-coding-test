from __future__ import annotations

import ast
import builtins
import importlib
from pathlib import Path
import re
import sys
import textwrap

from ..generate_bank import SEEDS
from ..source_checks import CHECK_DESCRIPTIONS, SOURCE_CHECKS_BY_SEED
from .model import Exercise


MODULE_NAMES = (
    "intro_variables_math",
    "functions_conditionals_loops",
    "strings_lists",
    "collections_io_exceptions",
)


def function_node(signature: str) -> ast.FunctionDef:
    module = ast.parse(f"{signature}\n    pass")
    if len(module.body) != 1 or not isinstance(module.body[0], ast.FunctionDef):
        raise ValueError(f"invalid signature: {signature}")
    return module.body[0]


def validate(module_names: tuple[str, ...], require_complete: bool) -> None:
    failures: list[str] = []
    catalogs: dict[str, list[Exercise]] = {}
    function_names: list[str] = []
    slugs: list[str] = []
    tasks: list[str] = []
    test_suites: list[tuple[str, ...]] = []

    for module_name in module_names:
        module = importlib.import_module(f"{__package__}.{module_name}")
        exercises = getattr(module, "EXERCISES", None)
        if not isinstance(exercises, dict):
            failures.append(f"{module_name}: EXERCISES must be a dict")
            continue
        overlap = catalogs.keys() & exercises.keys()
        if overlap:
            failures.append(f"{module_name}: duplicate seeds {sorted(overlap)}")
        catalogs.update(exercises)

    for seed_slug, exercises in catalogs.items():
        if len(exercises) != 10:
            failures.append(f"{seed_slug}: expected 10 exercises, found {len(exercises)}")
        titles = [exercise.title for exercise in exercises if isinstance(exercise, Exercise)]
        focuses = [exercise.focus for exercise in exercises if isinstance(exercise, Exercise)]
        if len(titles) != len(set(titles)):
            failures.append(f"{seed_slug}: exercise titles must be distinct")
        if len(focuses) != len(set(focuses)):
            failures.append(f"{seed_slug}: practice focuses must be distinct")
        seed_definition = next((seed for seed in SEEDS if seed.slug == seed_slug), None)
        if seed_definition is not None and exercises:
            if exercises[0].signature != seed_definition.signature:
                failures.append(
                    f"{seed_slug}: first exercise must preserve baseline signature "
                    f"{seed_definition.signature!r}"
                )
        if seed_slug == "code_errors" and any(
            exercise.starter_body is None for exercise in exercises
        ):
            failures.append("code_errors: every exercise needs a buggy starter_body")
        if seed_slug == "global_vs_local" and any(
            not exercise.prelude.strip() for exercise in exercises
        ):
            failures.append("global_vs_local: every exercise needs a global prelude")
        for index, exercise in enumerate(exercises, start=1):
            label = f"{seed_slug}[{index}]"
            if not isinstance(exercise, Exercise):
                failures.append(f"{label}: not an Exercise")
                continue
            slugs.append(exercise.slug)
            tasks.append(exercise.task)
            if not exercise.title.strip() or not exercise.task.strip() or not exercise.focus.strip():
                failures.append(f"{label}: title/task/focus must be non-empty")
            if "원래 계약:" in exercise.task or "각 case에" in exercise.task:
                failures.append(f"{label}: generic wrapper wording is not allowed")
            if not 30 <= exercise.time_cap <= 300:
                failures.append(f"{label}: unreasonable time cap {exercise.time_cap}")
            if exercise.prelude:
                try:
                    ast.parse(exercise.prelude)
                except SyntaxError as error:
                    failures.append(f"{label}: invalid prelude: {error}")
            try:
                hinted = function_node(exercise.signature)
            except (SyntaxError, ValueError) as error:
                failures.append(f"{label}: {error}")
                continue
            function_names.append(hinted.name)
            if len(exercise.tests) != 3 or len(set(exercise.tests)) != 3:
                failures.append(f"{label}: expected 3 distinct tests")
            parsed_tests: list[str] = []
            for test in exercise.tests:
                try:
                    expression = ast.parse(test, mode="eval").body
                except SyntaxError as error:
                    failures.append(f"{label}: invalid test {test!r}: {error}")
                    continue
                parsed_tests.append(ast.dump(expression, include_attributes=False))
                calls = {
                    node.func.id
                    for node in ast.walk(expression)
                    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                }
                if hinted.name not in calls:
                    failures.append(f"{label}: test does not call {hinted.name}: {test}")
                unknown = calls - {hinted.name} - set(dir(builtins))
                if unknown:
                    failures.append(f"{label}: undefined test calls {sorted(unknown)}")
            test_suites.append(tuple(parsed_tests))
            if exercise.starter_body is not None:
                starter_source = "\n\n".join(
                    part
                    for part in (
                        exercise.prelude.strip(),
                        f"{exercise.signature}\n"
                        f"{textwrap.indent(exercise.starter_body.strip(), '    ')}",
                    )
                    if part
                )
                try:
                    ast.parse(starter_source)
                except SyntaxError as error:
                    failures.append(f"{label}: invalid starter_body: {error}")
                else:
                    starter_passes: list[bool] = []
                    for test in exercise.tests:
                        namespace: dict[str, object] = {}
                        try:
                            exec(starter_source, namespace)
                            starter_passes.append(bool(eval(test, namespace)))
                        except Exception:
                            starter_passes.append(False)
                    if all(starter_passes):
                        failures.append(f"{label}: buggy starter passes all tests")

    expected_slugs = {seed.slug for seed in SEEDS}
    unknown_check_seeds = SOURCE_CHECKS_BY_SEED.keys() - expected_slugs
    if unknown_check_seeds:
        failures.append(f"source checks reference unknown seeds: {sorted(unknown_check_seeds)}")
    unknown_checks = {
        check
        for checks in SOURCE_CHECKS_BY_SEED.values()
        for check in checks
        if check not in CHECK_DESCRIPTIONS
    }
    if unknown_checks:
        failures.append(f"unknown source checks: {sorted(unknown_checks)}")
    if require_complete:
        missing = expected_slugs - catalogs.keys()
        extra = catalogs.keys() - expected_slugs
        if missing:
            failures.append(f"missing seeds: {sorted(missing)}")
        if extra:
            failures.append(f"unknown seeds: {sorted(extra)}")
        if sum(len(group) for group in catalogs.values()) != 820:
            failures.append("complete catalog must contain exactly 820 exercises")
    else:
        extra = catalogs.keys() - expected_slugs
        if extra:
            failures.append(f"unknown seeds: {sorted(extra)}")

    for values, description in (
        (function_names, "function names"),
        (slugs, "exercise slugs"),
        (tasks, "tasks"),
        (test_suites, "test suites"),
    ):
        if len(values) != len(set(values)):
            duplicates = sorted(
                {str(value) for value in values if values.count(value) > 1}
            )
            failures.append(f"duplicate {description}: {duplicates[:5]}")

    if failures:
        raise SystemExit("\n".join(failures))

    print(f"modules={len(module_names)}")
    print(f"seeds={len(catalogs)}")
    print(f"exercises={sum(len(group) for group in catalogs.values())}")
    print(f"unique_functions={len(set(function_names))}")
    print(f"unique_tasks={len(set(tasks))}")
    print(f"unique_test_suites={len(set(test_suites))}")


def main() -> None:
    requested = tuple(sys.argv[1:])
    validate(requested or MODULE_NAMES, require_complete=not requested)


if __name__ == "__main__":
    main()
