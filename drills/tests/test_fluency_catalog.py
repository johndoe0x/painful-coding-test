"""Reference and counterexample checks for short Python-tool drills."""

import ast
from collections import Counter, defaultdict, deque
from copy import deepcopy
import bisect
import heapq
import inspect
import itertools
from operator import itemgetter
from pathlib import Path
from types import GeneratorType
import unittest

from python_coding.fluency_catalog import IN_PLACE_IDS, PURPOSE, REPLACEMENTS
from python_basic.source_checks import failed_source_checks


def stable_descending_key(records):
    return sorted(records, key=lambda row: row[1], reverse=True)


def casefold_sort(words):
    return sorted(words, key=str.casefold)


def none_last_sort(values):
    return sorted(values, key=lambda value: (value is None, value if value is not None else 0))


def itemgetter_two_fields(rows):
    return sorted(rows, key=itemgetter('team', 'rank'))


def sort_in_place(values):
    return values.sort(reverse=True)


def sorted_indices(values):
    return sorted(range(len(values)), key=values.__getitem__)


def enumerate_offset(values, start):
    return [f'{index}:{value}' for index, value in enumerate(values, start=start)]


def zip_longest_fill(left, right, fill):
    return list(itertools.zip_longest(left, right, fillvalue=fill))


def starred_unpack(values):
    first, *middle, last = values
    return first, middle, last


def zip_to_mapping(keys, values):
    return dict(zip(keys, values))


def yield_even_squares(values):
    for value in values:
        if value % 2 == 0:
            yield value * value


def next_with_default(values, count, default):
    iterator = iter(values)
    return [next(iterator, default) for _ in range(count)]


def slice_replace_in_place(values, start, stop, replacement):
    values[start:stop] = replacement


def shallow_outer_copy(rows):
    return rows.copy()


def independent_row_copy(rows):
    return [row.copy() for row in rows]


def pop_copy_index(values, index):
    result = values.copy()
    value = result.pop(index) if -len(result) <= index < len(result) else None
    return value, result


def extended_slice_assignment(values, step, replacement):
    if len(values[::step]) != len(replacement):
        return None
    result = values.copy()
    result[::step] = replacement
    return result


def dict_order_deduplicate(values):
    return list(dict.fromkeys(values))


def deque_until_stop(values, stop):
    pending, result = deque(values), []
    while pending:
        value = pending.popleft()
        if value == stop:
            break
        result.append(value)
    return result, list(pending)


def deque_maxlen(values, capacity):
    result = deque(maxlen=capacity)
    for value in values:
        result.append(value)
    return list(result)


def deque_rotate_pop(values, steps):
    result = deque(values)
    result.rotate(steps)
    return (result.popleft(), list(result)) if result else (None, [])


def deque_extendleft(start, additions):
    result = deque(start)
    result.extendleft(additions)
    return list(result)


def stack_push_pop_batch(start, additions, count):
    result, popped = start.copy(), []
    for value in additions:
        result.append(value)
    for _ in range(count):
        popped.append(result.pop() if result else None)
    return popped, result


def queue_take(values, count):
    pending = deque(values)
    result = [pending.popleft() for _ in range(min(count, len(pending)))]
    return result, list(pending)


def enumerate_cells(rows):
    result = []
    for row, values in enumerate(rows):
        for col, value in enumerate(values):
            if value != 0:
                result.append((row, col, value))
    return result


def copy_update_cell(rows, row, col, value):
    result = [values.copy() for values in rows]
    result[row][col] = value
    return result


def zip_transpose_rows(rows):
    return [list(col) for col in zip(*rows)]


def shared_row_identity(rows):
    result = []
    for left in range(len(rows)):
        for right in range(left + 1, len(rows)):
            if rows[left] is rows[right]:
                result.append((left, right))
    return result


def chain_flatten(rows):
    return list(itertools.chain.from_iterable(rows))


def independent_checkerboard(rows, cols, first):
    return [[(row + col + first) % 2 for col in range(cols)] for row in range(rows)]


def counter_signed_subtract(left, right):
    result = Counter(left)
    result.subtract(right)
    return dict(result)


def counter_intersection(left, right):
    return dict(Counter(left) & Counter(right))


