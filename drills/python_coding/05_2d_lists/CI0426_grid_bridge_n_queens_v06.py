"""
CI0426 — 격자 → N-Queen 배치 열 목록

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 06 / 20
Time cap: 1200 seconds
Source checks:

문제
----
0<=n<=8입니다. n*n 보드에 서로 공격하지 않는 퀸 n개를 놓는 모든 배치를 반환하세요. 각 tuple의 r번째 값은 r행 퀸의 열 인덱스입니다. 결과는 tuple 사전순, 중복 없이, n=0이면 [()]입니다.

연습 초점
---------
열과 두 대각선 집합을 사용하는 백트래킹

구현할 함수
-----------
def grid_bridge_n_queens(n: int) -> list[tuple[int, ...]]:

예시 및 필수 테스트
-------------------
- grid_bridge_n_queens(0) == [()] and grid_bridge_n_queens(1) == [(0,)]
- grid_bridge_n_queens(2) == [] and grid_bridge_n_queens(3) == []
- grid_bridge_n_queens(4) == [(1, 3, 0, 2), (2, 0, 3, 1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0426 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_bridge_n_queens(n: int) -> list[tuple[int, ...]]:
    raise NotImplementedError("TODO: CI0426")


def self_test() -> None:
    assert grid_bridge_n_queens(0) == [()] and grid_bridge_n_queens(1) == [(0,)]
    assert grid_bridge_n_queens(2) == [] and grid_bridge_n_queens(3) == []
    assert grid_bridge_n_queens(4) == [(1, 3, 0, 2), (2, 0, 3, 1)]
