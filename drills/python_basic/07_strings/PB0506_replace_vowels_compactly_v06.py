"""
PB0506 — 모음을 기호로 바꾸기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
대소문자 모음을 한 글자인 mask로 바꾸고 나머지 글자는 유지한다.

연습 초점
---------
조건 표현식을 포함한 generator와 join을 사용한다.

구현할 함수
-----------
def mask_vowels(text: str, mask: str) -> str:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- mask_vowels('Apple', '*') == '*ppl*'
- mask_vowels('sky', '?') == 'sky'
- mask_vowels('AE', '-') == '--'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0506 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mask_vowels(text: str, mask: str) -> str:
    raise NotImplementedError("TODO: PB0506")


def self_test() -> None:
    assert mask_vowels('Apple', '*') == '*ppl*'
    assert mask_vowels('sky', '?') == 'sky'
    assert mask_vowels('AE', '-') == '--'