def defaultdict_unique_groups(pairs):
    groups = defaultdict(set)
    for key, value in pairs:
        groups[key].add(value)
    return {key: sorted(values) for key, values in groups.items()}


def mapping_missing_vs_none(mapping, keys, default):
    return [mapping.get(key, default) for key in keys]


def mapping_pop_presence(mapping, key):
    result = mapping.copy()
    present = key in result
    value = result.pop(key, None)
    return present, value, result


def set_symmetric_difference(left, right):
    return left.symmetric_difference(right)


def heap_pushpop_contract(values, incoming):
    result = values.copy()
    heapq.heapify(result)
    popped = heapq.heappushpop(result, incoming)
    return popped, sorted(result)


def heap_replace_contract(values, incoming):
    if not values:
        return None, []
    result = values.copy()
    heapq.heapify(result)
    popped = heapq.heapreplace(result, incoming)
    return popped, sorted(result)


def nsmallest_records(records, count):
    return heapq.nsmallest(count, records, key=lambda row: row[1])


def nlargest_word_lengths(words, count):
    return heapq.nlargest(count, words, key=len)


def merge_islice_prefix(batches, count):
    return list(itertools.islice(heapq.merge(*batches), count))


def heap_commands(operations):
    values, result = [], []
    for command, value in operations:
        if command == 'push':
            heapq.heappush(values, value)
        elif command == 'peek':
            result.append(values[0] if values else None)
        else:
            result.append(heapq.heappop(values) if values else None)
    return result


def bisect_subrange(values, target, low, high):
    return bisect.bisect_left(values, target, low, high), bisect.bisect_right(values, target, low, high)


def insort_right_key(records, incoming):
    result = records.copy()
    bisect.insort_right(result, incoming, key=lambda item: item[0])
    return result


def bisect_remove_all(values, target):
    result = values.copy()
    del result[bisect.bisect_left(result, target):bisect.bisect_right(result, target)]
    return result


def bisect_ceiling_queries(values, queries):
    result = []
    for query in queries:
        index = bisect.bisect_left(values, query)
        result.append(values[index] if index < len(values) else None)
    return result


def bisect_record_key(records, target):
    index = bisect.bisect_left(records, target, key=lambda item: item[0])
    return records[index][1] if index < len(records) and records[index][0] == target else None


def bisect_three_slices(values, target):
    left, right = bisect.bisect_left(values, target), bisect.bisect_right(values, target)
    return values[:left], values[left:right], values[right:]


