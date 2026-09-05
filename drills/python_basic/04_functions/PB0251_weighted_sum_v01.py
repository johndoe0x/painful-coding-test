"""
PB0251 — 가중 합계

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
a*weight + b*(1-weight)를 반환한다.

연습 초점
---------
여러 수치 매개변수로 하나의 공식 계산

구현할 함수
-----------
def weighted_sum(a: float, b: float, weight: float) -> float:

예시 및 필수 테스트
-------------------
- weighted_sum(10.0, 20.0, 0.25) == 17.5
- weighted_sum(5.0, 9.0, 1.0) == 5.0
- weighted_sum(-2.0, 2.0, 0.5) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0251 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def weighted_sum(a: float, b: float, weight: float) -> float:
    raise NotImplementedError("TODO: PB0251")


def self_test() -> None:
    assert weighted_sum(10.0, 20.0, 0.25) == 17.5
    assert weighted_sum(5.0, 9.0, 1.0) == 5.0
    assert weighted_sum(-2.0, 2.0, 0.5) == 0.0
