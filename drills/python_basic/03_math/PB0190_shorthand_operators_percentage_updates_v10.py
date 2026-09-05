"""
PB0190 — 비율 복합 적용

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
value에 각 multiplier를 *=로 순서대로 적용하세요.

연습 초점
---------
실수 상태의 *= 갱신

구현할 함수
-----------
def apply_multipliers(value: float, multipliers: list[float]) -> float:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- apply_multipliers(100, [1.25, 0.5]) == 62.5
- apply_multipliers(0, [2]) == 0
- apply_multipliers(7, []) == 7

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0190 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_multipliers(value: float, multipliers: list[float]) -> float:
    raise NotImplementedError("TODO: PB0190")


def self_test() -> None:
    assert apply_multipliers(100, [1.25, 0.5]) == 62.5
    assert apply_multipliers(0, [2]) == 0
    assert apply_multipliers(7, []) == 7
