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
    "Introduction": "01_introduction",
    "Variables": "02_variables",
    "Math": "03_math",
    "Functions": "04_functions",
    "Conditional Statements": "05_conditionals",
    "Loops": "06_loops",
    "Strings": "07_strings",
    "Lists": "08_lists",
    "Sets": "09_sets",
    "Dictionaries": "10_dictionaries",
    "Reading Stdin": "11_reading_stdin",
    "Exception Handling": "12_exception_handling",
}


SEEDS = [
    Seed("Introduction", "Hello, World", "hello_world", "def make_message() -> str:", "정확히 'Hello, world!'를 반환한다.", "make_message() == 'Hello, world!'"),
    Seed("Introduction", "What is Python?", "what_is_python", "def python_summary() -> dict[str, str]:", "Python의 이름과 동적 타입 특성을 딕셔너리로 반환한다.", "python_summary() == {'language': 'Python', 'typing': 'dynamic'}"),
    Seed("Introduction", "Execution Order", "execution_order", "def execution_trace(values: list[int]) -> list[str]:", "start, 각 값의 처리 기록, end 순서로 실행 흔적을 만든다.", "execution_trace([2, 4]) == ['start', 'value=2', 'value=4', 'end']"),
    Seed("Introduction", "Printing Text", "printing_text", "def format_greeting(name: str) -> str:", "이름을 받아 'Hello, <name>!' 형식으로 반환한다.", "format_greeting('Devan') == 'Hello, Devan!'"),
    Seed("Introduction", "Code Errors", "code_errors", "def normalize_number(text: str) -> int:", "앞뒤 공백이 있는 정수 문자열을 올바른 int로 변환한다.", "normalize_number(' 42 ') == 42"),
    Seed("Introduction", "Comments", "comments", "def calculate_subtotal(prices: list[float]) -> float:", "가격 합계를 반환하고 계산 이유를 설명하는 유용한 주석 한 줄을 작성한다.", "calculate_subtotal([1.5, 2.0]) == 3.5"),
    Seed("Variables", "Variable Declaration", "variable_declaration", "def build_profile(name: str, age: int) -> dict[str, object]:", "입력값을 명확한 변수에 담아 프로필 딕셔너리를 반환한다.", "build_profile('Ada', 36) == {'name': 'Ada', 'age': 36}"),
    Seed("Variables", "Variable Naming", "variable_naming", "def join_name(first_name: str, last_name: str) -> str:", "의미 있는 변수명을 사용해 전체 이름을 만든다.", "join_name('Ada', 'Lovelace') == 'Ada Lovelace'"),
    Seed("Variables", "Naming Conventions", "naming_conventions", "def to_snake_case(words: list[str]) -> str:", "단어들을 소문자 snake_case 식별자로 결합한다.", "to_snake_case(['First', 'User', 'Name']) == 'first_user_name'"),
    Seed("Variables", "Reassigning Variables", "reassigning_variables", "def running_total(start: int, changes: list[int]) -> int:", "하나의 total 변수를 재할당하며 모든 변화를 적용한다.", "running_total(10, [3, -2, 5]) == 16"),
    Seed("Variables", "Multiple Assignments", "multiple_assignments", "def rotate_three(a: object, b: object, c: object) -> tuple[object, object, object]:", "다중 할당으로 a,b,c를 왼쪽으로 회전한다.", "rotate_three(1, 2, 3) == (2, 3, 1)"),
    Seed("Variables", "Variable Types", "variable_types", "def classify_value(value: object) -> str:", "bool, int, float, str, list, dict, None을 올바른 이름으로 분류한다.", "classify_value(True) == 'bool'; classify_value(3) == 'int'"),
    Seed("Variables", "Dynamic Typing", "dynamic_typing", "def type_history(values: list[object]) -> list[str]:", "값마다 런타임 타입 이름을 순서대로 반환한다.", "type_history([1, '1', 1.0]) == ['int', 'str', 'float']"),
    Seed("Variables", "Type Casting", "type_casting", "def convert_fields(age_text: str, score_text: str) -> tuple[int, float]:", "문자열 필드를 int와 float로 변환한다.", "convert_fields('21', '98.5') == (21, 98.5)"),
    Seed("Variables", "Type Errors", "type_errors", "def add_numeric_strings(left: str, right: str) -> int:", "문자열 연결이 아니라 숫자 덧셈을 수행한다.", "add_numeric_strings('10', '5') == 15"),
    Seed("Variables", "Empty Variable", "empty_variable", "def optional_label(label: str | None) -> str:", "None 또는 빈 문자열이면 'unknown'을 반환한다.", "optional_label(None) == 'unknown'; optional_label('x') == 'x'"),
    Seed("Math", "Arithmetic Operators", "arithmetic_operators", "def arithmetic_report(a: int, b: int) -> dict[str, int]:", "+, -, *, //, % 결과를 딕셔너리로 반환한다.", "arithmetic_report(7, 3) == {'add': 10, 'sub': 4, 'mul': 21, 'floordiv': 2, 'mod': 1}"),
    Seed("Math", "More Operators", "more_operators", "def power_and_division(a: int, b: int) -> tuple[int, float]:", "거듭제곱과 실수 나눗셈 결과를 반환한다.", "power_and_division(8, 2) == (64, 4.0)"),
    Seed("Math", "Shorthand Operators", "shorthand_operators", "def apply_changes(start: int, changes: list[int]) -> int:", "+= 연산으로 변화를 누적한다.", "apply_changes(5, [1, 2, -3]) == 5"),
    Seed("Math", "Boolean OR", "boolean_or", "def any_permission(is_admin: bool, is_owner: bool) -> bool:", "둘 중 하나라도 참이면 접근을 허용한다.", "any_permission(False, True) is True"),
    Seed("Math", "Boolean AND", "boolean_and", "def all_requirements(age_ok: bool, consent_ok: bool) -> bool:", "두 조건이 모두 참일 때만 True를 반환한다.", "all_requirements(True, False) is False"),
    Seed("Math", "Boolean Negation", "boolean_negation", "def toggle(flag: bool) -> bool:", "논리 부정으로 값을 반전한다.", "toggle(True) is False"),
    Seed("Functions", "Introduction to Functions", "functions_intro", "def double(number: int) -> int:", "입력을 두 배로 반환하는 순수 함수를 작성한다.", "double(7) == 14"),
    Seed("Functions", "Function Declaration", "function_declaration", "def rectangle_area(width: float, height: float) -> float:", "직사각형 넓이를 반환한다.", "rectangle_area(3, 4) == 12"),
    Seed("Functions", "Parameters", "parameters", "def repeat_text(text: str, count: int) -> str:", "문자열을 count번 반복한다.", "repeat_text('ab', 3) == 'ababab'"),
    Seed("Functions", "Multiple Parameters", "multiple_parameters", "def weighted_sum(a: float, b: float, weight: float) -> float:", "a*weight + b*(1-weight)를 반환한다.", "weighted_sum(10, 20, 0.25) == 17.5"),
    Seed("Functions", "Return Statement", "return_statement", "def min_max(numbers: list[int]) -> tuple[int, int]:", "최솟값과 최댓값을 tuple로 반환한다.", "min_max([3, 1, 8]) == (1, 8)"),
    Seed("Functions", "Type Hints", "type_hints", "def average(numbers: list[float]) -> float:", "타입 힌트를 유지하며 평균을 반환한다.", "average([2.0, 4.0]) == 3.0"),
    Seed("Functions", "Scope", "scope", "def count_local_updates(values: list[int]) -> int:", "전역 상태 없이 함수 내부 변수만으로 양수 개수를 센다.", "count_local_updates([-1, 2, 3]) == 2"),
    Seed("Functions", "Global vs Local Scope", "global_vs_local", "def shadow_value(value: int) -> tuple[int, int]:", "원본 값과 지역 변수로 변경한 값을 함께 반환한다.", "shadow_value(5) == (5, 6)"),
    Seed("Functions", "Default Arguments", "default_arguments", "def greet(name: str, prefix: str = 'Hello') -> str:", "기본 인자를 사용해 인사말을 만든다.", "greet('Ada') == 'Hello, Ada'; greet('Ada', 'Hi') == 'Hi, Ada'"),
    Seed("Conditional Statements", "Comparison Operators", "comparison_operators", "def compare_numbers(a: int, b: int) -> str:", "a가 b보다 작음·같음·큼을 문자열로 반환한다.", "compare_numbers(2, 5) == 'less'"),
    Seed("Conditional Statements", "If Statements", "if_statements", "def positive_label(number: int) -> str:", "양수면 'positive', 아니면 빈 문자열을 반환한다.", "positive_label(3) == 'positive'; positive_label(0) == ''"),
    Seed("Conditional Statements", "If Statement Scope", "if_scope", "def shipping_fee(total: float) -> float:", "total이 50 이상이면 0, 아니면 5를 반환한다.", "shipping_fee(50) == 0; shipping_fee(10) == 5"),
    Seed("Conditional Statements", "If-Else Statements", "if_else", "def parity(number: int) -> str:", "짝수면 even, 홀수면 odd를 반환한다.", "parity(7) == 'odd'"),
    Seed("Conditional Statements", "Else-If Statements", "elif_statements", "def grade(score: int) -> str:", "90/80/70/60 경계로 A/B/C/D/F를 반환한다.", "grade(85) == 'B'"),
    Seed("Conditional Statements", "Logic Condition", "logic_condition", "def eligible(age: int, has_id: bool, banned: bool) -> bool:", "성인이고 신분증이 있으며 차단되지 않은 경우만 허용한다.", "eligible(20, True, False) is True"),
    Seed("Conditional Statements", "Truthy and Falsy", "truthy_falsy", "def fallback(value: object, default: object) -> object:", "value가 truthy면 value, 아니면 default를 반환한다.", "fallback('', 'n/a') == 'n/a'"),
    Seed("Loops", "While Loops", "while_loops", "def countdown(start: int) -> list[int]:", "while로 start부터 1까지 감소하는 리스트를 만든다.", "countdown(3) == [3, 2, 1]"),
    Seed("Loops", "While Loops Counting", "while_counting", "def sum_to_n(n: int) -> int:", "while로 1부터 n까지 합한다.", "sum_to_n(4) == 10"),
    Seed("Loops", "While Loops Multiples", "while_multiples", "def multiples(limit: int, base: int) -> list[int]:", "limit 이하의 양의 base 배수를 while로 만든다.", "multiples(10, 3) == [3, 6, 9]"),
    Seed("Loops", "For Loops", "for_loops", "def square_all(numbers: list[int]) -> list[int]:", "for로 각 숫자의 제곱 리스트를 만든다.", "square_all([1, 3]) == [1, 9]"),
    Seed("Loops", "For Loops Start", "for_loops_start", "def range_from_to(start: int, stop: int) -> list[int]:", "range(start, stop)을 리스트로 반환한다.", "range_from_to(2, 5) == [2, 3, 4]"),
    Seed("Loops", "For Loops Step", "for_loops_step", "def stepped_range(start: int, stop: int, step: int) -> list[int]:", "step을 적용한 range를 만든다.", "stepped_range(1, 8, 3) == [1, 4, 7]"),
    Seed("Loops", "For Loops Reverse", "for_loops_reverse", "def reverse_indices(length: int) -> list[int]:", "length-1부터 0까지의 인덱스를 만든다.", "reverse_indices(4) == [3, 2, 1, 0]"),
    Seed("Loops", "Nested Loops", "nested_loops", "def multiplication_table(size: int) -> list[list[int]]:", "중첩 loop로 size x size 곱셈표를 만든다.", "multiplication_table(2) == [[1, 2], [2, 4]]"),
    Seed("Loops", "Control Flow", "control_flow", "def filter_until_zero(numbers: list[int]) -> list[int]:", "0에서 중단하고 그전 양수만 continue/break를 사용해 모은다.", "filter_until_zero([-1, 2, 3, 0, 4]) == [2, 3]"),
    Seed("Strings", "Length Function", "string_length", "def string_length(text: str) -> int:", "문자열 길이를 반환한다.", "string_length('python') == 6"),
    Seed("Strings", "String Indexing", "string_indexing", "def first_last(text: str) -> tuple[str, str]:", "비어 있지 않은 문자열의 첫 글자와 마지막 글자를 반환한다.", "first_last('code') == ('c', 'e')"),
    Seed("Strings", "String Looping", "string_looping", "def char_codes(text: str) -> list[int]:", "문자를 순회해 ord 값 리스트를 만든다.", "char_codes('AB') == [65, 66]"),
    Seed("Strings", "String Looping Shorthand", "string_looping_shorthand", "def count_vowels(text: str) -> int:", "문자열을 직접 순회해 모음 개수를 센다.", "count_vowels('Apple') == 2"),
    Seed("Strings", "String Concatenation", "string_concatenation", "def join_words(words: list[str], separator: str) -> str:", "구분자로 단어를 결합한다.", "join_words(['a', 'b'], '-') == 'a-b'"),
    Seed("Strings", "String Slicing Part 1", "string_slicing_1", "def prefix_suffix(text: str, size: int) -> tuple[str, str]:", "앞 size글자와 뒤 size글자를 반환한다.", "prefix_suffix('python', 2) == ('py', 'on')"),
    Seed("Strings", "String Slicing Part 2", "string_slicing_2", "def every_other(text: str) -> str:", "0번 인덱스부터 한 글자씩 건너뛴 문자열을 반환한다.", "every_other('abcdef') == 'ace'"),
    Seed("Strings", "Reversing a String", "reverse_string", "def reverse_text(text: str) -> str:", "슬라이싱으로 문자열을 뒤집는다.", "reverse_text('abc') == 'cba'"),
    Seed("Strings", "Strings are Immutable", "strings_immutable", "def replace_character(text: str, index: int, replacement: str) -> str:", "원본을 직접 수정하지 않고 새 문자열을 만든다.", "replace_character('cat', 0, 'b') == 'bat'"),
    Seed("Strings", "Strings Formatting", "string_formatting", "def format_receipt(item: str, quantity: int, price: float) -> str:", "f-string으로 영수증 한 줄을 만든다.", "format_receipt('pen', 2, 1.5) == 'pen x2 = 3.00'"),
    Seed("Lists", "Intro to Lists", "intro_lists", "def make_list(first: object, second: object, third: object) -> list[object]:", "세 값을 순서대로 담은 리스트를 만든다.", "make_list(1, 'a', True) == [1, 'a', True]"),
    Seed("Lists", "List Operations", "list_operations", "def update_at(values: list[int], index: int, value: int) -> list[int]:", "원본을 복사한 뒤 지정 위치를 바꿔 반환한다.", "update_at([1, 2, 3], 1, 9) == [1, 9, 3]"),
    Seed("Lists", "List Looping", "list_looping", "def sum_list(values: list[int]) -> int:", "for loop로 합계를 계산한다.", "sum_list([2, 3, 4]) == 9"),
    Seed("Lists", "List Functions", "list_functions", "def list_stats(values: list[int]) -> dict[str, int]:", "len, min, max, sum 결과를 반환한다.", "list_stats([2, 5]) == {'len': 2, 'min': 2, 'max': 5, 'sum': 7}"),
    Seed("Lists", "List Append", "list_append", "def append_if_missing(values: list[int], value: int) -> list[int]:", "값이 없을 때만 복사본 끝에 추가한다.", "append_if_missing([1, 2], 3) == [1, 2, 3]"),
    Seed("Lists", "List Pop", "list_pop", "def pop_last(values: list[int]) -> tuple[list[int], int | None]:", "복사본의 마지막 값을 제거해 리스트와 제거값을 반환한다.", "pop_last([1, 2]) == ([1], 2); pop_last([]) == ([], None)"),
    Seed("Lists", "List Find", "list_find", "def find_index(values: list[object], target: object) -> int:", "target의 첫 인덱스를 반환하고 없으면 -1을 반환한다.", "find_index(['a', 'b'], 'b') == 1"),
    Seed("Lists", "List Slicing", "list_slicing", "def middle_slice(values: list[int]) -> list[int]:", "첫 값과 마지막 값을 제외한 슬라이스를 반환한다.", "middle_slice([1, 2, 3, 4]) == [2, 3]"),
    Seed("Lists", "Tuples", "tuples", "def swap_pair(pair: tuple[object, object]) -> tuple[object, object]:", "두 원소의 순서를 바꾼 tuple을 반환한다.", "swap_pair(('a', 1)) == (1, 'a')"),
    Seed("Sets", "Intro to Sets", "intro_sets", "def unique_values(values: list[int]) -> set[int]:", "리스트를 set으로 변환한다.", "unique_values([1, 1, 2]) == {1, 2}"),
    Seed("Sets", "Set Operations", "set_operations", "def set_report(left: set[int], right: set[int]) -> dict[str, set[int]]:", "합집합·교집합·차집합을 반환한다.", "set_report({1, 2}, {2, 3})['intersection'] == {2}"),
    Seed("Sets", "Set Practice", "set_practice", "def dedupe_preserve_order(values: list[int]) -> list[int]:", "set을 사용하되 최초 등장 순서를 보존해 중복을 제거한다.", "dedupe_preserve_order([2, 1, 2, 3]) == [2, 1, 3]"),
    Seed("Dictionaries", "Intro to Dictionaries", "intro_dicts", "def make_user(name: str, age: int) -> dict[str, object]:", "name과 age를 가진 딕셔너리를 만든다.", "make_user('Ada', 36) == {'name': 'Ada', 'age': 36}"),
    Seed("Dictionaries", "Dict Operations", "dict_operations", "def upsert(mapping: dict[str, int], key: str, value: int) -> dict[str, int]:", "복사본에 key-value를 추가하거나 갱신한다.", "upsert({'a': 1}, 'a', 2) == {'a': 2}"),
    Seed("Dictionaries", "Dict Looping", "dict_looping", "def invert_dict(mapping: dict[str, int]) -> dict[int, str]:", "items를 순회해 key와 value를 뒤집는다.", "invert_dict({'a': 1}) == {1: 'a'}"),
    Seed("Dictionaries", "Dict Practice", "dict_practice", "def frequency(values: list[str]) -> dict[str, int]:", "각 문자열의 빈도를 딕셔너리로 센다.", "frequency(['a', 'b', 'a']) == {'a': 2, 'b': 1}"),
    Seed("Dictionaries", "Dict Remove", "dict_remove", "def remove_keys(mapping: dict[str, int], keys: list[str]) -> dict[str, int]:", "복사본에서 존재하는 키만 안전하게 제거한다.", "remove_keys({'a': 1, 'b': 2}, ['a', 'x']) == {'b': 2}"),
    Seed("Dictionaries", "Dict Values", "dict_values", "def sum_values(mapping: dict[str, int]) -> int:", "values를 사용해 합계를 반환한다.", "sum_values({'a': 2, 'b': 3}) == 5"),
    Seed("Reading Stdin", "Reading Input", "reading_input", "def normalize_line(line: str) -> str:", "입력 한 줄의 앞뒤 공백과 줄바꿈을 제거한다.", "normalize_line('  hello\\n') == 'hello'"),
    Seed("Reading Stdin", "Type Conversion with Input", "input_type_conversion", "def parse_int(text: str) -> int:", "입력 문자열을 정수로 변환한다.", "parse_int(' 12 ') == 12"),
    Seed("Reading Stdin", "Parse Input", "parse_input", "def parse_int_list(line: str) -> list[int]:", "공백으로 구분된 정수들을 리스트로 파싱한다.", "parse_int_list('1 2 3') == [1, 2, 3]"),
    Seed("Reading Stdin", "Read Input Practice", "input_practice", "def parse_record(line: str) -> tuple[str, int, bool]:", "'name age active' 한 줄을 str,int,bool로 파싱한다.", "parse_record('Ada 36 true') == ('Ada', 36, True)"),
    Seed("Exception Handling", "Try Except", "try_except", "def to_int_or_default(text: str, default: int = 0) -> int:", "정수 변환 실패 시 default를 반환한다.", "to_int_or_default('x', 7) == 7"),
    Seed("Exception Handling", "Error Catching", "error_catching", "def safe_index(values: list[object], index: int) -> object | None:", "IndexError를 처리해 잘못된 인덱스면 None을 반환한다.", "safe_index([1], 2) is None"),
    Seed("Exception Handling", "Multiple Except Blocks", "multiple_except", "def parse_ratio(left: str, right: str) -> float | None:", "ValueError와 ZeroDivisionError를 별도 except로 처리하고 실패 시 None을 반환한다.", "parse_ratio('6', '2') == 3.0; parse_ratio('x', '2') is None"),
]


