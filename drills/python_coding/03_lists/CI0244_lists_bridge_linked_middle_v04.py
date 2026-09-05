"""
CI0244 — 리스트 → 연결 경로의 중간 노드

Chapter: Lists
Seed: 13 / 40
Variant: 04 / 20
Time cap: 420 seconds
Source checks:

문제
----
최대 200개 노드의 다음 인덱스 links와 head(-1은 null)가 주어집니다. 도달 경로는 비순환입니다. 중간 노드의 인덱스를 반환하며 짝수 길이면 두 중앙 중 뒤쪽을 선택합니다. 빈 경로는 -1, 입력은 보존합니다.

연습 초점
---------
배열 위치가 아닌 연결 순서와 빠른/느린 포인터

구현할 함수
-----------
def lists_bridge_linked_middle(links: list[int], head: int) -> int:

예시 및 필수 테스트
-------------------
- lists_bridge_linked_middle([], -1) == -1 and lists_bridge_linked_middle([-1], 0) == 0
- lists_bridge_linked_middle([2, -1, 1], 0) == 2
- ((_bridge_1_arg_0 := [3, -1, 1, 2]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_middle(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [1, -1]), (_bridge_2_arg_1 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_middle(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0244 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_bridge_linked_middle(links: list[int], head: int) -> int:
    raise NotImplementedError("TODO: CI0244")


def self_test() -> None:
    assert lists_bridge_linked_middle([], -1) == -1 and lists_bridge_linked_middle([-1], 0) == 0
    assert lists_bridge_linked_middle([2, -1, 1], 0) == 2
    assert ((_bridge_1_arg_0 := [3, -1, 1, 2]), (_bridge_1_arg_1 := 0), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := lists_bridge_linked_middle(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [1, -1]), (_bridge_2_arg_1 := 0), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := lists_bridge_linked_middle(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 1
