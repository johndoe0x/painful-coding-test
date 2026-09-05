"""48 short drills for Python syntax and standard-library fluency."""

import ast
from dataclasses import replace

from python_coding.quality_catalog import ChallengeTemplate, T

PURPOSE = "PYTHON_TOOL_FLUENCY"
IN_PLACE_IDS = frozenset({26, 242})


def D(slug, title, signature, task, focus, a, b, c, *checks, time_cap=150):
    return T(slug, title, signature,
             task + " 입력 컬렉션은 각각 1,000개 이하입니다.",
             focus, a, b, c, *checks, time_cap=time_cap)


REPLACEMENTS: dict[int, ChallengeTemplate] = {
    22: D("stable_descending_key", "점수 내림차순과 동률 순서", "(records: list[tuple[str, int]]) -> list[tuple[str, int]]:",
          "sorted의 key와 reverse로 (이름, 점수)를 점수 내림차순 정렬하세요. 동률은 입력 순서이며 원본은 보존합니다.", "reverse=True의 안정성",
          "__FN__([('b', 2), ('a', 2), ('z', 3)]) == [('z', 3), ('b', 2), ('a', 2)]", "__FN__([]) == []",
          "__FN__([('b', -1), ('a', -1), ('c', 0)]) == [('c', 0), ('b', -1), ('a', -1)]", "sorted_call"),
    23: D("casefold_sort", "대소문자 무시 key와 원래 표기", "(words: list[str]) -> list[str]:",
          "sorted의 key에 str.casefold를 사용하세요. key가 같으면 입력 순서를 유지하고 원래 표기로 반환합니다. 입력은 보존합니다.", "정렬 key와 반환 원소 분리",
          "__FN__(['b', 'A', 'a', 'B']) == ['A', 'a', 'b', 'B']", "__FN__([]) == []",
          "__FN__(['SS', 'ß', 'ss', 'a']) == ['a', 'SS', 'ß', 'ss']", "sorted_call"),
    24: D("none_last_sort", "None을 끝에 놓는 tuple key", "(values: list[int | None]) -> list[int | None]:",
          "정수는 오름차순, None은 모두 끝에 놓은 새 리스트를 sorted와 tuple key로 반환하세요. 입력은 보존합니다.", "비교 불가능한 타입의 key 분리",
          "__FN__([None, 2, -1, None, 0]) == [-1, 0, 2, None, None]", "__FN__([]) == []",
          "__FN__([0, None, 0, -2]) == [-2, 0, 0, None]", "sorted_call", time_cap=180),
    25: D("itemgetter_two_fields", "itemgetter로 두 필드 정렬", "(rows: list[dict[str, int]]) -> list[dict[str, int]]:",
          "모든 행에 정수 team과 rank 키가 있습니다. operator.itemgetter('team', 'rank')를 sorted의 key로 사용해 두 필드 모두 오름차순 정렬하세요. 동률 순서와 입력은 보존합니다.", "다중 필드 itemgetter",
          "__FN__([{'team': 2, 'rank': 0}, {'team': 1, 'rank': 2}, {'team': 1, 'rank': 1}]) == [{'team': 1, 'rank': 1}, {'team': 1, 'rank': 2}, {'team': 2, 'rank': 0}]", "__FN__([]) == []",
          "__FN__([{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]) == [{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]", "sorted_call", "itemgetter_call", time_cap=180),
    26: D("sort_in_place", "list.sort의 변경과 반환값", "(values: list[int]) -> None:",
          "values 자체를 list.sort(reverse=True)로 내림차순 정렬하고 None을 반환하세요. 새 리스트를 반환하면 안 됩니다.", "원본 객체 변경과 None 반환",
          "((v := [2, 1, 3]), __FN__(v), v) == ([3, 2, 1], None, [3, 2, 1])", "((v := []), __FN__(v), v) == ([], None, [])",
          "((v := [-1, 0, -1]), __FN__(v), v) == ([0, -1, -1], None, [0, -1, -1])", "list_sort_call"),
    27: D("sorted_indices", "값 순서대로 원래 인덱스 정렬", "(values: list[int]) -> list[int]:",
          "sorted(range(len(values)), key=...)로 값 오름차순에 해당하는 원래 인덱스를 반환하세요. 동률이면 작은 인덱스가 먼저이며 입력은 보존합니다.", "값을 key로 쓰는 인덱스 정렬",
          "__FN__([5, 2, 5, 1]) == [3, 1, 0, 2]", "__FN__([]) == []", "__FN__([0, -1, -1]) == [1, 2, 0]", "sorted_call", "range", time_cap=180),
    122: D("enumerate_offset", "enumerate 시작 번호", "(values: list[str], start: int) -> list[str]:",
           "enumerate(values, start=start)로 '번호:값' 문자열을 반환하세요. 빈 문자열과 음수 start도 그대로 처리하며 입력은 보존합니다.", "enumerate start 인수",
           "__FN__(['a', 'b'], 3) == ['3:a', '4:b']", "__FN__([], 9) == []", "__FN__(['', 'x'], -1) == ['-1:', '0:x']", "enumerate_call"),
    123: D("zip_longest_fill", "길이가 다른 열의 zip_longest", "(left: list[int], right: list[int], fill: int) -> list[tuple[int, int]]:",
           "itertools.zip_longest(fillvalue=fill)로 두 열을 긴 쪽 길이까지 묶으세요. 부족한 쪽만 fill을 사용하고 입력은 보존합니다.", "zip과 zip_longest의 길이 계약",
           "__FN__([1, 2], [9], 0) == [(1, 9), (2, 0)]", "__FN__([], [], -1) == []", "__FN__([], [0, 2], -1) == [(-1, 0), (-1, 2)]", "itertools_call"),
    124: D("starred_unpack", "별표 unpacking으로 가운데 분리", "(values: list[int]) -> tuple[int, list[int], int]:",
           "길이 2 이상인 values를 first, *middle, last로 unpack해 tuple로 반환하세요. middle은 새 리스트이고 입력은 보존합니다.", "가변 길이 unpacking과 빈 가운데",
           "__FN__([1, 2, 3, 4]) == (1, [2, 3], 4)", "__FN__([5, 6]) == (5, [], 6)", "__FN__([0, -1, 0]) == (0, [-1], 0)", "tuple_unpack"),
    125: D("zip_to_mapping", "zip으로 두 열을 딕셔너리로", "(keys: list[str], values: list[int]) -> dict[str, int]:",
           "dict(zip(keys, values))로 딕셔너리를 만드세요. 짧은 열 길이까지만 사용하고 같은 key는 마지막 값을 남깁니다. 입력은 보존합니다.", "zip 길이와 dict 중복 키",
           "__FN__(['a', 'b', 'a'], [1, 2, 3]) == {'a': 3, 'b': 2}", "__FN__([], [1]) == {}", "__FN__(['x', 'y'], [0]) == {'x': 0}", "zip_call"),
    126: D("yield_even_squares", "yield의 지연 실행", "(values: list[int]) -> object:",
           "yield로 짝수의 제곱을 순서대로 생성하는 generator를 반환하세요. 리스트를 미리 만들지 않습니다. 입력을 바꾸지 않으며 첫 next 전에 입력에 추가된 값도 순회에 포함합니다.", "generator 시작 시점과 한 번만 소비되는 iterator",
           "list(__FN__([1, 2, -4])) == [4, 16]", "list(__FN__([])) == []",
           "((v := [2]), (g := __FN__(v)), v.append(4), list(g), list(g), v)[3:] == ([4, 16], [], [2, 4])", "yield", time_cap=180),
    127: D("next_with_default", "iter와 next 기본값", "(values: list[int], count: int, default: int) -> list[int]:",
           "iter(values)를 하나 만들고 next(iterator, default)를 count번 호출한 결과를 반환하세요. 0<=count<=1000이며 소진된 뒤에도 default를 채웁니다. 입력은 보존합니다.", "iterator 소진과 StopIteration 회피",
           "__FN__([1, 2], 4, -1) == [1, 2, -1, -1]", "__FN__([1], 0, 0) == []", "__FN__([], 2, 7) == [7, 7]", "iter_call", "next_call"),
    242: D("slice_replace_in_place", "슬라이스 대입으로 길이 변경", "(values: list[int], start: int, stop: int, replacement: list[int]) -> None:",
           "values[start:stop] = replacement를 수행하고 None을 반환하세요. values 객체를 직접 바꾸고 replacement는 보존합니다. 음수와 범위 밖 경계는 Python 슬라이스 규칙을 따릅니다.", "슬라이스 조회와 대입",
           "((v := [1, 2, 3]), __FN__(v, 1, 2, [8, 9]), v) == ([1, 8, 9, 3], None, [1, 8, 9, 3])", "((v := []), __FN__(v, 0, 0, [1]), v) == ([1], None, [1])",
           "((v := [1, 2, 3]), (r := [7]), __FN__(v, -2, 99, r), v, r)[2:] == (None, [1, 7], [7])", "slice", time_cap=180),
    243: D("shallow_outer_copy", "중첩 리스트의 얕은 복사", "(rows: list[list[int]]) -> list[list[int]]:",
           "rows.copy()로 바깥 리스트만 새로 만들고 내부 행 객체는 공유하세요. 호출 중 입력을 변경하지 않습니다.", "값 동등성과 객체 정체성",
           "__FN__([[1], [2]]) == [[1], [2]]", "__FN__([]) == []", "((v := [[1], [2]]), (r := __FN__(v)), r is not v and r[0] is v[0] and r[1] is v[1])[-1]"),
    244: D("independent_row_copy", "행별 복사로 공유 끊기", "(rows: list[list[int]]) -> list[list[int]]:",
           "list comprehension에서 각 행을 copy해 바깥 리스트와 모든 행이 새 객체인 복사본을 만드세요. 입력에서 두 행이 같은 객체여도 결과 행은 각각 독립적이어야 합니다.", "shallow copy 한 단계 더 적용",
           "__FN__([[1], [], [2]]) == [[1], [], [2]]", "__FN__([]) == []", "((row := [1]), (v := [row, row]), (r := __FN__(v)), r[0] is not row and r[1] is not row and r[0] is not r[1] and r == [[1], [1]])[-1]", "comprehension"),
    245: D("pop_copy_index", "음수 인덱스로 복사본 pop", "(values: list[int], index: int) -> tuple[int | None, list[int]]:",
           "복사본에서 list.pop(index)한 값과 남은 복사본을 반환하세요. 유효 범위 -len<=index<len 밖이면 (None, 원본 사본)을 반환합니다. 입력은 보존합니다.", "pop 반환값과 음수 인덱스 경계",
           "__FN__([1, 2, 3], -2) == (2, [1, 3])", "__FN__([], 0) == (None, [])", "__FN__([5], -2) == (None, [5]) and __FN__([5], 0) == (5, [])", "pop_call", time_cap=180),
    246: D("extended_slice_assignment", "step 슬라이스 대입의 길이", "(values: list[int], step: int, replacement: list[int]) -> list[int] | None:",
           "step>0입니다. replacement 길이가 values[::step] 길이와 다르면 None, 같으면 사본의 [::step]에 대입한 새 리스트를 반환하세요. 두 입력은 보존합니다.", "확장 슬라이스 대입은 길이를 바꾸지 않음",
           "__FN__([0, 1, 2, 3, 4], 2, [8, 9, 10]) == [8, 1, 9, 3, 10]", "__FN__([], 2, []) == []", "__FN__([1, 2, 3], 2, [9]) is None", "slice", time_cap=180),
    247: D("dict_order_deduplicate", "dict.fromkeys로 첫 출현 보존", "(values: list[str]) -> list[str]:",
           "dict.fromkeys로 중복을 제거하고 첫 출현 순서의 새 리스트를 반환하세요. 문자열은 그대로 비교하고 입력은 보존합니다.", "dict 삽입 순서와 set 정렬의 차이",
           "__FN__(['b', 'a', 'b', 'c']) == ['b', 'a', 'c']", "__FN__([]) == []", "__FN__(['', 'A', 'a', '']) == ['', 'A', 'a']"),
    362: D("deque_until_stop", "deque에서 종료값까지 꺼내기", "(values: list[int], stop: int) -> tuple[list[int], list[int]]:",
           "deque에 values를 담아 왼쪽부터 꺼내세요. stop을 만나면 그것까지 제거하고 멈추며, (stop 이전 꺼낸 값, 남은 값)을 반환합니다. 없으면 전부 꺼냅니다. 입력은 보존합니다.", "popleft와 종료값 소비 여부",
           "__FN__([1, 2, 3, 2], 2) == ([1], [3, 2])", "__FN__([], 0) == ([], [])", "__FN__([4, 5], 9) == ([4, 5], [])", "deque_call", time_cap=180),
    363: D("deque_maxlen", "maxlen deque의 자동 제거", "(values: list[int], capacity: int) -> list[int]:",
           "0<=capacity<=1000입니다. deque(maxlen=capacity)에 values를 순서대로 append하고 최종 리스트를 반환하세요. capacity=0은 빈 리스트이며 입력은 보존합니다.", "bounded deque 반대쪽 자동 제거",
           "__FN__([1, 2, 3, 4], 2) == [3, 4]", "__FN__([1], 0) == []", "__FN__([1, 2], 5) == [1, 2]", "deque_call", "append_call"),
    364: D("deque_rotate_pop", "rotate 후 popleft", "(values: list[int], steps: int) -> tuple[int | None, list[int]]:",
           "deque.rotate(steps) 후 popleft한 값과 남은 리스트를 반환하세요. 양수는 오른쪽 회전입니다. 빈 입력은 (None, [])이며 입력은 보존합니다.", "회전 방향과 제거 방향 구별",
           "__FN__([1, 2, 3], 1) == (3, [1, 2])", "__FN__([], -9) == (None, [])", "__FN__([1, 2, 3], -1) == (2, [3, 1])", "deque_call", time_cap=180),
    365: D("deque_extendleft", "extendleft가 뒤집는 순서", "(start: list[int], additions: list[int]) -> list[int]:",
           "deque(start)에 extendleft(additions)를 한 번 호출한 최종 리스트를 반환하세요. additions를 미리 뒤집지 않으며 입력은 보존합니다.", "왼쪽에 차례로 넣는 순서",
           "__FN__([9], [1, 2, 3]) == [3, 2, 1, 9]", "__FN__([], []) == []", "__FN__([1], [2, 2]) == [2, 2, 1]", "deque_call"),
    366: D("stack_push_pop_batch", "stack 추가와 여러 번 pop", "(start: list[int], additions: list[int], count: int) -> tuple[list[int | None], list[int]]:",
           "start 사본에 additions를 append한 뒤 count번 pop하세요. 빈 stack에서는 None을 기록합니다. 0<=count<=1000이며 (pop 기록, 최종 stack)을 반환하고 입력은 보존합니다.", "LIFO와 underflow 처리",
           "__FN__([1], [2, 3], 2) == ([3, 2], [1])", "__FN__([], [], 2) == ([None, None], [])", "__FN__([7], [], 0) == ([], [7])", "append_call", "pop_call", time_cap=180),
    367: D("queue_take", "deque에서 앞 N개만 소비", "(values: list[int], count: int) -> tuple[list[int], list[int]]:",
           "deque.popleft로 앞에서 최대 count개를 꺼내 (꺼낸 값, 남은 값)을 반환하세요. 0<=count<=1000이며 부족하면 있는 만큼만 꺼냅니다. 입력은 보존합니다.", "FIFO 소비량 경계",
           "__FN__([1, 2, 3], 2) == ([1, 2], [3])", "__FN__([1], 0) == ([], [1])", "__FN__([1], 3) == ([1], [])", "deque_call"),
    422: D("enumerate_cells", "중첩 enumerate로 좌표 붙이기", "(rows: list[list[int]]) -> list[tuple[int, int, int]]:",
           "중첩 enumerate로 0이 아닌 셀의 (행, 열, 값)을 행 우선 순서로 반환하세요. 길이가 다른 행과 빈 행을 허용하고 입력은 보존합니다.", "행 번호와 열 번호를 따로 생성",
           "__FN__([[0, 2], [], [3]]) == [(0, 1, 2), (2, 0, 3)]", "__FN__([]) == []", "__FN__([[-1, 0, 4]]) == [(0, 0, -1), (0, 2, 4)]", "enumerate_call", "nested_loop"),
    423: D("copy_update_cell", "셀 수정 전 행별 복사", "(rows: list[list[int]], row: int, col: int, value: int) -> list[list[int]]:",
           "각 행을 copy한 새 격자를 만들고 유효한 row,col 한 칸만 value로 바꾸세요. rows는 비어 있지 않고 좌표는 0 이상입니다. 원래 격자는 보존합니다.", "바깥 리스트만 복사할 때의 alias 오류",
           "__FN__([[1, 2], [3, 4]], 0, 1, 9) == [[1, 9], [3, 4]]", "__FN__([[1]], 0, 0, 0) == [[0]]", "__FN__([[1], [], [2]], 2, 0, 7) == [[1], [], [7]]", "comprehension", time_cap=180),
    424: D("zip_transpose_rows", "zip 별표 인자로 전치", "(rows: list[list[int]]) -> list[list[int]]:",
           "직사각형 rows를 zip(*rows)로 전치하고 각 열 tuple을 리스트로 바꾸세요. 빈 격자나 빈 열이면 []이고 입력은 보존합니다.", "함수 호출의 별표 unpacking",
           "__FN__([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]", "__FN__([]) == [] and __FN__([[]]) == []", "__FN__([[1], [2]]) == [[1, 2]]", "zip_call"),
    425: D("shared_row_identity", "같은 내용과 같은 행 객체", "(rows: list[list[int]]) -> list[tuple[int, int]]:",
           "i<j이며 rows[i] is rows[j]인 모든 (i,j)를 인덱스 사전순으로 반환하세요. 값만 같은 독립 행은 제외합니다. 행은 최대 20개이고 입력은 보존합니다.", "==와 is를 중첩 리스트에서 구분",
           "__FN__([[1], [1]]) == []", "__FN__([]) == []", "((r := [1]), __FN__([r, [], r, r]))[1] == [(0, 2), (0, 3), (2, 3)]", "nested_loop", time_cap=180),
    426: D("chain_flatten", "chain.from_iterable 한 단계 평탄화", "(rows: list[list[int]]) -> list[int]:",
           "itertools.chain.from_iterable로 행들을 한 단계만 이어 새 리스트로 반환하세요. 빈 행을 허용하고 입력은 보존합니다.", "여러 iterable을 순서대로 소비",
           "__FN__([[1, 2], [], [3]]) == [1, 2, 3]", "__FN__([]) == []", "__FN__([[], [-1], [0]]) == [-1, 0]", "itertools_call"),
    427: D("independent_checkerboard", "중첩 comprehension 격자 생성", "(rows: int, cols: int, first: int) -> list[list[int]]:",
           "0<=rows,cols<=20, first는 0 또는 1입니다. cell=(행+열+first)%2인 격자를 중첩 comprehension으로 반환하세요. 행 객체는 서로 독립적이어야 합니다.", "행마다 새 리스트 생성",
           "__FN__(2, 3, 0) == [[0, 1, 0], [1, 0, 1]]", "__FN__(0, 3, 1) == [] and __FN__(2, 0, 1) == [[], []]", "((r := __FN__(3, 1, 1)), r == [[1], [0], [1]] and r[0] is not r[2])[-1]", "comprehension"),
    482: D("counter_signed_subtract", "Counter.subtract의 0과 음수", "(left: list[str], right: list[str]) -> dict[str, int]:",
           "Counter(left)에 subtract(right)를 적용해 dict로 반환하세요. 0과 음수도 남기며 right에만 있던 키도 포함합니다. 입력은 보존합니다.", "Counter - 연산과 subtract 메서드 차이",
           "__FN__(['a', 'a', 'b'], ['a', 'b', 'c']) == {'a': 1, 'b': 0, 'c': -1}", "__FN__([], []) == {}", "__FN__([], ['x', 'x']) == {'x': -2}", "counter_call"),
    483: D("counter_intersection", "Counter 교집합 최소 빈도", "(left: list[str], right: list[str]) -> dict[str, int]:",
           "두 Counter의 & 연산으로 공통 원소의 최소 양수 빈도만 dict로 반환하세요. 입력은 보존합니다.", "set 교집합과 multiset 빈도 차이",
           "__FN__(['a', 'a', 'b'], ['a', 'b', 'b']) == {'a': 1, 'b': 1}", "__FN__([], ['a']) == {}", "__FN__(['x', 'x', 'x'], ['x', 'x']) == {'x': 2}", "counter_call"),
    484: D("defaultdict_unique_groups", "defaultdict(set)과 반환 변환", "(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:",
           "defaultdict(set)으로 key별 value 중복을 제거한 뒤 각 집합을 sorted로 바꿔 dict로 반환하세요. 빈 문자열도 유효하고 입력은 보존합니다.", "기본 factory와 반환 자료형",
           "__FN__([('a', 'z'), ('a', 'b'), ('a', 'z'), ('b', 'x')]) == {'a': ['b', 'z'], 'b': ['x']}", "__FN__([]) == {}", "__FN__([('', ''), ('', 'a')]) == {'': ['', 'a']}", "defaultdict_call", "sorted_call", time_cap=180),
    485: D("mapping_missing_vs_none", "dict.get의 누락과 None", "(mapping: dict[str, int | None], keys: list[str], default: int) -> list[int | None]:",
           "각 key에 mapping.get(key, default)를 적용한 값을 순서대로 반환하세요. 저장된 None이나 0을 default로 바꾸지 않습니다. 입력은 보존합니다.", "누락 키와 falsy 값을 구분",
           "__FN__({'a': None, 'b': 0}, ['a', 'b', 'c'], 9) == [None, 0, 9]", "__FN__({}, [], 1) == []", "__FN__({}, ['x', 'x'], -1) == [-1, -1]"),
    486: D("mapping_pop_presence", "dict.pop 값과 키 존재 여부", "(mapping: dict[str, int | None], key: str) -> tuple[bool, int | None, dict[str, int | None]]:",
           "사본에서 pop(key, None)을 수행해 (호출 전 키 존재 여부, 꺼낸 값, 남은 사본)을 반환하세요. 저장된 None과 누락을 구별하고 원본은 보존합니다.", "pop default와 존재 여부",
           "__FN__({'a': None, 'b': 2}, 'a') == (True, None, {'b': 2})", "__FN__({}, 'x') == (False, None, {})", "__FN__({'a': 0}, 'a') == (True, 0, {})", "pop_call", time_cap=180),
    487: D("set_symmetric_difference", "집합 대칭 차집합", "(left: set[int], right: set[int]) -> set[int]:",
           "set.symmetric_difference 또는 집합 ^ 연산으로 한쪽에만 속한 값을 반환하세요. 두 원본은 보존합니다.", "합집합과 대칭 차집합",
           "__FN__({1, 2}, {2, 3}) == {1, 3}", "__FN__(set(), set()) == set()", "__FN__({0, -1}, {0}) == {-1}"),
    642: D("heap_pushpop_contract", "heappushpop의 반환값", "(values: list[int], incoming: int) -> tuple[int, list[int]]:",
           "사본을 heapify한 뒤 heappushpop(incoming)을 한 번 호출하세요. (꺼낸 값, 남은 값을 오름차순 정렬한 리스트)를 반환하고 입력은 보존합니다. 빈 heap도 처리합니다.", "push 후 최소값 pop 결합",
           "__FN__([2, 4], 1) == (1, [2, 4])", "__FN__([], 3) == (3, [])", "__FN__([2, 4], 5) == (2, [4, 5])", "heapq_call", "sorted_call", time_cap=180),
    643: D("heap_replace_contract", "heapreplace와 빈 heap", "(values: list[int], incoming: int) -> tuple[int | None, list[int]]:",
           "사본을 heapify한 뒤 heapreplace(incoming)을 한 번 호출하세요. (꺼낸 기존 최소값, 남은 정렬 리스트)를 반환합니다. 빈 입력은 호출하지 않고 (None, [])를 반환하며 입력은 보존합니다.", "기존 root를 먼저 제거하는 결합 연산",
           "__FN__([2, 4], 1) == (2, [1, 4])", "__FN__([], 3) == (None, [])", "__FN__([2, 4], 5) == (2, [4, 5])", "heapq_call", "sorted_call", time_cap=180),
    644: D("nsmallest_records", "nsmallest의 record key", "(records: list[tuple[str, int]], count: int) -> list[tuple[str, int]]:",
           "heapq.nsmallest로 (이름, 점수)의 점수가 작은 count개를 반환하세요. 0<=count<=1000이고 동률은 입력 순서, count가 크면 전부 반환하며 입력은 보존합니다.", "Top-K API의 key와 안정성",
           "__FN__([('b', 2), ('a', 2), ('c', 1)], 2) == [('c', 1), ('b', 2)]", "__FN__([('x', 1)], 0) == []", "__FN__([('x', -1), ('y', 0)], 9) == [('x', -1), ('y', 0)]", "heapq_call", time_cap=180),
    645: D("nlargest_word_lengths", "nlargest와 문자열 길이", "(words: list[str], count: int) -> list[str]:",
           "heapq.nlargest(count, words, key=len)로 긴 단어부터 반환하세요. 0<=count<=1000이며 동률은 입력 순서이고 입력은 보존합니다.", "key 값과 원소 자체의 비교",
           "__FN__(['bb', 'aa', 'c', 'ddd'], 3) == ['ddd', 'bb', 'aa']", "__FN__([], 3) == []", "__FN__(['', 'x'], 8) == ['x', '']", "heapq_call"),
    646: D("merge_islice_prefix", "merge iterator에서 앞 K개 소비", "(batches: list[list[int]], count: int) -> list[int]:",
           "각 배치는 오름차순입니다. heapq.merge(*batches)를 itertools.islice로 count개만 소비해 리스트로 반환하세요. 0<=count<=1000이며 중복을 유지하고 입력은 보존합니다.", "정렬 iterable과 제한된 소비 조합",
           "__FN__([[1, 4], [1, 3], []], 3) == [1, 1, 3]", "__FN__([[-1]], 0) == []", "__FN__([[], [-2, 0]], 9) == [-2, 0]", "heapq_call", "itertools_call", time_cap=240),
    647: D("heap_commands", "heap의 push·peek·pop", "(operations: list[tuple[str, int | None]]) -> list[int | None]:",
           "빈 min heap에서 push, peek, pop을 순서대로 처리하세요. push에는 정수, 나머지에는 None이 주어집니다. peek와 pop 결과만 기록하고 빈 heap이면 None입니다. 입력은 보존합니다.", "힙 API의 조회와 제거 구분",
           "__FN__([('push', 3), ('push', 1), ('peek', None), ('pop', None), ('peek', None)]) == [1, 1, 3]", "__FN__([]) == []", "__FN__([('pop', None), ('push', 0), ('pop', None), ('pop', None)]) == [None, 0, None]", "heapq_call", time_cap=240),
    782: D("bisect_subrange", "bisect의 lo·hi 경계", "(values: list[int], target: int, low: int, high: int) -> tuple[int, int]:",
           "values는 오름차순이며 0<=low<=high<=len(values)입니다. bisect_left/right의 lo=low, hi=high를 사용한 두 삽입 인덱스를 반환하세요. 결과는 원본 기준 절대 인덱스입니다. 입력은 보존합니다.", "반열린 검색 구간과 절대 인덱스",
           "__FN__([1, 2, 2, 2, 5], 2, 2, 4) == (2, 4)", "__FN__([], 0, 0, 0) == (0, 0)", "__FN__([1, 3, 5], 0, 1, 3) == (1, 1)", "bisect_call", time_cap=180),
    783: D("insort_right_key", "key가 있는 insort_right", "(records: list[tuple[int, str]], incoming: tuple[int, str]) -> list[tuple[int, str]]:",
           "records는 첫 정수 필드 오름차순입니다. 사본에 bisect.insort_right(..., key=lambda item: item[0])로 incoming을 삽입하세요. 같은 key 그룹 뒤에 삽입하고 입력은 보존합니다.", "insort의 key와 동률 오른쪽 삽입",
           "__FN__([(1, 'b'), (1, 'a'), (3, 'x')], (1, 'z')) == [(1, 'b'), (1, 'a'), (1, 'z'), (3, 'x')]", "__FN__([], (0, 'a')) == [(0, 'a')]", "__FN__([(2, 'x')], (1, 'y')) == [(1, 'y'), (2, 'x')]", "bisect_call", "lambda", time_cap=240),
    784: D("bisect_remove_all", "bisect 범위로 같은 값 제거", "(values: list[int], target: int) -> list[int]:",
           "오름차순 values에서 bisect_left/right로 target 구간을 찾고 사본의 그 슬라이스를 삭제한 리스트를 반환하세요. 입력은 보존합니다.", "좌우 경계와 슬라이스 삭제",
           "__FN__([1, 2, 2, 3], 2) == [1, 3]", "__FN__([], 1) == []", "__FN__([1, 3], 2) == [1, 3]", "bisect_call", "slice", time_cap=180),
    785: D("bisect_ceiling_queries", "bisect_left로 이상 값 조회", "(values: list[int], queries: list[int]) -> list[int | None]:",
           "values는 오름차순입니다. 각 query에 bisect_left를 적용해 query 이상인 첫 값을 반환하고 없으면 None을 넣으세요. 질의 순서와 입력은 보존합니다.", "삽입 위치와 len 경계",
           "__FN__([1, 3, 3, 7], [0, 3, 4, 8]) == [1, 3, 7, None]", "__FN__([], [1]) == [None]", "__FN__([0], [0, -1]) == [0, 0]", "bisect_call", time_cap=180),
    786: D("bisect_record_key", "bisect key의 적용 대상", "(records: list[tuple[int, str]], target: int) -> str | None:",
           "records는 첫 정수 필드 오름차순입니다. bisect_left(records, target, key=lambda item: item[0])로 같은 key의 첫 문자열을 반환하고 없으면 None입니다. target은 tuple이 아닌 정수이며 입력은 보존합니다.", "bisect와 insort의 key 적용 차이",
           "__FN__([(1, 'x'), (2, 'b'), (2, 'a')], 2) == 'b'", "__FN__([], 2) is None", "__FN__([(1, 'x'), (3, 'y')], 2) is None", "bisect_call", "lambda", time_cap=240),
    787: D("bisect_three_slices", "작은·같은·큰 값 슬라이스", "(values: list[int], target: int) -> tuple[list[int], list[int], list[int]]:",
           "오름차순 values에서 bisect_left/right와 슬라이스로 (target 미만, 같은 값, 초과) 세 새 리스트를 반환하세요. 입력은 보존합니다.", "경계 인덱스를 출력 구간으로 변환",
           "__FN__([1, 2, 2, 4], 2) == ([1], [2, 2], [4])", "__FN__([], 1) == ([], [], [])", "__FN__([1, 3], 2) == ([1], [], [3])", "bisect_call", "slice", time_cap=180),
}


