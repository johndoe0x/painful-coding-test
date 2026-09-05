"""
PB0370 — 대출 사전 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
income이 30000 이상, credit_score가 700 이상이고 연체 이력이 없을 때 True를 반환한다.

연습 초점
---------
수치 기준과 부정 플래그 결합

구현할 함수
-----------
def loan_precheck(income: int, credit_score: int, has_default: bool) -> bool:

예시 및 필수 테스트
-------------------
- loan_precheck(30000, 700, False) is True
- loan_precheck(29999, 800, False) is False
- loan_precheck(50000, 750, True) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0370 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def loan_precheck(income: int, credit_score: int, has_default: bool) -> bool:
    raise NotImplementedError("TODO: PB0370")


def self_test() -> None:
    assert loan_precheck(30000, 700, False) is True
    assert loan_precheck(29999, 800, False) is False
    assert loan_precheck(50000, 750, True) is False
