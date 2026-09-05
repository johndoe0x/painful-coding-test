"""
CI0645 — 우선순위 → 최소 신장 트리

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 05 / 20
Time cap: 900 seconds
Source checks:

문제
----
0<=n<=100 정점, 최대 1000개 무방향 간선 (u,v,w), -1000<=w<=1000입니다. 모든 정점을 연결하는 최소 신장 트리의 가중치 합을 반환하세요. 연결 불가면 None, n=0 또는 1이면 0입니다. 중복 간선 허용, 자기 루프는 선택 불가, 입력은 보존합니다.

연습 초점
---------
간선 우선순위와 Union-Find 사이클 배제

구현할 함수
-----------
def heap_bridge_minimum_spanning_tree(n: int, edges: list[tuple[int, int, int]]) -> int | None:

예시 및 필수 테스트
-------------------
- heap_bridge_minimum_spanning_tree(0, []) == 0 and heap_bridge_minimum_spanning_tree(1, [(0, 0, -9)]) == 0
- heap_bridge_minimum_spanning_tree(3, [(0, 1, 5), (0, 2, 2), (1, 2, -1)]) == 1
- ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 1)]), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_minimum_spanning_tree(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] is None and ((_bridge_2_arg_0 := 2), (_bridge_2_arg_1 := [(0, 1, 5), (0, 1, 2)]), (_bridge_2_before := repr((_bridge_2_arg_1,))), (_bridge_2_result := heap_bridge_minimum_spanning_tree(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_1,)) == _bridge_2_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0645 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_minimum_spanning_tree(n: int, edges: list[tuple[int, int, int]]) -> int | None:
    raise NotImplementedError("TODO: CI0645")


def self_test() -> None:
    assert heap_bridge_minimum_spanning_tree(0, []) == 0 and heap_bridge_minimum_spanning_tree(1, [(0, 0, -9)]) == 0
    assert heap_bridge_minimum_spanning_tree(3, [(0, 1, 5), (0, 2, 2), (1, 2, -1)]) == 1
    assert ((_bridge_1_arg_0 := 3), (_bridge_1_arg_1 := [(0, 1, 1)]), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_minimum_spanning_tree(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] is None and ((_bridge_2_arg_0 := 2), (_bridge_2_arg_1 := [(0, 1, 5), (0, 1, 2)]), (_bridge_2_before := repr((_bridge_2_arg_1,))), (_bridge_2_result := heap_bridge_minimum_spanning_tree(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_1,)) == _bridge_2_before else object())[-1] == 2
