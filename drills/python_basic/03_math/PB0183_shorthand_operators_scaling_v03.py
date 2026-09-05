"""
PB0183 — /=로 연속 축소

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
각 0이 아닌 divisor로 value를 /= 하여 반환하세요.

연습 초점
---------
/= 복합 할당

구현할 함수
-----------
def divide_by_factors(start: float, divisors: list[float]) -> float:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- divide_by_factors(100, [2, 5]) == 10.0
- divide_by_factors(0, [2]) == 0.0
- divide_by_factors(7, []) == 7

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0183 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def divide_by_factors(start: float, divisors: list[float]) -> float:
    raise NotImplementedError("TODO: PB0183")


def self_test() -> None:
    assert divide_by_factors(100, [2, 5]) == 10.0
    assert divide_by_factors(0, [2]) == 0.0
    assert divide_by_factors(7, []) == 7