VARIANTS = [
    ("baseline", "기본형", "기본 목표를 그대로 구현하고 예시를 통과시킨다.", 90),
    ("changed_values", "값 변경형", "예시와 다른 값 세 개를 직접 추가하고 일반화된 구현을 확인한다.", 90),
    ("input_form", "입력형", "함수 구현 후 main()에서 표준입력 한 줄을 읽어 함수를 호출한다.", 90),
    ("output_form", "출력형", "동일한 핵심 로직을 유지하되 결과를 명시된 반환값으로만 제공한다.", 90),
    ("fill_blank", "빈칸 완성형", "핵심 표현식 한 줄을 먼저 주석으로 설명한 뒤 구현한다.", 90),
    ("bug_fix", "버그 수정형", "흔한 오류를 드러내는 실패 테스트 두 개를 먼저 적고 올바른 구현을 작성한다.", 90),
    ("predict_build", "예측 후 구현형", "예시 실행 결과를 주석으로 먼저 예측한 뒤 구현하고 확인한다.", 90),
    ("edge_cases", "경계조건형", "빈 값·경계값·중복값 중 적용 가능한 세 가지를 테스트한다.", 90),
    ("combined", "결합형", "직전 seed의 개념을 헬퍼 함수 또는 추가 처리 단계로 결합한다.", 120),
    ("blind_speed", "블라인드 속도형", "설명 재열람 없이 제한시간 안에 구현하고 자체 테스트 두 개를 실행한다.", 120),
]


