"""
CI0787 — 정렬 집합 → 한 번씩 사용하는 목표 조합

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 07 / 20
Time cap: 900 seconds
Source checks:

문제
----
길이 0~16, 원소 1~30인 배열과 0<=target<=100입니다. 각 인덱스를 최대 한 번 사용해 합이 target인 조합을 반환하세요. 각 조합은 오름차순 tuple, 전체는 사전순이며 같은 값 조합은 중복 제거합니다. target=0이면 [()], 입력은 보존합니다.

연습 초점
---------
동일 값 후보와 인덱스 재사용을 구분하는 백트래킹

구현할 함수
-----------
def sorted_structure_bridge_single_use_combination_sum(values: list[int], target: int) -> list[tuple[int, ...]]:

예시 및 필수 테스트
-------------------
- sorted_structure_bridge_single_use_combination_sum([], 0) == [()] and sorted_structure_bridge_single_use_combination_sum([], 1) == []
- sorted_structure_bridge_single_use_combination_sum([10, 1, 2, 7, 6, 1, 5], 8) == [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]
- ((_bridge_1_arg_0 := [2, 2, 3]), (_bridge_1_arg_1 := 4), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_single_use_combination_sum(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [(2, 2)] and ((_bridge_2_arg_0 := [2]), (_bridge_2_arg_1 := 4), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_single_use_combination_sum(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0787 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_bridge_single_use_combination_sum(values: list[int], target: int) -> list[tuple[int, ...]]:
    raise NotImplementedError("TODO: CI0787")


def self_test() -> None:
    assert sorted_structure_bridge_single_use_combination_sum([], 0) == [()] and sorted_structure_bridge_single_use_combination_sum([], 1) == []
    assert sorted_structure_bridge_single_use_combination_sum([10, 1, 2, 7, 6, 1, 5], 8) == [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]
    assert ((_bridge_1_arg_0 := [2, 2, 3]), (_bridge_1_arg_1 := 4), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_single_use_combination_sum(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [(2, 2)] and ((_bridge_2_arg_0 := [2]), (_bridge_2_arg_1 := 4), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_single_use_combination_sum(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == []
