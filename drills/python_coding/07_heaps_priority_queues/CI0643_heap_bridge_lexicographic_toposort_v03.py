"""
CI0643 — 힙 → 사전순 최소 위상 정렬

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 03 / 20
Time cap: 900 seconds
Source checks:

문제
----
0<=n<=100 정점과 최대 1000개 유향 선행 간선 (u,v)이 주어집니다. 모든 정점을 포함하는 위상 순서 중 사전순 최소를 반환하세요. 사이클(자기 루프 포함)이면 None, 빈 그래프는 []입니다. 중복 간선은 같은 제약이며 입력은 보존합니다.

연습 초점
---------
진입차수와 현재 가능한 정점의 최소 힙

구현할 함수
-----------
def heap_bridge_lexicographic_toposort(n: int, edges: list[tuple[int, int]]) -> list[int] | None:

예시 및 필수 테스트
-------------------
- heap_bridge_lexicographic_toposort(0, []) == [] and heap_bridge_lexicographic_toposort(3, []) == [0, 1, 2]
- heap_bridge_lexicographic_toposort(4, [(0, 3), (1, 2)]) == [0, 1, 2, 3]
- ((_bridge_1_arg_0 := 2), (_bridge_1_arg_1 := [(0, 1), (1, 0)]), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_lexicographic_toposort(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] is None and ((_bridge_2_arg_0 := 2), (_bridge_2_arg_1 := [(0, 1), (0, 1)]), (_bridge_2_before := repr((_bridge_2_arg_1,))), (_bridge_2_result := heap_bridge_lexicographic_toposort(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_1,)) == _bridge_2_before else object())[-1] == [0, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0643 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_lexicographic_toposort(n: int, edges: list[tuple[int, int]]) -> list[int] | None:
    raise NotImplementedError("TODO: CI0643")


def self_test() -> None:
    assert heap_bridge_lexicographic_toposort(0, []) == [] and heap_bridge_lexicographic_toposort(3, []) == [0, 1, 2]
    assert heap_bridge_lexicographic_toposort(4, [(0, 3), (1, 2)]) == [0, 1, 2, 3]
    assert ((_bridge_1_arg_0 := 2), (_bridge_1_arg_1 := [(0, 1), (1, 0)]), (_bridge_1_before := repr((_bridge_1_arg_1,))), (_bridge_1_result := heap_bridge_lexicographic_toposort(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_1,)) == _bridge_1_before else object())[-1] is None and ((_bridge_2_arg_0 := 2), (_bridge_2_arg_1 := [(0, 1), (0, 1)]), (_bridge_2_before := repr((_bridge_2_arg_1,))), (_bridge_2_result := heap_bridge_lexicographic_toposort(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_1,)) == _bridge_2_before else object())[-1] == [0, 1]
