"""Regression checks for strengthened Basic contracts.

Wrong snippets check missing branches and input mutation. Positive controls are
internal test fixtures, never copied into generated learner problem starters.
"""

from __future__ import annotations

import ast
from collections import defaultdict
import unittest

from python_basic.catalog import EXERCISES
from python_basic.generate_bank import SEEDS
from python_basic.source_checks import checks_for_seed, failed_source_checks


CATALOG = {
    f"PB{seed_index * 10 + variant_index + 1:04d}": (seed, exercise)
    for seed_index, seed in enumerate(SEEDS)
    for variant_index, exercise in enumerate(EXERCISES[seed.slug])
}

# Each snippet used to satisfy all public examples and its source checks.
MISSING_BRANCH_MUTANTS = {
    "PB0191": "return is_owner or is_owner",
    "PB0192": "return day == 'Saturday' or day == 'Saturday'",
    "PB0193": "return left == '' or left == ''",
    "PB0194": (
        "return bool(text) and (text[0].lower() in 'aeiou' "
        "or text[0].lower() in 'aeiou')"
    ),
    "PB0196": "return has_message or has_message",
    "PB0197": "return value == low or value == high",
    "PB0198": "return bool(text) or False",
    "PB0199": "return x == 0 or x == 0",
    "PB0200": "return role == 'editor' or role == 'editor'",
    "PB0201": "return consent_ok and consent_ok",
    "PB0202": "return value <= maximum and value <= maximum",
    "PB0203": "return width > 0 and width > 0",
    "PB0204": "return bool(password) and any(c.isdigit() for c in password)",
    "PB0205": "return x > 0 and x > 0",
    "PB0206": "return number > 0 and number > 0",
    "PB0207": "return len(text) <= maximum and len(text) <= maximum",
    "PB0209": "return bool(character) and character.islower()",
    "PB0210": "return bool(flags) and flags[-1]",
    "PB0220": "return not left",
}

INPUT_MUTATION_MUTANTS = {
    "PB0187": "for chunk in chunks:\n    start += chunk\nreturn start",
    "PB0666": "values.add(candidate)\nreturn values",
    "PB0701": "mapping[key] = value\nreturn mapping",
    "PB0703": "counts[key] = counts.get(key, 0) + amount\nreturn counts",
    "PB0704": "if old in mapping:\n    mapping[new] = mapping.pop(old)\nreturn mapping",
    "PB0705": "left.update(right)\nreturn left",
    "PB0706": "mapping.setdefault(key, value)\nreturn mapping",
    "PB0707": (
        "if first in mapping and second in mapping:\n"
        "    mapping[first], mapping[second] = mapping[second], mapping[first]\n"
        "return mapping"
    ),
    "PB0708": "for key, value in updates:\n    mapping[key] = value\nreturn mapping",
    "PB0709": (
        "for key, change in changes.items():\n"
        "    stock[key] = stock.get(key, 0) + change\n"
        "return stock"
    ),
    "PB0710": "settings[key] = not settings.get(key, False)\nreturn settings",
    "PB0731": "for key in keys:\n    mapping.pop(key, None)\nreturn mapping",
    "PB0732": "value = mapping.pop(key, None)\nreturn mapping, value",
    "PB0805": (
        "try:\n"
        "    value = values.pop()\n"
        "except IndexError:\n"
        "    value = None\n"
        "return values, value"
    ),
}


POSITIVE_CONTROLS = {
    "PB0187": "result = start.copy()\nfor chunk in chunks:\n    result += chunk\nreturn result",
    "PB0191": "return is_admin or is_owner",
    "PB0192": "return day == 'Saturday' or day == 'Sunday'",
    "PB0193": "return left == '' or right == ''",
    "PB0194": (
        "return bool(text) and (text[0].lower() in 'aeiou' "
        "or text[-1].lower() in 'aeiou')"
    ),
    "PB0195": "return is_member or order_total >= 100",
    "PB0196": "return has_message or has_alert",
    "PB0197": "return value <= low or value >= high",
    "PB0198": "return text.startswith('#') or text.endswith('!')",
    "PB0199": "return x == 0 or y == 0",
    "PB0200": "return role == 'editor' or role == 'viewer'",
    "PB0201": "return age_ok and consent_ok",
    "PB0202": "return value >= minimum and value <= maximum",
    "PB0203": "return width > 0 and height > 0",
    "PB0204": "return len(password) >= 8 and any(c.isdigit() for c in password)",
    "PB0205": "return x > 0 and y > 0",
    "PB0206": "return number > 0 and number % 2 == 0",
    "PB0207": "return len(text) >= minimum and len(text) <= maximum",
    "PB0208": "return in_stock and balance >= price",
    "PB0209": "return len(character) == 1 and 'a' <= character <= 'z'",
    "PB0210": "return bool(flags) and all(flags)",
    "PB0213": "return [index for index, flag in enumerate(flags) if not flag]",
    "PB0220": "return not (left or right)",
    "PB0272": (
        "return ['(missing)' if name is None else '(empty)' if name == '' "
        "else f'user:{name}' for name in names]"
    ),
    "PB0666": "return values | {candidate}",
    "PB0701": "result = mapping.copy()\nresult[key] = value\nreturn result",
    "PB0703": (
        "result = counts.copy()\n"
        "result[key] = result.get(key, 0) + amount\n"
        "return result"
    ),
    "PB0704": (
        "result = mapping.copy()\n"
        "if old in result:\n"
        "    value = result.pop(old)\n"
        "    result[new] = value\n"
        "return result"
    ),
    "PB0705": "return {**left, **right}",
    "PB0706": "result = mapping.copy()\nresult.setdefault(key, value)\nreturn result",
    "PB0707": (
        "result = mapping.copy()\n"
        "if first in result and second in result:\n"
        "    result[first], result[second] = result[second], result[first]\n"
        "return result"
    ),
    "PB0708": (
        "result = mapping.copy()\n"
        "for key, value in updates:\n"
        "    result[key] = value\n"
        "return result"
    ),
    "PB0709": (
        "result = stock.copy()\n"
        "for key, value in changes.items():\n"
        "    result[key] = result.get(key, 0) + value\n"
        "return result"
    ),
    "PB0710": (
        "result = settings.copy()\n"
        "result[key] = not result.get(key, False)\n"
        "return result"
    ),
    "PB0731": "result = mapping.copy()\nfor key in keys:\n    result.pop(key, None)\nreturn result",
    "PB0732": "result = mapping.copy()\nvalue = result.pop(key, None)\nreturn result, value",
    "PB0805": (
        "result = values.copy()\n"
        "try:\n"
        "    value = result.pop()\n"
        "except IndexError:\n"
        "    value = None\n"
        "return result, value"
    ),
}


