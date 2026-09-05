"""
CI0772 — 목표 이하 쌍 개수 — 반복 세트 1

Chapter: Sorted Dicts and Sorted Sets
Seed: 39 / 40
Variant: 12 / 20
Time cap: 240 seconds
Source checks: bisect_call, sorted_call

문제
----
값을 정렬한 뒤 각 위치에서 bisect_right로 합이 target 이하인 서로 다른 index 쌍 i < j의 개수를 반환하세요. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
정렬과 upper bound counting

구현할 함수
-----------
def sorted_structure_r01_pair_sum_count(values: list[int], target: int) -> int:

필수 구현 방식
--------------
- bisect API를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r01_pair_sum_count([1, 2, 3, 4], 5) == 4
- sorted_structure_r01_pair_sum_count([], 0) == 0
- (sorted_structure_r01_pair_sum_count([2, 2, 2], 3), sorted_structure_r01_pair_sum_count([2, 2, 2], 4)) == (0, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0772 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r01_pair_sum_count(values: list[int], target: int) -> int:
    raise NotImplementedError("TODO: CI0772")


def self_test() -> None:
    assert sorted_structure_r01_pair_sum_count([1, 2, 3, 4], 5) == 4
    assert sorted_structure_r01_pair_sum_count([], 0) == 0
    assert (sorted_structure_r01_pair_sum_count([2, 2, 2], 3), sorted_structure_r01_pair_sum_count([2, 2, 2], 4)) == (0, 3)
