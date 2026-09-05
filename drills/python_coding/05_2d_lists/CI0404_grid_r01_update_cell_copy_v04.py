"""
CI0404 — 셀 변경 깊은 복사 — 반복 세트 1

Chapter: 2-D Lists
Seed: 21 / 40
Variant: 04 / 20
Time cap: 240 seconds
Source checks: comprehension

문제
----
모든 행을 복사한 새 행렬의 지정 셀만 바꾸고 원본은 보존하세요. 이 파일은 2-D Lists 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
중첩 리스트 독립 복사

구현할 함수
-----------
def grid_r01_update_cell_copy(matrix: list[list[int]], row: int, col: int, value: int) -> list[list[int]]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- grid_r01_update_cell_copy([[1, 2], [3, 4]], 0, 1, 9) == [[1, 9], [3, 4]]
- grid_r01_update_cell_copy([[1]], 0, 0, 0) == [[0]]
- ((grid := [[1, 2]]), grid_r01_update_cell_copy(grid, 0, 0, 7), grid) == ([[1, 2]], [[7, 2]], [[1, 2]])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0404 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r01_update_cell_copy(matrix: list[list[int]], row: int, col: int, value: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0404")


def self_test() -> None:
    assert grid_r01_update_cell_copy([[1, 2], [3, 4]], 0, 1, 9) == [[1, 9], [3, 4]]
    assert grid_r01_update_cell_copy([[1]], 0, 0, 0) == [[0]]
    assert ((grid := [[1, 2]]), grid_r01_update_cell_copy(grid, 0, 0, 7), grid) == ([[1, 2]], [[7, 2]], [[1, 2]])
