"""
PB0134 — 숫자 문자 리스트

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 문자가 숫자인 text의 각 문자를 int 리스트로 변환하세요. 빈 문자열은 빈 리스트입니다.

연습 초점
---------
문자 단위 정수 캐스팅

구현할 함수
-----------
def cast_digit_characters(text: str) -> list[int]:

예시 및 필수 테스트
-------------------
- cast_digit_characters('205') == [2, 0, 5]
- cast_digit_characters('') == []
- cast_digit_characters('0') == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0134 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_digit_characters(text: str) -> list[int]:
    raise NotImplementedError("TODO: PB0134")


def self_test() -> None:
    assert cast_digit_characters('205') == [2, 0, 5]
    assert cast_digit_characters('') == []
    assert cast_digit_characters('0') == [0]