def evaluate_candidate(problem_id: str, body: str) -> tuple[list[bool], list[str]]:
    seed, exercise = CATALOG[problem_id]
    source = exercise.signature + "\n" + "\n".join(
        "    " + line for line in body.splitlines()
    )
    function = ast.parse(source).body[0]
    namespace: dict[str, object] = {}
    exec(source, namespace)
    results = [bool(eval(expression, namespace)) for expression in exercise.tests]
    return results, failed_source_checks(source, function.name, checks_for_seed(seed.slug))


class NormalizeTargetName(ast.NodeTransformer):
    def __init__(self, target: str) -> None:
        self.target = target

    def visit_Name(self, node: ast.Name) -> ast.Name:
        if node.id == self.target:
            node.id = "TARGET_FUNCTION"
        return node


class BasicQualityTests(unittest.TestCase):
    def test_positive_controls_satisfy_all_changed_contracts(self) -> None:
        self.assertEqual(len(POSITIVE_CONTROLS), 37)
        for problem_id, body in POSITIVE_CONTROLS.items():
            with self.subTest(problem=problem_id):
                results, source_failures = evaluate_candidate(problem_id, body)
                self.assertEqual(results, [True, True, True])
                self.assertEqual(source_failures, [])

    def test_branch_mistakes_are_rejected_by_behavior_not_syntax(self) -> None:
        for problem_id, body in MISSING_BRANCH_MUTANTS.items():
            with self.subTest(problem=problem_id):
                results, source_failures = evaluate_candidate(problem_id, body)
                self.assertEqual(source_failures, [])
                self.assertFalse(all(results), "a missing-branch implementation passed")

    def test_original_inputs_must_survive_copy_operations(self) -> None:
        for problem_id, body in INPUT_MUTATION_MUTANTS.items():
            with self.subTest(problem=problem_id):
                results, source_failures = evaluate_candidate(problem_id, body)
                self.assertEqual(source_failures, [])
                self.assertFalse(all(results), "an input-mutating implementation passed")

    def test_replacements_have_distinct_data_contracts(self) -> None:
        _, inactive = CATALOG["PB0213"]
        self.assertEqual(
            inactive.signature,
            "def inactive_indices(flags: list[bool]) -> list[int]:",
        )
        _, optional_names = CATALOG["PB0272"]
        self.assertEqual(
            optional_names.signature,
            "def label_optional_names(names: list[str | None]) -> list[str]:",
        )
        self.assertIn("None", optional_names.task)
        self.assertIn("빈 문자열", optional_names.task)

    def test_no_rename_only_test_duplicate_with_the_same_practice_mode(self) -> None:
        signatures: dict[tuple[object, ...], list[str]] = defaultdict(list)
        for problem_id, (seed, exercise) in CATALOG.items():
            name = ast.parse(exercise.signature + "\n    pass").body[0].name
            normalized = tuple(
                ast.dump(
                    NormalizeTargetName(name).visit(ast.parse(test, mode="eval")),
                    include_attributes=False,
                )
                for test in exercise.tests
            )
            # A bug-fix starter or a different enforced construct is purposeful
            # retrieval practice, not an independently distinct algorithm.
            mode = (checks_for_seed(seed.slug), exercise.starter_body is not None)
            signatures[(*mode, normalized)].append(problem_id)
        duplicates = [ids for ids in signatures.values() if len(ids) > 1]
        self.assertEqual(duplicates, [])

    def test_catalog_retains_exactly_three_documentable_assertions(self) -> None:
        self.assertEqual(len(CATALOG), 820)
        for problem_id, (_, exercise) in CATALOG.items():
            with self.subTest(problem=problem_id):
                self.assertEqual(len(exercise.tests), 3)
                self.assertEqual(len(set(exercise.tests)), 3)
                for expression in exercise.tests:
                    ast.parse(expression, mode="eval")


if __name__ == "__main__":
    unittest.main()
