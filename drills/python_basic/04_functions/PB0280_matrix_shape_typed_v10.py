"""
PB0280 — 행렬 크기 반환

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 행의 길이가 같은 직사각형 matrix만 입력됩니다. 빈 행렬은 (0, 0), 아니면 (행 수, 첫 행의 열 수)를 반환한다.

연습 초점
---------
직사각형 중첩 입력과 tuple 반환 타입 표기

구현할 함수
-----------
def matrix_shape_typed(matrix: list[list[float]]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- matrix_shape_typed([[1.0, 2.0], [3.0, 4.0]]) == (2, 2)
- matrix_shape_typed([]) == (0, 0)
- matrix_shape_typed([[]]) == (1, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0280 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def matrix_shape_typed(matrix: list[list[float]]) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0280")


def self_test() -> None:
    assert matrix_shape_typed([[1.0, 2.0], [3.0, 4.0]]) == (2, 2)
    assert matrix_shape_typed([]) == (0, 0)
    assert matrix_shape_typed([[]]) == (1, 0)
