"""
CI0366 — 스택 → 트리 최장 경로

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 06 / 20
Time cap: 720 seconds
Source checks:

문제
----
최대 200개 nodes[i]=(값,왼쪽,오른쪽), -1은 null이며 root 도달 영역은 정상 이진 트리입니다. 임의의 두 도달 노드 사이 최장 단순 경로의 간선 수를 반환하세요. 경로가 root를 지날 필요는 없습니다. 빈/단일 노드 트리는 0, 입력은 보존합니다.

연습 초점
---------
서브트리 높이와 루트를 지나지 않는 지름

구현할 함수
-----------
def stack_queue_bridge_tree_diameter(nodes: list[tuple[int, int, int]], root: int) -> int:

예시 및 필수 테스트
-------------------
- stack_queue_bridge_tree_diameter([], -1) == 0 and stack_queue_bridge_tree_diameter([(1, -1, -1)], 0) == 0
- stack_queue_bridge_tree_diameter([(1, 1, 2), (2, 3, 4), (3, -1, -1), (4, -1, -1), (5, -1, -1)], 0) == 3
- ((_bridge_1_arg_0 := [(0, 1, -1), (1, 2, 3), (2, 4, -1), (3, -1, 5), (4, -1, -1), (5, -1, -1)]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_diameter(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 4

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0366 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_bridge_tree_diameter(nodes: list[tuple[int, int, int]], root: int) -> int:
    raise NotImplementedError("TODO: CI0366")


def self_test() -> None:
    assert stack_queue_bridge_tree_diameter([], -1) == 0 and stack_queue_bridge_tree_diameter([(1, -1, -1)], 0) == 0
    assert stack_queue_bridge_tree_diameter([(1, 1, 2), (2, 3, 4), (3, -1, -1), (4, -1, -1), (5, -1, -1)], 0) == 3
    assert ((_bridge_1_arg_0 := [(0, 1, -1), (1, 2, 3), (2, 4, -1), (3, -1, 5), (4, -1, -1), (5, -1, -1)]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_diameter(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 4
