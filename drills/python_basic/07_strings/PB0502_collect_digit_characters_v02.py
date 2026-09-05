"""
PB0502 — 숫자 글자만 모으기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
text에서 숫자인 글자만 원래 순서대로 이어 반환한다.

연습 초점
---------
조건부 컴프리헨션과 str.isdigit을 사용한다.

구현할 함수
-----------
def digit_characters(text: str) -> str:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- digit_characters('a1b2c3') == '123'
- digit_characters('no digits') == ''
- digit_characters('007') == '007'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0502 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def digit_characters(text: str) -> str:
    raise NotImplementedError("TODO: PB0502")


def self_test() -> None:
    assert digit_characters('a1b2c3') == '123'
    assert digit_characters('no digits') == ''
    assert digit_characters('007') == '007'