REFERENCES = {number: globals()[template.slug] for number, template in REPLACEMENTS.items()}
EXTRA = {
    22: (([('z', 0), ('a', 0)],), [('z', 0), ('a', 0)]),
    23: ((['z', 'Straße', 'STRASSE'],), ['Straße', 'STRASSE', 'z']),
    24: (([None, None, -1],), [-1, None, None]),
    25: (([{'team': 1, 'rank': -1}, {'team': 0, 'rank': 9}],), [{'team': 0, 'rank': 9}, {'team': 1, 'rank': -1}]),
    26: (([4, 4, -2],), None),
    27: (([7, 7, -7],), [2, 0, 1]),
    122: ((['x:y'], 0), ['0:x:y']),
    123: (([0], [1, 2, 3], -9), [(0, 1), (-9, 2), (-9, 3)]),
    124: (([-1, 0, 1, 2, 3],), (-1, [0, 1, 2], 3)),
    125: ((['a', 'b', 'a'], [1, 2]), {'a': 1, 'b': 2}),
    126: (([0, -3, -2, 2],), [0, 4, 4]),
    127: (([8], 3, 0), [8, 0, 0]),
    242: (([1, 2, 3], 2, 1, [7]), None),
    243: (([[], [9]],), [[], [9]]),
    244: (([[], [9]],), [[], [9]]),
    245: (([2, 4, 6], -3), (2, [4, 6])),
    246: (([0, 1, 2, 3], 3, [8, 9]), [8, 1, 2, 9]),
    247: ((['z', 'x', 'z', 'x', 'a'],), ['z', 'x', 'a']),
    362: (([4, 4, 5], 4), ([], [4, 5])),
    363: (([1, 2, 3], 1), [3]),
    364: (([1, 2, 3, 4], 10), (3, [4, 1, 2])),
    365: (([8, 9], [0, 1]), [1, 0, 8, 9]),
    366: (([1], [2], 4), ([2, 1, None, None], [])),
    367: (([], 4), ([], [])),
    422: (([[], [0], [-1, 2]],), [(2, 0, -1), (2, 1, 2)]),
    423: (([[0, 1]], 0, 0, -9), [[-9, 1]]),
    424: (([[1, 2]],), [[1], [2]]),
    425: (([[1], [], [1]],), []),
    426: (([[0], [0], []],), [0, 0]),
    427: ((2, 2, 1), [[1, 0], [0, 1]]),
    482: ((['x'], ['x', 'x', 'y']), {'x': -1, 'y': -1}),
    483: ((['x'], ['y']), {}),
    484: (([('b', '2'), ('a', '1'), ('b', '1')],), {'b': ['1', '2'], 'a': ['1']}),
    485: (({'x': None, 'y': -1}, ['x', 'z', 'y'], 0), [None, 0, -1]),
    486: (({'x': 1}, 'y'), (False, None, {'x': 1})),
    487: (({-3, 2}, {-3, 4}), {2, 4}),
    642: (([3, 3], 3), (3, [3, 3])),
    643: (([0], -9), (0, [-9])),
    644: (([('z', 1), ('b', 1), ('a', 1)], 2), [('z', 1), ('b', 1)]),
    645: ((['Z', 'A', 'b'], 2), ['Z', 'A']),
    646: (([[-3, 1], [-2, 0]], 2), [-3, -2]),
    647: (([('push', -1), ('peek', None), ('peek', None), ('pop', None)],), [-1, -1, -1]),
    782: (([1, 2, 3], 9, 1, 1), (1, 1)),
    783: (([(1, 'b'), (1, 'a')], (1, '0')), [(1, 'b'), (1, 'a'), (1, '0')]),
    784: (([2, 2, 2], 2), []),
    785: (([-2, 0], [-3, -2, 1]), [-2, -2, None]),
    786: (([(0, 'z'), (0, 'a')], 0), 'z'),
    787: (([2, 2], 9), ([2, 2], [], [])),
}


def accepts(number, implementation):
    try:
        return all(eval(test, {'__FN__': implementation}) is True
                   for test in REPLACEMENTS[number].tests)
    except (AssertionError, TypeError, ValueError, IndexError, StopIteration):
        return False


