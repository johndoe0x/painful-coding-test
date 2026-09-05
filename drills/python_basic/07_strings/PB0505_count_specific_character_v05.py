"""
PB0505 — 특정 글자 세기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
target이 한 글자라고 가정하고 text에서 target과 같은 글자의 개수를 반환한다.

연습 초점
---------
불리언 조건을 정수로 합산하는 짧은 순회 표현을 연습한다.

구현할 함수
-----------
def count_character(text: str, target: str) -> int:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- count_character('banana', 'a') == 3
- count_character('banana', 'x') == 0
- count_character('', 'a') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0505 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_character(text: str, target: str) -> int:
    raise NotImplementedError("TODO: PB0505")


def self_test() -> None:
    assert count_character('banana', 'a') == 3
    assert count_character('banana', 'x') == 0
    assert count_character('', 'a') == 0
