"""
PB0185 — **=로 거듭제곱

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
각 exponent에 대해 value **= exponent를 순서대로 적용하세요.

연습 초점
---------
**= 복합 할당

구현할 함수
-----------
def apply_exponents(start: int, exponents: list[int]) -> int:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- apply_exponents(2, [3, 2]) == 64
- apply_exponents(0, [2]) == 0
- apply_exponents(5, []) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0185 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_exponents(start: int, exponents: list[int]) -> int:
    raise NotImplementedError("TODO: PB0185")


def self_test() -> None:
    assert apply_exponents(2, [3, 2]) == 64
    assert apply_exponents(0, [2]) == 0
    assert apply_exponents(5, []) == 5
