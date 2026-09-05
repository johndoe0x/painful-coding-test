"""
CI0245 — 리스트 → 사이클 진입 노드

Chapter: Lists
Seed: 13 / 40
Variant: 05 / 20
Time cap: 600 seconds
Source checks:

문제
----
최대 200개 노드의 다음 인덱스 links와 head(-1은 null)가 주어집니다. head부터 따라갈 때 처음 재방문하게 되는 노드 인덱스를 반환하세요. 사이클이 없으면 -1입니다. 비도달 사이클은 무시하고 입력은 보존합니다.

연습 초점
---------
사이클 존재와 진입점의 구분

구현할 함수
-----------
def lists_bridge_linked_cycle_entry(links: list[int], head: int) -> int:

예시 및 필수 테스트
-------------------
- lists_bridge_linked_cycle_entry([], -1) == -1 and lists_bridge_linked_cycle_entry([0], 0) == 0
- lists_bridge_linked_cycle_entry([1, 2, 3, 1], 0) == 1
- ((_bridge_1_arg_0 := [2, -1, 1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_cycle_entry(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == -1 and ((_bridge_2_arg_0 := [1, 2, 2]), (_bridge_2_arg_1 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_cycle_entry(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0245 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_bridge_linked_cycle_entry(links: list[int], head: int) -> int:
    raise NotImplementedError("TODO: CI0245")


def self_test() -> None:
    assert lists_bridge_linked_cycle_entry([], -1) == -1 and lists_bridge_linked_cycle_entry([0], 0) == 0
    assert lists_bridge_linked_cycle_entry([1, 2, 3, 1], 0) == 1
    assert ((_bridge_1_arg_0 := [2, -1, 1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_cycle_entry(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == -1 and ((_bridge_2_arg_0 := [1, 2, 2]), (_bridge_2_arg_1 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_cycle_entry(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2