def function_name(signature: str) -> str:
    match = re.search(r"def\s+([a-zA-Z_][a-zA-Z0-9_]*)", signature)
    if match is None:
        raise ValueError(f"invalid signature: {signature}")
    return match.group(1)


def render_problem(seed: Seed, seed_number: int, variant_number: int, problem_id: int) -> str:
    variant_slug, variant_name, variant_instruction, time_cap = VARIANTS[variant_number - 1]
    previous = SEEDS[seed_number - 2].title if seed_number > 1 else "Printing Text"
    if variant_number == 9:
        variant_instruction = f"'{previous}' 개념을 헬퍼 함수 또는 추가 처리 단계로 결합한다."

    main_stub = ""
    if variant_number == 3:
        main_stub = textwrap.dedent(
            """


            def main() -> None:
                # TODO: 표준입력을 읽고 위 함수를 호출해 결과를 출력하세요.
                raise NotImplementedError("TODO: input variant")
            """
        ).rstrip()

    docstring = textwrap.dedent(
        f'''\
        """
        PB{problem_id:04d} — {seed.title} / {variant_name}

        Chapter: {seed.chapter}
        Seed: {seed_number:02d} / 82
        Variant: {variant_number:02d} / 10
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
        1. 빈 화면에서 직접 구현한다.
        2. 예시와 자체 테스트를 통과한다.
        3. 답안을 보며 타이핑한 코드는 완료로 세지 않는다.
        4. 마지막에는 NotImplementedError를 제거한다.
        """
        '''
    )

    starter = f"{seed.signature}\n    raise NotImplementedError(\"TODO: PB{problem_id:04d}\")"
    return f"{docstring}\n\n{starter}{main_stub}\n"


