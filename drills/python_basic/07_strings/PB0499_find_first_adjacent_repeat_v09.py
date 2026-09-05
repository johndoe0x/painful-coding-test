"""
PB0499 — 처음 연속으로 반복된 글자

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: for

문제
----
같은 글자가 연속으로 나온 첫 위치의 글자를 반환하고 없으면 None을 반환한다.

연습 초점
---------
이전 글자와 현재 글자를 반복 중 비교하고 첫 일치에서 멈춘다.

구현할 함수
-----------
def first_adjacent_repeat(text: str) -> str | None:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- first_adjacent_repeat('bookkeeper') == 'o'
- first_adjacent_repeat('abc') is None
- first_adjacent_repeat('aa') == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0499 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_adjacent_repeat(text: str) -> str | None:
    raise NotImplementedError("TODO: PB0499")


def self_test() -> None:
    assert first_adjacent_repeat('bookkeeper') == 'o'
    assert first_adjacent_repeat('abc') is None
    assert first_adjacent_repeat('aa') == 'a'
