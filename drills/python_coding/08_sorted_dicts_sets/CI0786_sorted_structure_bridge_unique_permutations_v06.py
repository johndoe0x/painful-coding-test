"""
CI0786 — 정렬 집합 → 중복 없는 순열

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 06 / 20
Time cap: 900 seconds
Source checks:

문제
----
길이 0~8의 정수 배열 원소를 모두 한 번씩 사용하는 서로 다른 순열을 tuple 사전순으로 반환하세요. 중복 값은 같은 순열을 중복 생성하지 않습니다. 빈 배열은 [()], 입력은 보존합니다.

연습 초점
---------
정렬과 같은 깊이 중복 제거 백트래킹

구현할 함수
-----------
def sorted_structure_bridge_unique_permutations(values: list[int]) -> list[tuple[int, ...]]:

예시 및 필수 테스트
-------------------
- sorted_structure_bridge_unique_permutations([]) == [()] and sorted_structure_bridge_unique_permutations([2, 2]) == [(2, 2)]
- sorted_structure_bridge_unique_permutations([1, 1, 2]) == [(1, 1, 2), (1, 2, 1), (2, 1, 1)]
- ((_bridge_1_arg_0 := [0, -1]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_unique_permutations(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [(-1, 0), (0, -1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0786 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_bridge_unique_permutations(values: list[int]) -> list[tuple[int, ...]]:
    raise NotImplementedError("TODO: CI0786")


def self_test() -> None:
    assert sorted_structure_bridge_unique_permutations([]) == [()] and sorted_structure_bridge_unique_permutations([2, 2]) == [(2, 2)]
    assert sorted_structure_bridge_unique_permutations([1, 1, 2]) == [(1, 1, 2), (1, 2, 1), (2, 1, 1)]
    assert ((_bridge_1_arg_0 := [0, -1]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_unique_permutations(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [(-1, 0), (0, -1)]
