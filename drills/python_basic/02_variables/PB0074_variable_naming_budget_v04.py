"""
PB0074 — 남은 예산

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
초기 예산에서 사용 금액을 빼 남은 예산을 반환하세요.

연습 초점
---------
계산 방향을 드러내는 변수명

구현할 함수
-----------
def calculate_remaining_budget(initial_budget: float, amount_spent: float) -> float:

예시 및 필수 테스트
-------------------
- calculate_remaining_budget(100, 30) == 70
- calculate_remaining_budget(0, 0) == 0
- calculate_remaining_budget(50, 75) == -25

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0074 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_remaining_budget(initial_budget: float, amount_spent: float) -> float:
    raise NotImplementedError("TODO: PB0074")


def self_test() -> None:
    assert calculate_remaining_budget(100, 30) == 70
    assert calculate_remaining_budget(0, 0) == 0
    assert calculate_remaining_budget(50, 75) == -25
