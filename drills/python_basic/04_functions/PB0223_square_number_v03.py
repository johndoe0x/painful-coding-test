"""
PB0223 — 제곱 계산 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
정수의 제곱을 반환한다.

연습 초점
---------
짧은 순수 함수 작성

구현할 함수
-----------
def square_number(number: int) -> int:

예시 및 필수 테스트
-------------------
- square_number(5) == 25
- square_number(0) == 0
- square_number(-3) == 9

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0223 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def square_number(number: int) -> int:
    raise NotImplementedError("TODO: PB0223")


def self_test() -> None:
    assert square_number(5) == 25
    assert square_number(0) == 0
    assert square_number(-3) == 9
