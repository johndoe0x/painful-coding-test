from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import textwrap


ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Seed:
    chapter: str
    title: str
    slug: str
    signature: str
    task: str
    example: str


CHAPTERS = {
    "Sorting": "01_sorting",
    "Pythonic Code": "02_pythonic_code",
    "Lists": "03_lists",
    "Stacks and Queues": "04_stacks_queues",
    "2-D Lists": "05_2d_lists",
    "Hashmaps and Hashsets": "06_hashmaps_hashsets",
    "Heaps / Priority Queues": "07_heaps_priority_queues",
    "Sorted Dicts and Sorted Sets": "08_sorted_dicts_sets",
}


SEEDS = [
    Seed("Sorting", "Sort Ascending", "sort_ascending", "def sort_ascending(values: list[int]) -> list[int]:", "원본을 보존하면서 숫자를 오름차순으로 정렬한 새 리스트를 반환한다.", "sort_ascending([3, 1, 2]) == [1, 2, 3]"),
    Seed("Sorting", "Sort Descending", "sort_descending", "def sort_descending(values: list[int]) -> list[int]:", "원본을 보존하면서 숫자를 내림차순으로 정렬한다.", "sort_descending([3, 1, 2]) == [3, 2, 1]"),
    Seed("Sorting", "Sort Custom", "sort_custom", "def sort_words(words: list[str]) -> list[str]:", "문자열을 길이, 그다음 사전순으로 정렬한다.", "sort_words(['bb', 'a', 'ab']) == ['a', 'ab', 'bb']"),
    Seed("Sorting", "Sort Lambda", "sort_lambda", "def sort_people(people: list[tuple[str, int]]) -> list[tuple[str, int]]:", "사람을 나이 오름차순, 이름 오름차순으로 lambda key를 사용해 정렬한다.", "sort_people([('B', 20), ('A', 20), ('C', 18)]) == [('C', 18), ('A', 20), ('B', 20)]"),
    Seed("Sorting", "Sorted Copy", "sorted_copy", "def sorted_copy(values: list[int]) -> tuple[list[int], list[int]]:", "원본을 바꾸지 않고 정렬본과 원본 사본을 함께 반환한다.", "sorted_copy([2, 1]) == ([1, 2], [2, 1])"),
    Seed("Pythonic Code", "Unpacking", "unpacking", "def swap_and_sum(pair: tuple[int, int]) -> tuple[int, int, int]:", "tuple unpacking으로 두 값을 교환하고 합계도 반환한다.", "swap_and_sum((2, 5)) == (5, 2, 7)"),
    Seed("Pythonic Code", "Loop Unpacking", "loop_unpacking", "def sum_products(pairs: list[tuple[int, int]]) -> int:", "for 문에서 tuple을 직접 unpack해 각 곱의 합을 구한다.", "sum_products([(2, 3), (4, 5)]) == 26"),
    Seed("Pythonic Code", "Enumerate", "enumerate", "def indexed_labels(values: list[str]) -> list[str]:", "enumerate로 'index:value' 문자열을 만든다.", "indexed_labels(['a', 'b']) == ['0:a', '1:b']"),
    Seed("Pythonic Code", "Zip", "zip", "def pair_columns(names: list[str], scores: list[int]) -> list[tuple[str, int]]:", "zip으로 두 열을 짝지으며 짧은 쪽 길이에 맞춘다.", "pair_columns(['A', 'B'], [10, 20, 30]) == [('A', 10), ('B', 20)]"),
    Seed("Pythonic Code", "Inequality", "inequality", "def outside_range(value: int, low: int, high: int) -> bool:", "연쇄 비교와 논리 부정으로 닫힌 구간 밖인지 판정한다.", "outside_range(5, 1, 4) is True"),
    Seed("Pythonic Code", "Min Max Shortcut", "min_max_shortcut", "def clamp(value: int, low: int, high: int) -> int:", "min과 max를 조합해 값을 구간 안으로 제한한다.", "clamp(12, 0, 10) == 10"),
    Seed("Lists", "Resizable List Part 1", "resizable_list_1", "def append_sequence(start: list[int], additions: list[int]) -> list[int]:", "원본 사본에 additions를 순서대로 append한다.", "append_sequence([1], [2, 3]) == [1, 2, 3]"),
    Seed("Lists", "Resizable List Part 2", "resizable_list_2", "def insert_and_remove(values: list[int], index: int, new_value: int) -> list[int]:", "사본의 index에 값을 삽입한 뒤 첫 번째 음수를 제거한다.", "insert_and_remove([1, -1, 3], 1, 2) == [1, 2, 3]"),
    Seed("Lists", "List Concat", "list_concat", "def concat_lists(left: list[int], right: list[int]) -> list[int]:", "두 리스트를 원본 변경 없이 결합한다.", "concat_lists([1, 2], [3]) == [1, 2, 3]"),
    Seed("Lists", "List Initialization", "list_initialization", "def repeat_value(value: object, count: int) -> list[object]:", "독립적인 count개 슬롯을 가진 리스트를 만든다.", "repeat_value('x', 3) == ['x', 'x', 'x']"),
    Seed("Lists", "List Clone", "list_clone", "def clone_and_update(values: list[int], index: int, value: int) -> tuple[list[int], list[int]]:", "shallow copy를 수정하고 수정본과 원본을 반환한다.", "clone_and_update([1, 2], 0, 9) == ([9, 2], [1, 2])"),
    Seed("Lists", "List Comprehension", "list_comprehension", "def even_squares(values: list[int]) -> list[int]:", "comprehension으로 짝수의 제곱만 반환한다.", "even_squares([1, 2, 3, 4]) == [4, 16]"),
    Seed("Stacks and Queues", "Stack Push and Pop", "stack_push_pop", "def process_stack(operations: list[tuple[str, int | None]]) -> list[int]:", "list를 stack으로 사용해 push/pop 연산의 pop 결과를 반환한다.", "process_stack([('push', 2), ('push', 3), ('pop', None)]) == [3]"),
    Seed("Stacks and Queues", "Queue Enqueue and Dequeue", "queue_enqueue_dequeue", "def process_queue(operations: list[tuple[str, int | None]]) -> list[int]:", "collections.deque로 enqueue/dequeue를 처리한다.", "process_queue([('enqueue', 2), ('enqueue', 3), ('dequeue', None)]) == [2]"),
    Seed("Stacks and Queues", "Double Ended Queue", "double_ended_queue", "def rotate_window(values: list[int], steps: int) -> list[int]:", "deque.rotate를 사용해 오른쪽으로 steps만큼 회전한다.", "rotate_window([1, 2, 3], 1) == [3, 1, 2]"),
    Seed("2-D Lists", "Multi-Dimensional List", "multi_dimensional_list", "def matrix_shape(matrix: list[list[object]]) -> tuple[int, int]:", "직사각형 행렬의 행과 열 수를 반환하고 빈 행렬은 (0,0)으로 처리한다.", "matrix_shape([[1, 2], [3, 4]]) == (2, 2)"),
    Seed("2-D Lists", "2D Grid", "grid_neighbors", "def orthogonal_neighbors(grid: list[list[int]], row: int, col: int) -> list[int]:", "상하좌우의 유효한 이웃 값을 정해진 순서로 반환한다.", "orthogonal_neighbors([[1, 2], [3, 4]], 0, 0) == [3, 2]"),
    Seed("2-D Lists", "Nested List Comprehension", "nested_list_comprehension", "def make_grid(rows: int, cols: int) -> list[list[int]]:", "중첩 comprehension으로 cell 값이 row+col인 격자를 만든다.", "make_grid(2, 3) == [[0, 1, 2], [1, 2, 3]]"),
    Seed("Hashmaps and Hashsets", "Hash Map Basics", "hash_map_basics", "def index_by_key(records: list[tuple[str, int]]) -> dict[str, int]:", "key가 반복되면 마지막 값을 유지하는 딕셔너리를 만든다.", "index_by_key([('a', 1), ('a', 2)]) == {'a': 2}"),
    Seed("Hashmaps and Hashsets", "Default Dict", "default_dict", "def group_words(words: list[str]) -> dict[str, list[str]]:", "defaultdict(list)로 첫 글자별 단어를 그룹화한다.", "group_words(['ant', 'apple', 'bee']) == {'a': ['ant', 'apple'], 'b': ['bee']}"),
    Seed("Hashmaps and Hashsets", "Counter", "counter", "def most_common_value(values: list[str]) -> tuple[str, int] | None:", "Counter로 최빈값과 빈도를 반환하며 동률이면 사전순 최소를 선택한다.", "most_common_value(['b', 'a', 'b']) == ('b', 2)"),
    Seed("Hashmaps and Hashsets", "Dict Comprehension", "dict_comprehension", "def square_map(values: list[int]) -> dict[int, int]:", "dict comprehension으로 값과 제곱을 매핑한다.", "square_map([2, 3]) == {2: 4, 3: 9}"),
    Seed("Hashmaps and Hashsets", "Dict Items", "dict_items", "def filter_mapping(mapping: dict[str, int], minimum: int) -> dict[str, int]:", "items를 순회해 minimum 이상 값만 남긴다.", "filter_mapping({'a': 1, 'b': 3}, 2) == {'b': 3}"),
    Seed("Hashmaps and Hashsets", "Hash Set Basics", "hash_set_basics", "def has_duplicate(values: list[int]) -> bool:", "set을 사용해 중복 존재 여부를 O(n)에 판정한다.", "has_duplicate([1, 2, 1]) is True"),
    Seed("Hashmaps and Hashsets", "Set Comprehension", "set_comprehension", "def unique_lengths(words: list[str]) -> set[int]:", "set comprehension으로 서로 다른 문자열 길이를 만든다.", "unique_lengths(['a', 'bb', 'cc']) == {1, 2}"),
    Seed("Hashmaps and Hashsets", "Tuple Keys", "tuple_keys", "def count_coordinates(points: list[tuple[int, int]]) -> dict[tuple[int, int], int]:", "좌표 tuple을 key로 사용해 빈도를 센다.", "count_coordinates([(0, 0), (0, 0), (1, 2)]) == {(0, 0): 2, (1, 2): 1}"),
    Seed("Heaps / Priority Queues", "Heap Push", "heap_push", "def running_minimum(values: list[int]) -> list[int]:", "heapq.heappush를 사용해 각 삽입 뒤 최솟값을 기록한다.", "running_minimum([3, 1, 2]) == [3, 1, 1]"),
    Seed("Heaps / Priority Queues", "Heap Pop", "heap_pop", "def pop_sorted(values: list[int]) -> list[int]:", "heap에서 모두 pop해 오름차순 결과를 만든다.", "pop_sorted([3, 1, 2]) == [1, 2, 3]"),
    Seed("Heaps / Priority Queues", "Heapify", "heapify", "def smallest_after_heapify(values: list[int]) -> int | None:", "사본을 heapify하고 최솟값을 반환한다.", "smallest_after_heapify([4, 2, 3]) == 2"),
    Seed("Heaps / Priority Queues", "Max Heap", "max_heap", "def top_k_largest(values: list[int], k: int) -> list[int]:", "음수 변환 max heap으로 큰 값 k개를 내림차순 반환한다.", "top_k_largest([3, 1, 5, 2], 2) == [5, 3]"),
    Seed("Heaps / Priority Queues", "Custom Heap", "custom_heap", "def schedule_tasks(tasks: list[tuple[int, str]]) -> list[str]:", "priority가 작을수록 먼저, 동률이면 이름순으로 처리한다.", "schedule_tasks([(2, 'b'), (1, 'c'), (1, 'a')]) == ['a', 'c', 'b']"),
    Seed("Heaps / Priority Queues", "Heap N Smallest", "heap_nsmallest", "def n_smallest(values: list[int], n: int) -> list[int]:", "heapq.nsmallest로 작은 값 n개를 반환한다.", "n_smallest([4, 1, 3, 2], 2) == [1, 2]"),
    Seed("Heaps / Priority Queues", "Heap N Largest", "heap_nlargest", "def n_largest(values: list[int], n: int) -> list[int]:", "heapq.nlargest로 큰 값 n개를 반환한다.", "n_largest([4, 1, 3, 2], 2) == [4, 3]"),
    Seed("Sorted Dicts and Sorted Sets", "Sorted Dict Basics", "sorted_dict_basics", "def sorted_items(mapping: dict[str, int]) -> list[tuple[str, int]]:", "key 오름차순으로 정렬된 items 리스트를 반환한다.", "sorted_items({'b': 2, 'a': 1}) == [('a', 1), ('b', 2)]"),
    Seed("Sorted Dicts and Sorted Sets", "Sorted Set Basics", "sorted_set_basics", "def sorted_unique(values: list[int]) -> list[int]:", "중복을 제거하고 오름차순 리스트로 반환한다.", "sorted_unique([3, 1, 3, 2]) == [1, 2, 3]"),
]


VARIANTS = [
    ("baseline", "기본 구현", "표준 요구사항을 빈 화면에서 구현하고 대표 테스트를 통과한다.", 150),
    ("reverse", "반대 동작", "정렬 방향·우선순위·처리 순서를 반대로 바꿔 구현한다.", 150),
    ("container_swap", "컨테이너 변경", "list·tuple·iterator 중 다른 입력 형태를 받아도 처리하게 한다.", 150),
    ("return_shape", "반환 형태 변경", "단일 값·인덱스·쌍·리스트 중 다른 반환 형태로 확장한다.", 150),
    ("empty_input", "빈 입력", "빈 입력에서 예외 없이 명확한 결과를 반환한다.", 150),
    ("duplicates", "중복 입력", "중복이 많은 입력에서도 의미와 복잡도를 유지한다.", 150),
    ("negative_bounds", "음수·경계값", "음수·큰 값·경계 인덱스를 포함한 테스트를 통과한다.", 150),
    ("bug_fix", "버그 수정", "off-by-one 또는 잘못된 API 사용을 드러내는 테스트를 먼저 작성하고 수정한다.", 150),
    ("trace", "실행 추적", "핵심 상태 변화를 최소 세 단계 주석으로 추적한 뒤 구현한다.", 150),
    ("speed", "속도 구현", "표준형을 설명 재열람 없이 제한시간 안에 구현한다.", 180),
    ("helper_function", "헬퍼 함수", "핵심 로직을 이름이 분명한 헬퍼 함수로 분리한다.", 180),
    ("loop_comprehension", "Loop·Comprehension", "loop 구현과 comprehension 구현을 서로 변환하고 결과를 비교한다.", 180),
    ("inplace_copy", "In-place·Copy", "원본 변경형과 복사본 반환형을 각각 작성하고 차이를 테스트한다.", 180),
    ("tie_break", "동률 처리", "값이 같을 때 두 번째 기준으로 안정적으로 순서를 결정한다.", 180),
    ("second_structure", "두 자료구조 결합", "두 번째 표준 자료구조를 결합해 기능을 확장한다.", 240),
    ("memory_limit", "공간 제한", "불필요한 복사를 줄이고 추가 공간 사용을 설명한다.", 240),
    ("multiple_queries", "다중 쿼리", "하나의 입력 상태에 여러 쿼리를 효율적으로 처리한다.", 240),
    ("streaming_update", "스트리밍 갱신", "새 값이 하나씩 도착할 때 상태를 갱신하는 API로 바꾼다.", 240),
    ("self_tests", "자체 테스트", "정상·경계·실패 테스트를 직접 세 개 만든 뒤 구현한다.", 240),
    ("blind_mixed", "블라인드 혼합", "관련 Python 기능 두 개 이상을 결합해 제한시간 안에 구현한다.", 300),
]


def render_problem(seed: Seed, seed_number: int, variant_number: int, problem_id: int) -> str:
    variant_slug, variant_name, variant_instruction, time_cap = VARIANTS[variant_number - 1]
    previous = SEEDS[seed_number - 2].title if seed_number > 1 else "Sorted Copy"
    if variant_number == 15:
        variant_instruction = f"'{previous}'에서 사용한 Python 기능 또는 자료구조를 함께 사용해 기능을 확장한다."

    docstring = textwrap.dedent(
        f'''\
        """
        CI{problem_id:04d} — {seed.title} / {variant_name}

        Chapter: {seed.chapter}
        Seed: {seed_number:02d} / 40
        Variant: {variant_number:02d} / 20
        Time cap: {time_cap} seconds

        기본 목표
        ---------
        {seed.task}

        이번 변형
        ---------
        {variant_instruction}

        예시
        ----
        {seed.example}

        완료 조건
        ---------
        1. 필요한 표준 라이브러리 import를 기억에서 직접 작성한다.
        2. 예시와 자체 테스트를 통과한다.
        3. 시간·공간복잡도를 마지막 주석에 적는다.
        4. 답안을 보며 타이핑한 코드는 완료로 세지 않는다.
        5. 마지막에는 NotImplementedError를 제거한다.
        """
        '''
    )
    starter = f"{seed.signature}\n    raise NotImplementedError(\"TODO: CI{problem_id:04d}\")"
    return f"{docstring}\n\n{starter}\n"


