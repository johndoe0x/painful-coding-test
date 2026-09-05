"""
PB0165 — 직사각형 수치

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
직사각형의 넓이와 둘레를 (area, perimeter)로 반환하세요.

연습 초점
---------
곱셈·덧셈으로 도형 공식 표현

구현할 함수
-----------
def rectangle_arithmetic(width: int, height: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- rectangle_arithmetic(3, 4) == (12, 14)
- rectangle_arithmetic(0, 5) == (0, 10)
- rectangle_arithmetic(1, 1) == (1, 4)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0165 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rectangle_arithmetic(width: int, height: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0165")


def self_test() -> None:
    assert rectangle_arithmetic(3, 4) == (12, 14)
    assert rectangle_arithmetic(0, 5) == (0, 10)
    assert rectangle_arithmetic(1, 1) == (1, 4)
