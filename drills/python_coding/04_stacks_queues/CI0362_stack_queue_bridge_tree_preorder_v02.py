"""
CI0362 — 스택 → 이진 트리 전위 순회

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 02 / 20
Time cap: 480 seconds
Source checks:

문제
----
최대 200개 nodes[i]=(값,왼쪽 인덱스,오른쪽 인덱스), -1은 null입니다. root 도달 영역은 공유 자식/사이클 없는 이진 트리입니다. 루트-왼쪽-오른쪽 순서로 값을 반환하세요. root=-1이면 [], 비도달 노드는 무시하며 입력은 보존합니다.

연습 초점
---------
스택의 역순 push와 트리 순회

구현할 함수
-----------
def stack_queue_bridge_tree_preorder(nodes: list[tuple[int, int, int]], root: int) -> list[int]:

예시 및 필수 테스트
-------------------
- stack_queue_bridge_tree_preorder([], -1) == [] and stack_queue_bridge_tree_preorder([(4, -1, -1)], 0) == [4]
- stack_queue_bridge_tree_preorder([(1, 1, 2), (2, -1, -1), (3, -1, -1)], 0) == [1, 2, 3]
- ((_bridge_1_arg_0 := [(8, -1, -1), (5, 2, 0), (6, -1, -1)]), (_bridge_1_arg_1 := 1), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_preorder(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [5, 6, 8]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0362 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_bridge_tree_preorder(nodes: list[tuple[int, int, int]], root: int) -> list[int]:
    raise NotImplementedError("TODO: CI0362")


def self_test() -> None:
    assert stack_queue_bridge_tree_preorder([], -1) == [] and stack_queue_bridge_tree_preorder([(4, -1, -1)], 0) == [4]
    assert stack_queue_bridge_tree_preorder([(1, 1, 2), (2, -1, -1), (3, -1, -1)], 0) == [1, 2, 3]
    assert ((_bridge_1_arg_0 := [(8, -1, -1), (5, 2, 0), (6, -1, -1)]), (_bridge_1_arg_1 := 1), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_preorder(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [5, 6, 8]