def legacy_main() -> None:
    if len(SEEDS) != 40:
        raise RuntimeError(f"expected 40 seeds, found {len(SEEDS)}")

    for directory in CHAPTERS.values():
        chapter_dir = ROOT / directory
        chapter_dir.mkdir(parents=True, exist_ok=True)
        for old_problem in chapter_dir.glob("CI*.py"):
            old_problem.unlink()

    index_lines = [
        "# Python Coding Interview 800 Problem Index",
        "",
        "40개 seed × 20개 변형 = 800개 문제입니다.",
        "",
    ]
    problem_id = 0
    chapter_counts: dict[str, int] = {chapter: 0 for chapter in CHAPTERS}

    for seed_number, seed in enumerate(SEEDS, start=1):
        chapter_dir = ROOT / CHAPTERS[seed.chapter]
        if chapter_counts[seed.chapter] == 0:
            index_lines.extend([f"## {seed.chapter}", ""])

        for variant_number, (variant_slug, variant_name, _, _) in enumerate(VARIANTS, start=1):
            problem_id += 1
            filename = f"CI{problem_id:04d}_{seed.slug}_v{variant_number:02d}_{variant_slug}.py"
            path = chapter_dir / filename
            path.write_text(render_problem(seed, seed_number, variant_number, problem_id), encoding="utf-8")
            relative = path.relative_to(ROOT)
            index_lines.append(f"- [CI{problem_id:04d} — {seed.title} / {variant_name}]({relative.as_posix()})")
            chapter_counts[seed.chapter] += 1
        index_lines.append("")

    if problem_id != 800:
        raise RuntimeError(f"expected 800 problems, generated {problem_id}")

    (ROOT / "INDEX.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    print(f"generated={problem_id}")
    for chapter, count in chapter_counts.items():
        print(f"{CHAPTERS[chapter]}={count}")


def main() -> None:
    raise SystemExit(
        "generate_bank.py는 초기 저품질 생성기라 비활성화되었습니다. "
        "답안을 보존하는 regenerate_variants.py를 사용하세요."
    )


if __name__ == "__main__":
    main()
