"""
PB0240 — 일수를 시간으로

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
일수를 24시간 단위로 변환한다.

연습 초점
---------
작은 변환 함수를 선언하고 호출

구현할 함수
-----------
def days_to_hours(days: int) -> int:

예시 및 필수 테스트
-------------------
- days_to_hours(3) == 72
- days_to_hours(0) == 0
- days_to_hours(365) == 8760

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0240 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def days_to_hours(days: int) -> int:
    raise NotImplementedError("TODO: PB0240")


def self_test() -> None:
    assert days_to_hours(3) == 72
    assert days_to_hours(0) == 0
    assert days_to_hours(365) == 8760
