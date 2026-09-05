"""
CI0026 — 정렬 사고 → 양방향 이웃 제약

Chapter: Sorting
Seed: 02 / 40
Variant: 06 / 20
Time cap: 600 seconds
Source checks:

문제
----
최대 200명의 평점에 사탕을 배분합니다. 모두 최소 1개, 바로 옆보다 평점이 높으면 그 이웃보다 더 받아야 합니다. 같은 평점에는 대소 제약이 없습니다. 최소 총개수를 반환하세요. 빈 입력은 0, 입력은 보존합니다.

연습 초점
---------
좌우 제약을 결합하는 양방향 그리디

구현할 함수
-----------
def sorting_bridge_minimum_candy(ratings: list[int]) -> int:

예시 및 필수 테스트
-------------------
- sorting_bridge_minimum_candy([]) == 0 and sorting_bridge_minimum_candy([1]) == 1
- sorting_bridge_minimum_candy([1, 0, 2]) == 5 and sorting_bridge_minimum_candy([1, 2, 2]) == 4
- ((_bridge_1_arg_0 := [1, 3, 4, 5, 2]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_minimum_candy(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 11 and ((_bridge_2_arg_0 := [3, 2, 1]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_minimum_candy(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 6

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0026 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_minimum_candy(ratings: list[int]) -> int:
    raise NotImplementedError("TODO: CI0026")


def self_test() -> None:
    assert sorting_bridge_minimum_candy([]) == 0 and sorting_bridge_minimum_candy([1]) == 1
    assert sorting_bridge_minimum_candy([1, 0, 2]) == 5 and sorting_bridge_minimum_candy([1, 2, 2]) == 4
    assert ((_bridge_1_arg_0 := [1, 3, 4, 5, 2]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_minimum_candy(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 11 and ((_bridge_2_arg_0 := [3, 2, 1]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_minimum_candy(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 6
