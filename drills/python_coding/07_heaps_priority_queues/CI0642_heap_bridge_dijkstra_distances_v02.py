"""
CI0642 — 힙 → 비음수 가중 최단 거리

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 02 / 20
Time cap: 900 seconds
Source checks:

문제
----
1<=n<=100 정점, 최대 1000개 유향 간선 (u,v,w), 0<=w<=1000과 유효 source가 주어집니다. source부터 최소 가중치 합을 정점 순서로 반환하세요. 도달 불가는 None, 자기 자신은 0입니다. 중복/자기 간선을 허용하고 입력은 보존합니다.

연습 초점
---------
다익스트라 완화와 오래된 힙 항목 무시

구현할 함수
-----------
def heap_bridge_dijkstra_distances(n: int, edges: list[tuple[int, int, int]], source: int) -> list[int | None]:

예시 및 필수 테스트
-------------------
- heap_bridge_dijkstra_distances(1, [], 0) == [0]
- heap_bridge_dijkstra_distances(4, [(0, 1, 10), (0, 2, 1), (2, 1, 2)], 0) == [0, 3, 1, None]
- ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 5), (0, 1, 0), (1, 2, 0), (2, 1, 0)]), (_bridge_1_arg_2 := 0), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_dijkstra_distances(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == [0, 0, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0642 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_dijkstra_distances(n: int, edges: list[tuple[int, int, int]], source: int) -> list[int | None]:
    raise NotImplementedError("TODO: CI0642")


def self_test() -> None:
    assert heap_bridge_dijkstra_distances(1, [], 0) == [0]
    assert heap_bridge_dijkstra_distances(4, [(0, 1, 10), (0, 2, 1), (2, 1, 2)], 0) == [0, 3, 1, None]
    assert ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 5), (0, 1, 0), (1, 2, 0), (2, 1, 0)]), (_bridge_1_arg_2 := 0), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_dijkstra_distances(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] == [0, 0, 0]
