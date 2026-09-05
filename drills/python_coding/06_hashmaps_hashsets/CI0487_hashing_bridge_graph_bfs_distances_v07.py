"""
CI0487 — 해시맵 → 유향 그래프 최단 거리

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 07 / 20
Time cap: 600 seconds
Source checks:

문제
----
1<=n<=200 정점, 최대 1000개 유향 간선과 유효 source가 주어집니다. source에서 각 정점까지 최소 간선 수를 정점 순서로 반환하세요. 자기 자신은 0, 도달 불가는 -1입니다. 중복/자기 간선 허용, 간선을 역방향으로 해석하지 말고 입력은 보존합니다.

연습 초점
---------
첫 발견 시점의 BFS 거리 확정

구현할 함수
-----------
def hashing_bridge_graph_bfs_distances(n: int, edges: list[tuple[int, int]], source: int) -> list[int]:

예시 및 필수 테스트
-------------------
- hashing_bridge_graph_bfs_distances(1, [], 0) == [0]
- hashing_bridge_graph_bfs_distances(5, [(0, 1), (1, 2), (0, 2), (2, 3)], 0) == [0, 1, 1, 2, -1]
- ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1), (1, 1), (0, 1)]), (_bridge_1_arg_2 := 1), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := hashing_bridge_graph_bfs_distances(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == [-1, 0, -1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0487 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_bridge_graph_bfs_distances(n: int, edges: list[tuple[int, int]], source: int) -> list[int]:
    raise NotImplementedError("TODO: CI0487")


def self_test() -> None:
    assert hashing_bridge_graph_bfs_distances(1, [], 0) == [0]
    assert hashing_bridge_graph_bfs_distances(5, [(0, 1), (1, 2), (0, 2), (2, 3)], 0) == [0, 1, 1, 2, -1]
    assert ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1), (1, 1), (0, 1)]), (_bridge_1_arg_2 := 1), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := hashing_bridge_graph_bfs_distances(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == [-1, 0, -1]
