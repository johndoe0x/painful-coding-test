"""
PB0169 — 이차식 계산

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
a*x*x + b*x + c의 값을 반환하세요.

연습 초점
---------
여러 산술 연산이 섞인 식

구현할 함수
-----------
def evaluate_quadratic(a: int, b: int, c: int, x: int) -> int:

예시 및 필수 테스트
-------------------
- evaluate_quadratic(1, 2, 3, 2) == 11
- evaluate_quadratic(0, 0, 0, 5) == 0
- evaluate_quadratic(1, 0, 0, -3) == 9

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0169 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def evaluate_quadratic(a: int, b: int, c: int, x: int) -> int:
    raise NotImplementedError("TODO: PB0169")


def self_test() -> None:
    assert evaluate_quadratic(1, 2, 3, 2) == 11
    assert evaluate_quadratic(0, 0, 0, 5) == 0
    assert evaluate_quadratic(1, 0, 0, -3) == 9
