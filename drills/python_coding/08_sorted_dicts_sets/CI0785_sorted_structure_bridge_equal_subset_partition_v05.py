"""
CI0785 — 정렬 구조 → 같은 합 부분집합

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 05 / 20
Time cap: 720 seconds
Source checks:

문제
----
길이 0~40, 원소 0~100인 배열의 모든 인덱스를 두 그룹에 한 번씩 배정해 합을 같게 할 수 있는지 반환하세요. 빈 그룹을 허용하며 빈 배열은 True입니다. 같은 값의 서로 다른 위치는 별개 원소이고 각 원소는 한 번만 사용합니다. 입력은 보존합니다.

연습 초점
---------
0/1 배낭과 같은 라운드 상태 재사용 방지

구현할 함수
-----------
def sorted_structure_bridge_equal_subset_partition(values: list[int]) -> bool:

예시 및 필수 테스트
-------------------
- sorted_structure_bridge_equal_subset_partition([]) is True and sorted_structure_bridge_equal_subset_partition([0, 0]) is True
- sorted_structure_bridge_equal_subset_partition([1, 5, 11, 5]) is True and sorted_structure_bridge_equal_subset_partition([1, 2, 3, 5]) is False
- ((_bridge_1_arg_0 := [1, 2, 5]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_equal_subset_partition(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] is False and ((_bridge_2_arg_0 := [2, 2]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_equal_subset_partition(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0785 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_bridge_equal_subset_partition(values: list[int]) -> bool:
    raise NotImplementedError("TODO: CI0785")


def self_test() -> None:
    assert sorted_structure_bridge_equal_subset_partition([]) is True and sorted_structure_bridge_equal_subset_partition([0, 0]) is True
    assert sorted_structure_bridge_equal_subset_partition([1, 5, 11, 5]) is True and sorted_structure_bridge_equal_subset_partition([1, 2, 3, 5]) is False
    assert ((_bridge_1_arg_0 := [1, 2, 5]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_equal_subset_partition(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] is False and ((_bridge_2_arg_0 := [2, 2]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_equal_subset_partition(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] is True
