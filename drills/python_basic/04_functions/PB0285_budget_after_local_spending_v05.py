"""
PB0285 — 지역 예산 차감

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
지역 remaining에 budget을 복사해 모든 비용을 차감한 값을 반환한다.

연습 초점
---------
지역 누적 변수로 입력값 보존

구현할 함수
-----------
def budget_after_local_spending(budget: float, costs: list[float]) -> float:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- budget_after_local_spending(20.0, [3.5, 4.5]) == 12.0
- budget_after_local_spending(0.0, []) == 0.0
- budget_after_local_spending(5.0, [8.0]) == -3.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0285 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def budget_after_local_spending(budget: float, costs: list[float]) -> float:
    raise NotImplementedError("TODO: PB0285")


def self_test() -> None:
    assert budget_after_local_spending(20.0, [3.5, 4.5]) == 12.0
    assert budget_after_local_spending(0.0, []) == 0.0
    assert budget_after_local_spending(5.0, [8.0]) == -3.0
