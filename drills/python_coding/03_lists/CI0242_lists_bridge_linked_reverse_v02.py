"""
CI0242 — 리스트 → 인덱스 연결 역전

Chapter: Lists
Seed: 13 / 40
Variant: 02 / 20
Time cap: 600 seconds
Source checks:

문제
----
길이 0~200인 links[i]는 다음 노드 인덱스 또는 -1입니다. head도 유효 인덱스 또는 -1이며 도달 경로는 비순환입니다. 그 경로만 역전한 (새 head, 새 links)를 반환하세요. 도달하지 않는 노드의 링크는 그대로, 입력은 보존합니다.

연습 초점
---------
노드 정체성을 유지하는 포인터 역전

구현할 함수
-----------
def lists_bridge_linked_reverse(links: list[int], head: int) -> tuple[int, list[int]]:

예시 및 필수 테스트
-------------------
- lists_bridge_linked_reverse([], -1) == (-1, []) and lists_bridge_linked_reverse([-1], 0) == (0, [-1])
- lists_bridge_linked_reverse([2, -1, 1], 0) == (1, [-1, 2, 0])
- ((_bridge_1_arg_0 := [1, -1, 2]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_reverse(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (1, [-1, 0, 2]) and ((_bridge_2_arg_0 := [0]), (_bridge_2_arg_1 := (-1)), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_reverse(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (-1, [0])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0242 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_bridge_linked_reverse(links: list[int], head: int) -> tuple[int, list[int]]:
    raise NotImplementedError("TODO: CI0242")


def self_test() -> None:
    assert lists_bridge_linked_reverse([], -1) == (-1, []) and lists_bridge_linked_reverse([-1], 0) == (0, [-1])
    assert lists_bridge_linked_reverse([2, -1, 1], 0) == (1, [-1, 2, 0])
    assert ((_bridge_1_arg_0 := [1, -1, 2]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_reverse(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (1, [-1, 0, 2]) and ((_bridge_2_arg_0 := [0]), (_bridge_2_arg_1 := (-1)), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_reverse(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (-1, [0])
