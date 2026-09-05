"""
CI0459 — 격자 최단 거리 — 반복 세트 3

Chapter: 2-D Lists
Seed: 23 / 40
Variant: 19 / 20
Time cap: 240 seconds
Source checks: deque_call

문제
----
0은 통과 가능, 1은 벽인 직사각형에서 좌상단부터 우하단까지 4방향 최소 이동 수를 BFS로 반환하고 불가능하면 -1입니다. 이 파일은 2-D Lists 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
deque 기반 최단 경로

구현할 함수
-----------
def grid_r03_shortest_grid_path(grid: list[list[int]]) -> int:

필수 구현 방식
--------------
- collections.deque를 사용한다.

예시 및 필수 테스트
-------------------
- grid_r03_shortest_grid_path([[0, 0], [1, 0]]) == 2
- grid_r03_shortest_grid_path([[0, 1], [1, 0]]) == -1
- grid_r03_shortest_grid_path([[0]]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0459 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r03_shortest_grid_path(grid: list[list[int]]) -> int:
    raise NotImplementedError("TODO: CI0459")


def self_test() -> None:
    assert grid_r03_shortest_grid_path([[0, 0], [1, 0]]) == 2
    assert grid_r03_shortest_grid_path([[0, 1], [1, 0]]) == -1
    assert grid_r03_shortest_grid_path([[0]]) == 0
