"""
PB0566 — 고정 너비 표 한 줄

Chapter: Strings
Topic: Strings Formatting
Seed: 57 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: f_string

문제
----
label은 너비 10에 왼쪽 정렬하고 value는 너비 5에 오른쪽 정렬해 두 필드를 바로 이어 반환한다.

연습 초점
---------
문자열과 정수에 서로 다른 정렬·너비 형식 지정자를 적용한다.

구현할 함수
-----------
def format_fixed_width_row(label: str, value: int) -> str:

필수 구현 방식
--------------
- f-string을 사용한다.

예시 및 필수 테스트
-------------------
- format_fixed_width_row('apple', 42) == 'apple        42'
- format_fixed_width_row('x', 7) == 'x             7'
- format_fixed_width_row('abcdefghij', 12345) == 'abcdefghij12345'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0566 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_fixed_width_row(label: str, value: int) -> str:
    raise NotImplementedError("TODO: PB0566")


def self_test() -> None:
    assert format_fixed_width_row('apple', 42) == 'apple        42'
    assert format_fixed_width_row('x', 7) == 'x             7'
    assert format_fixed_width_row('abcdefghij', 12345) == 'abcdefghij12345'
