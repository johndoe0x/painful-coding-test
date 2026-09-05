"""
PB0145 — 문자열 나눗셈

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 문자열을 float로 변환해 나누세요. denominator는 0이 아닙니다.

연습 초점
---------
지원되지 않는 str 나눗셈 수정

구현할 함수
-----------
def divide_number_texts(numerator: str, denominator: str) -> float:

예시 및 필수 테스트
-------------------
- divide_number_texts('9', '2') == 4.5
- divide_number_texts('0', '3') == 0.0
- divide_number_texts('-6', '2') == -3.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0145 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def divide_number_texts(numerator: str, denominator: str) -> float:
    raise NotImplementedError("TODO: PB0145")


def self_test() -> None:
    assert divide_number_texts('9', '2') == 4.5
    assert divide_number_texts('0', '3') == 0.0
    assert divide_number_texts('-6', '2') == -3.0
