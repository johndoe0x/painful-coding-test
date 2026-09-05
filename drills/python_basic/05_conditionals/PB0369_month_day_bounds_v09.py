"""
PB0369 — 월·일 숫자 범위 확인

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
실제 달력 유효성은 판단하지 않고 month가 1~12이고 day가 1~31인 숫자 범위 안이면 True를 반환한다.

연습 초점
---------
서로 다른 값의 단순 범위 조건 결합

구현할 함수
-----------
def within_month_day_bounds(month: int, day: int) -> bool:

예시 및 필수 테스트
-------------------
- within_month_day_bounds(1, 1) is True
- within_month_day_bounds(2, 31) is True
- within_month_day_bounds(13, 1) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0369 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def within_month_day_bounds(month: int, day: int) -> bool:
    raise NotImplementedError("TODO: PB0369")


def self_test() -> None:
    assert within_month_day_bounds(1, 1) is True
    assert within_month_day_bounds(2, 31) is True
    assert within_month_day_bounds(13, 1) is False
