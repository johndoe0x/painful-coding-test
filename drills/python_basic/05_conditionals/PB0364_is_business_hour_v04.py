"""
PB0364 — 영업 시간 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
평일이고 공휴일이 아니며 hour가 9 이상 18 미만일 때 True를 반환한다.

연습 초점
---------
범위·불리언 부정 조건 결합

구현할 함수
-----------
def is_business_hour(hour: int, is_weekend: bool, is_holiday: bool) -> bool:

예시 및 필수 테스트
-------------------
- is_business_hour(9, False, False) is True
- is_business_hour(18, False, False) is False
- is_business_hour(12, True, False) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0364 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_business_hour(hour: int, is_weekend: bool, is_holiday: bool) -> bool:
    raise NotImplementedError("TODO: PB0364")


def self_test() -> None:
    assert is_business_hour(9, False, False) is True
    assert is_business_hour(18, False, False) is False
    assert is_business_hour(12, True, False) is False
