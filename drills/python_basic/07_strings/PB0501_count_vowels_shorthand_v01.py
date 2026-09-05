"""
PB0501 — 모음 개수 세기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
대소문자를 구분하지 않고 a, e, i, o, u의 개수를 반환한다.

연습 초점
---------
문자열 직접 순회와 membership 조건을 짧은 표현으로 결합한다.

구현할 함수
-----------
def count_vowels(text: str) -> int:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- count_vowels('Apple') == 2
- count_vowels('rhythm') == 0
- count_vowels('AEIOU') == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0501 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_vowels(text: str) -> int:
    raise NotImplementedError("TODO: PB0501")


def self_test() -> None:
    assert count_vowels('Apple') == 2
    assert count_vowels('rhythm') == 0
    assert count_vowels('AEIOU') == 5
