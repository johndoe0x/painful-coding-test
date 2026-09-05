"""
PB0094 — 연속 성장률 적용

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
value를 각 소수 비율 rate만큼 차례로 증가시키며 재할당하세요.

연습 초점
---------
이전 결과를 다음 계산에 사용

구현할 함수
-----------
def apply_growth_rates(value: float, rates: list[float]) -> float:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- apply_growth_rates(100, [0.1, 0.2]) == 132.0
- apply_growth_rates(0, [0.5]) == 0.0
- apply_growth_rates(50, []) == 50

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0094 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_growth_rates(value: float, rates: list[float]) -> float:
    raise NotImplementedError("TODO: PB0094")


def self_test() -> None:
    assert apply_growth_rates(100, [0.1, 0.2]) == 132.0
    assert apply_growth_rates(0, [0.5]) == 0.0
    assert apply_growth_rates(50, []) == 50