def main() -> None:
    raise SystemExit(
        "generate_bank.py는 초기 생성 전용으로 비활성화되었습니다. "
        "답안을 보존하는 regenerate_problems.py를 사용하세요."
    )


def legacy_main() -> None:
    if len(SEEDS) != 82:
        raise RuntimeError(f"expected 82 seeds, found {len(SEEDS)}")

    for directory in CHAPTERS.values():
        chapter_dir = ROOT / directory
        chapter_dir.mkdir(parents=True, exist_ok=True)
        for old_problem in chapter_dir.glob("PB*.py"):
            old_problem.unlink()

    index_lines = [
        "# Python Basic 820 Problem Index",
        "",
        "82개 seed × 10개 변형 = 820개 문제입니다.",
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
            filename = f"PB{problem_id:04d}_{seed.slug}_v{variant_number:02d}_{variant_slug}.py"
            path = chapter_dir / filename
            path.write_text(
                render_problem(seed, seed_number, variant_number, problem_id),
                encoding="utf-8",
            )
            relative = path.relative_to(ROOT)
            index_lines.append(
                f"- [PB{problem_id:04d} — {seed.title} / {variant_name}]({relative.as_posix()})"
            )
            chapter_counts[seed.chapter] += 1

        index_lines.append("")

    if problem_id != 820:
        raise RuntimeError(f"expected 820 problems, generated {problem_id}")

    (ROOT / "INDEX.md").write_text("\n".join(index_lines).rstrip() + "\n", encoding="utf-8")
    print(f"generated={problem_id}")
    for chapter, count in chapter_counts.items():
        print(f"{CHAPTERS[chapter]}={count}")


if __name__ == "__main__":
    main()
