"""
PB0560 — 일정 간격의 글자 교체하기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
n이 양수이고 replacement가 한 글자라고 가정해 1부터 셌을 때 n번째마다 해당 글자를 교체한다.

연습 초점
---------
원본을 직접 고치지 않고 위치 조건으로 새 문자열을 생성한다.

구현할 함수
-----------
def replace_every_nth_character(text: str, n: int, replacement: str) -> str:

예시 및 필수 테스트
-------------------
- replace_every_nth_character('abcdefgh', 3, '*') == 'ab*de*gh'
- replace_every_nth_character('abc', 1, '-') == '---'
- replace_every_nth_character('', 2, '?') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0560 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_every_nth_character(text: str, n: int, replacement: str) -> str:
    raise NotImplementedError("TODO: PB0560")


def self_test() -> None:
    assert replace_every_nth_character('abcdefgh', 3, '*') == 'ab*de*gh'
    assert replace_every_nth_character('abc', 1, '-') == '---'
    assert replace_every_nth_character('', 2, '?') == ''
