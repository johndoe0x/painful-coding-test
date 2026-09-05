"""
CI0442 — 행렬 shape — 반복 세트 3

Chapter: 2-D Lists
Seed: 23 / 40
Variant: 02 / 20
Time cap: 240 seconds
Source checks:

문제
----
직사각형 matrix의 (행 수, 열 수)를 반환하고 빈 행렬은 (0, 0)으로 처리하세요. 이 파일은 2-D Lists 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
2D 구조의 행·열 크기

구현할 함수
-----------
def grid_r03_matrix_shape(matrix: list[list[object]]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- grid_r03_matrix_shape([[1, 2], [3, 4]]) == (2, 2)
- grid_r03_matrix_shape([]) == (0, 0)
- grid_r03_matrix_shape([[]]) == (1, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0442 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r03_matrix_shape(matrix: list[list[object]]) -> tuple[int, int]:
    raise NotImplementedError("TODO: CI0442")


def self_test() -> None:
    assert grid_r03_matrix_shape([[1, 2], [3, 4]]) == (2, 2)
    assert grid_r03_matrix_shape([]) == (0, 0)
    assert grid_r03_matrix_shape([[]]) == (1, 0)
