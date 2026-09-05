"""
PB0367 — 렌터카 대여 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
age가 21 이상이고 면허가 있으며 정지 상태가 아닐 때 True를 반환한다.

연습 초점
---------
필수 조건과 금지 조건 조합

구현할 함수
-----------
def can_rent_car(age: int, has_license: bool, suspended: bool) -> bool:

예시 및 필수 테스트
-------------------
- can_rent_car(21, True, False) is True
- can_rent_car(20, True, False) is False
- can_rent_car(30, True, True) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0367 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def can_rent_car(age: int, has_license: bool, suspended: bool) -> bool:
    raise NotImplementedError("TODO: PB0367")


def self_test() -> None:
    assert can_rent_car(21, True, False) is True
    assert can_rent_car(20, True, False) is False
    assert can_rent_car(30, True, True) is False
