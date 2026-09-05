"""
CI0247 — 리스트 → 양끝 교대 재연결

Chapter: Lists
Seed: 13 / 40
Variant: 07 / 20
Time cap: 900 seconds
Source checks:

문제
----
최대 200개 노드의 다음 인덱스 links와 head(-1은 null)의 도달 경로는 비순환입니다. 경로가 L0,L1,...,Lk이면 L0,Lk,L1,Lk-1,... 순서로 중복 없이 재연결한 (head, 새 links)를 반환하세요. 마지막은 -1이며 비도달 링크와 입력은 보존합니다.

연습 초점
---------
연결 리스트 분할·역전·교대 병합

구현할 함수
-----------
def lists_bridge_linked_reorder(links: list[int], head: int) -> tuple[int, list[int]]:

예시 및 필수 테스트
-------------------
- lists_bridge_linked_reorder([], -1) == (-1, []) and lists_bridge_linked_reorder([-1], 0) == (0, [-1])
- lists_bridge_linked_reorder([1, 2, 3, -1], 0) == (0, [3, 2, -1, 1])
- ((_bridge_1_arg_0 := [2, -1, 1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_reorder(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (0, [1, 2, -1, 3])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0247 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_bridge_linked_reorder(links: list[int], head: int) -> tuple[int, list[int]]:
    raise NotImplementedError("TODO: CI0247")


def self_test() -> None:
    assert lists_bridge_linked_reorder([], -1) == (-1, []) and lists_bridge_linked_reorder([-1], 0) == (0, [-1])
    assert lists_bridge_linked_reorder([1, 2, 3, -1], 0) == (0, [3, 2, -1, 1])
    assert ((_bridge_1_arg_0 := [2, -1, 1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_reorder(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (0, [1, 2, -1, 3])
