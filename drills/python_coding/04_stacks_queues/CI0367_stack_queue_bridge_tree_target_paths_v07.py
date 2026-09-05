"""
CI0367 — 스택 → 목표 합 루트-리프 경로

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 07 / 20
Time cap: 720 seconds
Source checks:

문제
----
최대 200개 nodes[i]=(정수 값,왼쪽,오른쪽), -1은 null이며 root 도달 영역은 정상 이진 트리입니다. 값 합이 target인 루트부터 리프까지의 경로를 값 리스트로 반환하세요. 왼쪽 우선 DFS 순서이며 같은 값 경로도 노드 경로가 다르면 중복 보존합니다. 빈 트리는 [], 음수 허용, 입력은 보존합니다.

연습 초점
---------
백트래킹 경로 복사와 리프 종료 조건

구현할 함수
-----------
def stack_queue_bridge_tree_target_paths(nodes: list[tuple[int, int, int]], root: int, target: int) -> list[list[int]]:

예시 및 필수 테스트
-------------------
- stack_queue_bridge_tree_target_paths([], -1, 0) == [] and stack_queue_bridge_tree_target_paths([(0, -1, -1)], 0, 0) == [[0]]
- stack_queue_bridge_tree_target_paths([(1, 1, 2), (2, -1, -1), (2, -1, -1)], 0, 3) == [[1, 2], [1, 2]]
- ((_bridge_1_arg_0 := [(2, 1, -1), (-2, -1, -1)]), (_bridge_1_arg_1 := 0), (_bridge_1_arg_2 := 2), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_target_paths(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [] and ((_bridge_2_arg_0 := [(2, 1, -1), (-2, -1, -1)]), (_bridge_2_arg_1 := 0), (_bridge_2_arg_2 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := stack_queue_bridge_tree_target_paths(_bridge_2_arg_0, _bridge_2_arg_1, _bridge_2_arg_2)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == [[2, -2]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0367 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_bridge_tree_target_paths(nodes: list[tuple[int, int, int]], root: int, target: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0367")


def self_test() -> None:
    assert stack_queue_bridge_tree_target_paths([], -1, 0) == [] and stack_queue_bridge_tree_target_paths([(0, -1, -1)], 0, 0) == [[0]]
    assert stack_queue_bridge_tree_target_paths([(1, 1, 2), (2, -1, -1), (2, -1, -1)], 0, 3) == [[1, 2], [1, 2]]
    assert ((_bridge_1_arg_0 := [(2, 1, -1), (-2, -1, -1)]), (_bridge_1_arg_1 := 0), (_bridge_1_arg_2 := 2), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := stack_queue_bridge_tree_target_paths(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [] and ((_bridge_2_arg_0 := [(2, 1, -1), (-2, -1, -1)]), (_bridge_2_arg_1 := 0), (_bridge_2_arg_2 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := stack_queue_bridge_tree_target_paths(_bridge_2_arg_0, _bridge_2_arg_1, _bridge_2_arg_2)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == [[2, -2]]