def _with_input_preservation(expression: str) -> str:
    """Check mutable literal inputs in the third example; first two stay readable."""
    class PreserveInputs(ast.NodeTransformer):
        counter = 0

        def visit_Call(self, node: ast.Call) -> ast.expr:
            if not isinstance(node.func, ast.Name) or node.func.id != "__FN__":
                return self.generic_visit(node)
            mutable = [i for i, arg in enumerate(node.args) if isinstance(arg, (ast.List, ast.Dict, ast.Set))]
            if not mutable:
                return node
            self.counter += 1
            prefix = f"_practice_{self.counter}"
            names = [f"{prefix}_{i}" for i in range(len(node.args))]
            pieces = [f"({name} := {ast.unparse(arg)})" for name, arg in zip(names, node.args)]
            values = "(" + ", ".join(names[i] for i in mutable) + ",)"
            pieces += [f"({prefix}_before := repr({values}))",
                       f"({prefix}_result := __FN__({', '.join(names)}))",
                       f"({prefix}_result if repr({values}) == {prefix}_before else object())"]
            return ast.parse("(" + ", ".join(pieces) + ")[-1]", mode="eval").body

    return ast.unparse(PreserveInputs().visit(ast.parse(expression, mode="eval")))


REPLACEMENTS = {
    number: replace(template, tests=(template.tests[0], template.tests[1],
                    template.tests[2] if number in IN_PLACE_IDS else _with_input_preservation(template.tests[2])))
    for number, template in REPLACEMENTS.items()
}
