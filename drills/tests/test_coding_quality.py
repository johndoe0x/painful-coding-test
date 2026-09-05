"""Generator-contract regressions; these do not execute or edit learner files."""
from __future__ import annotations

import ast
from collections import Counter, deque
import heapq
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

CODING_ROOT = Path(__file__).resolve().parents[1] / "python_coding"
sys.path.insert(0, str(CODING_ROOT))

from quality_catalog import TEMPLATES
from quality_regenerate import build_catalog, digest, plan_actions
from python_coding.validate_bank import argument_binding_errors, normalized_test_suite


def template(slug: str):
    return next(item for group in TEMPLATES.values() for item in group if item.slug == slug)


def passes_examples(slug: str, implementation) -> bool:
    return all(eval(case, {"__FN__": implementation}) for case in template(slug).tests)


class CodingContractTests(unittest.TestCase):
    def test_all_generated_example_calls_bind_to_signature(self):
        for build in build_catalog():
            with self.subTest(problem=build.problem_id):
                function = ast.parse(build.exercise.signature + "\n    pass").body[0]
                for case in build.exercise.tests:
                    self.assertEqual(argument_binding_errors(function, ast.parse(case)), [])

    def test_binding_rejects_missing_argument_without_executing_example(self):
        function = ast.parse("def nearest(values, target):\n    pass").body[0]
        errors = argument_binding_errors(function, ast.parse("nearest([]) is None"))
        self.assertEqual(len(errors), 1)
        self.assertIn("target", errors[0])

    def test_binding_handles_defaults_and_keyword_arguments(self):
        function = ast.parse("def example(values, target=0, *, strict=False):\n    pass").body[0]
        self.assertEqual(argument_binding_errors(function, ast.parse("example([], strict=True)")), [])
        self.assertTrue(argument_binding_errors(function, ast.parse("example([], unknown=True)")))

    def test_normalization_removes_function_names_not_input_literals(self):
        self.assertEqual(
            normalized_test_suite("alpha", ("alpha([1]) == [1]",)),
            normalized_test_suite("beta", ("beta([1]) == [1]",)),
        )
        self.assertNotEqual(
            normalized_test_suite("alpha", ("alpha(['alpha']) == ['alpha']",)),
            normalized_test_suite("beta", ("beta(['beta']) == ['beta']",)),
        )

    def test_rpn_examples_require_truncation_toward_zero_and_exact_integers(self):
        def evaluate(tokens, mode="exact"):
            stack = []
            for token in tokens:
                if token not in {"+", "-", "*", "/"}:
                    stack.append(int(token))
                    continue
                right, left = stack.pop(), stack.pop()
                if token == "+": result = left + right
                elif token == "-": result = left - right
                elif token == "*": result = left * right
                elif mode == "floor": result = left // right
                elif mode == "float": result = int(left / right)
                else:
                    result = abs(left) // abs(right)
                    if (left < 0) != (right < 0): result = -result
                stack.append(result)
            return stack[0]
        self.assertTrue(passes_examples("evaluate_rpn", evaluate))
        self.assertFalse(passes_examples("evaluate_rpn", lambda tokens: evaluate(tokens, "floor")))
        self.assertFalse(passes_examples("evaluate_rpn", lambda tokens: evaluate(tokens, "float")))

    def test_heap_comparison_cannot_pass_with_constant_true(self):
        def compare(values):
            first, second = list(values), []
            heapq.heapify(first)
            for value in values:
                heapq.heappush(second, value)
            return ([heapq.heappop(first) for _ in range(len(first))],
                    [heapq.heappop(second) for _ in range(len(second))])
        self.assertTrue(passes_examples("heap_build_comparison", compare))
        self.assertFalse(passes_examples("heap_build_comparison", lambda values: True))

    def test_isomorphism_examples_reject_length_and_reverse_mapping_bugs(self):
        def correct(left, right):
            return len(left) == len(right) and len(set(left)) == len(set(right)) == len(set(zip(left, right)))
        self.assertTrue(passes_examples("isomorphic_strings", correct))
        self.assertFalse(passes_examples("isomorphic_strings", lambda a, b: len(set(a)) == len(set(zip(a, b)))))

    def test_missing_remove_does_not_delete_a_future_insertion(self):
        def reference(operations):
            values = Counter()
            result = []
            for command, value in operations:
                if command == "add": values[value] += 1
                elif command == "remove" and values[value]: values[value] -= 1
                elif command == "min": result.append(min((v for v, n in values.items() if n), default=None))
            return result
        self.assertTrue(passes_examples("lazy_delete_min", reference))

    def test_duplicate_and_empty_contract_policies(self):
        def join(left, right):
            indexed = dict(right)
            return [(key, value, indexed[key]) for key, value in left if key in indexed]

        def history(records, queries):
            indexed = {}
            for key, timestamp, value in records:
                indexed[(key, timestamp)] = value
            return [indexed.get(max(
                ((key, timestamp) for key, timestamp in indexed if key == query_key and timestamp <= when),
                default=None,
            )) for query_key, when in queries]

        def two_sum(values, target):
            for right in range(len(values)):
                for left in range(right):
                    if values[left] + values[right] == target:
                        return left, right
            return None

        def word_break(text, words):
            reachable = {0}
            for end in range(1, len(text) + 1):
                if any(text[start:end] in words for start in reachable):
                    reachable.add(end)
            return len(text) in reachable

        references = {"hash_join": join, "time_map": history,
                      "two_sum_indices": two_sum, "word_break_cached": word_break}
        for slug, implementation in references.items():
            with self.subTest(contract=slug):
                self.assertTrue(passes_examples(slug, implementation))

    def test_bfs_cycle_and_missing_adjacency_contract(self):
        def traverse(graph, start):
            seen, pending, output = {start}, deque([start]), []
            while pending:
                node = pending.popleft()
                output.append(node)
                for child in graph.get(node, []):
                    if child not in seen:
                        seen.add(child)
                        pending.append(child)
            return output
        self.assertTrue(passes_examples("bfs_order", traverse))

    def test_scheduler_examples_require_available_nonpreemptive_selection(self):
        def schedule(tasks):
            pending, now, output = list(tasks), 0, []
            while pending:
                available = [task for task in pending if task[0] <= now]
                if not available:
                    now = min(task[0] for task in pending)
                    continue
                selected = min(available, key=lambda task: (task[1], task[2]))
                pending.remove(selected)
                now += selected[1]
                output.append(selected[2])
            return output
        self.assertTrue(passes_examples("task_schedule", schedule))

    def test_repaired_sorted_query_examples_have_correct_oracles(self):
        def nearest(values, target):
            return min(values, key=lambda value: (abs(value - target), value), default=None)

        def pair_count(values, target):
            return sum(values[left] + values[right] <= target
                       for right in range(len(values)) for left in range(right))

        self.assertTrue(passes_examples("nearest_value", nearest))
        self.assertTrue(passes_examples("pair_sum_count", pair_count))

    def test_unmanifested_partial_solution_is_archived_even_with_todo(self):
        build = build_catalog()[0]
        previous = CODING_ROOT / build.relative_path
        partial = build.starter_source.replace(
            '    raise NotImplementedError', '    progress = "learner work"\n    raise NotImplementedError'
        )
        with patch("quality_regenerate.load_manifest", return_value={"problems": {}}), \
             patch("quality_regenerate.existing_problems", return_value={build.problem_id: [previous]}), \
             patch.object(Path, "read_text", return_value=partial):
            action = plan_actions([build])[0]
        self.assertEqual(action.reason, "preserved_user_work")
        self.assertTrue(action.archive_source.endswith("\0" + partial))
        self.assertIn('progress = "learner work"', action.source)

    def test_replacement_rename_refuses_intervening_learner_edit(self):
        build = next(build for build in build_catalog() if "_bridge_" in build.exercise.slug)
        old_path = CODING_ROOT / build.relative_path.parent / f"{build.problem_id}_old.py"
        pristine, partial = "old starter", "old starter\n# learner note"
        manifest = {"problems": {build.problem_id: {"starter_sha256": digest(pristine)}}}
        with patch("quality_regenerate.load_manifest", return_value=manifest), \
             patch("quality_regenerate.existing_problems", return_value={build.problem_id: [old_path]}), \
             patch.object(Path, "read_text", return_value=partial):
            with self.assertRaisesRegex(RuntimeError, "manifest-confirmed pristine"):
                plan_actions([build])


if __name__ == "__main__":
    unittest.main()
