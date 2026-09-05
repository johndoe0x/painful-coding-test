"""
CI0243 — 리스트 → 뒤에서 N번째 노드 삭제

Chapter: Lists
Seed: 13 / 40
Variant: 03 / 20
Time cap: 600 seconds
Source checks:

문제
----
최대 200개 노드의 다음 인덱스 links와 head(-1은 null)가 주어집니다. head 도달 경로는 비순환이며 1<=n<=경로 길이입니다. 뒤에서 n번째 노드를 연결에서 빼고 해당 노드 링크를 -1로 바꾼 (새 head, 새 links)를 반환하세요. 나머지 비도달 링크와 입력은 보존합니다.

연습 초점
---------
선행 노드와 head 삭제 경계

구현할 함수
-----------
def lists_bridge_linked_remove_nth(links: list[int], head: int, n: int) -> tuple[int, list[int]]:

예시 및 필수 테스트
-------------------
- lists_bridge_linked_remove_nth([-1], 0, 1) == (-1, [-1])
- lists_bridge_linked_remove_nth([2, -1, 1], 0, 2) == (0, [1, -1, -1])
- ((_bridge_1_arg_0 := [1, 2, -1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_arg_2 := 3), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_remove_nth(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (1, [-1, 2, -1, 3]) and ((_bridge_2_arg_0 := [1, -1]), (_bridge_2_arg_1 := 0), (_bridge_2_arg_2 := 1), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_remove_nth(_bridge_2_arg_0, _bridge_2_arg_1, _bridge_2_arg_2)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (0, [-1, -1])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0243 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_bridge_linked_remove_nth(links: list[int], head: int, n: int) -> tuple[int, list[int]]:
    raise NotImplementedError("TODO: CI0243")


def self_test() -> None:
    assert lists_bridge_linked_remove_nth([-1], 0, 1) == (-1, [-1])
    assert lists_bridge_linked_remove_nth([2, -1, 1], 0, 2) == (0, [1, -1, -1])
    assert ((_bridge_1_arg_0 := [1, 2, -1, 3]), (_bridge_1_arg_1 := 0), (_bridge_1_arg_2 := 3), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_remove_nth(_bridge_1_arg_0, _bridge_1_arg_1, _bridge_1_arg_2)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (1, [-1, 2, -1, 3]) and ((_bridge_2_arg_0 := [1, -1]), (_bridge_2_arg_1 := 0), (_bridge_2_arg_2 := 1), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_remove_nth(_bridge_2_arg_0, _bridge_2_arg_1, _bridge_2_arg_2)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (0, [-1, -1])