class FluencyTests(unittest.TestCase):
    def test_frozen_scope_ids_and_time_caps(self):
        starts = (22, 122, 242, 362, 422, 482, 642, 782)
        self.assertEqual(set(REPLACEMENTS), {start + n for start in starts for n in range(6)})
        self.assertEqual(set(REFERENCES), set(EXTRA))
        self.assertEqual(PURPOSE, 'PYTHON_TOOL_FLUENCY')
        for template in REPLACEMENTS.values():
            self.assertTrue(150 <= template.time_cap <= 300)
            self.assertEqual(len(template.tests), 3)
            self.assertNotIn('bridge', template.slug)
            for word in ('Dijkstra', 'MST', 'Union-Find', 'N-Queen', '백트래킹', '위상 정렬'):
                self.assertNotIn(word, template.task)

    def test_repetition_remains_part_of_the_training_bank(self):
        from review_bank import collect
        bank = collect()['banks']['CI']
        self.assertEqual(bank['count'], 800)
        self.assertEqual({row['study_role'] for row in bank['problems']}, {'automation_drill'})
        self.assertGreater(bank['repeated_learning_entries'], 0)
        self.assertEqual(bank['optional_recall_entries'], 0)

    def test_all_144_public_assertions(self):
        for number, reference in REFERENCES.items():
            with self.subTest(problem=number):
                self.assertTrue(accepts(number, reference))

    def test_48_independent_extra_goldens_and_mutation_contracts(self):
        for number, (args, expected) in EXTRA.items():
            with self.subTest(problem=number):
                args = deepcopy(args)
                before = deepcopy(args)
                result = REFERENCES[number](*args)
                if isinstance(result, GeneratorType):
                    result = list(result)
                self.assertEqual(result, expected)
                if number not in IN_PLACE_IDS:
                    self.assertEqual(args, before)
        v = [4, 4, -2]
        self.assertIsNone(sort_in_place(v))
        self.assertEqual(v, [4, 4, -2])
        v = [1, 2, 3]
        self.assertIsNone(slice_replace_in_place(v, 2, 1, [7]))
        self.assertEqual(v, [1, 2, 7, 3])

    def test_reference_uses_required_python_constructs(self):
        imports = '\n'.join(line for line in Path(__file__).read_text().splitlines()
                            if line.startswith(('import ', 'from ')))
        for number, reference in REFERENCES.items():
            with self.subTest(problem=number):
                source = imports + '\n' + inspect.getsource(reference)
                self.assertEqual(failed_source_checks(source, reference.__name__,
                                 REPLACEMENTS[number].source_checks), [])

    def test_wrong_api_semantics_are_rejected(self):
        wrong = {
            22: lambda records: sorted(records, key=lambda r: (-r[1], r[0])),
            23: lambda words: sorted(words, key=str.lower),
            24: lambda values: sorted(values),
            26: lambda values: sorted(values, reverse=True),
            123: lambda left, right, fill: list(zip(left, right)),
            124: lambda values: (values[0], tuple(values[1:-1]), values[-1]),
            125: lambda keys, values: {key: values[keys.index(key)] for key in keys},
            126: lambda values: [x*x for x in values if x % 2 == 0],
            127: lambda values, count, default: values[:count],
            242: lambda values, start, stop, replacement: values[:start] + replacement + values[stop:],
            243: deepcopy,
            244: lambda rows: rows.copy(),
            247: lambda values: sorted(set(values)),
            363: lambda values, capacity: values[-capacity:],
            365: lambda start, additions: additions + start,
            423: lambda rows, row, col, value: _shallow_update(rows, row, col, value),
            425: lambda rows: [(i, j) for i in range(len(rows)) for j in range(i+1, len(rows)) if rows[i] == rows[j]],
            427: lambda rows, cols, first: [[(c+first)%2 for c in range(cols)]] * rows,
            482: lambda left, right: dict(Counter(left) - Counter(right)),
            483: lambda left, right: dict(Counter(left) | Counter(right)),
            485: lambda mapping, keys, default: [mapping.get(k) or default for k in keys],
            486: lambda mapping, key: (mapping.get(key) is not None, mapping.get(key), {k:v for k,v in mapping.items() if k != key}),
            487: lambda left, right: left | right,
            642: heap_replace_contract,
            643: heap_pushpop_contract,
            644: lambda records, count: sorted(records, key=lambda r: (r[1], r[0]))[:count],
            645: lambda words, count: heapq.nlargest(count, words),
            646: lambda batches, count: list(itertools.chain.from_iterable(batches))[:count],
            783: lambda records, incoming: _insort_left(records, incoming),
            786: lambda records, target: _bisect_wrong_target(records, target),
        }
        for number, implementation in wrong.items():
            with self.subTest(problem=number):
                self.assertFalse(accepts(number, implementation))

    def test_boundary_matrix_against_simple_python_expectations(self):
        for size in range(5):
            for values in itertools.product((-1, 0, 1), repeat=size):
                values = list(values)
                ordered = sorted(values)
                for target in (-2, -1, 0, 1, 2):
                    self.assertEqual(bisect_remove_all(ordered, target), [x for x in ordered if x != target])
                    self.assertEqual(bisect_three_slices(ordered, target),
                                     ([x for x in ordered if x < target], [x for x in ordered if x == target], [x for x in ordered if x > target]))
                    popped, rest = heap_pushpop_contract(values, target)
                    self.assertEqual([popped] + rest, sorted(values + [target]))
                for count in (0, 1, 5):
                    self.assertEqual(queue_take(values, count), (values[:count], values[count:]))
                    self.assertEqual(deque_maxlen(values, count), values[-count:] if count else [])


def _shallow_update(rows, row, col, value):
    result = rows.copy()
    result[row][col] = value
    return result


def _insort_left(records, incoming):
    result = records.copy()
    bisect.insort_left(result, incoming, key=lambda x: x[0])
    return result


def _bisect_wrong_target(records, target):
    return bisect.bisect_left(records, (target, ''), key=lambda x: x[0])


if __name__ == '__main__':
    unittest.main()
