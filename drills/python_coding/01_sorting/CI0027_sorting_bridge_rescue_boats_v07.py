"""
CI0027 — 정렬 → 두 사람 보트 배치

Chapter: Sorting
Seed: 02 / 40
Variant: 07 / 20
Time cap: 420 seconds
Source checks:

문제
----
최대 200명의 몸무게는 1~limit이고 limit>=1입니다. 보트마다 최대 2명, 합계 limit 이하로 모두 태울 최소 보트 수를 반환하세요. 빈 입력은 0, 입력은 보존합니다.

연습 초점
---------
정렬 양끝 포인터와 짝짓기 그리디

구현할 함수
-----------
def sorting_bridge_rescue_boats(weights: list[int], limit: int) -> int:

예시 및 필수 테스트
-------------------
- sorting_bridge_rescue_boats([], 3) == 0 and sorting_bridge_rescue_boats([1, 2], 3) == 1
- sorting_bridge_rescue_boats([3, 2, 2, 1], 3) == 3 and sorting_bridge_rescue_boats([3, 3, 3, 3], 5) == 4
- ((_bridge_1_arg_0 := [1, 1, 1]), (_bridge_1_arg_1 := 3), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_rescue_boats(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [2, 2, 2]), (_bridge_2_arg_1 := 4), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_rescue_boats(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0027 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_rescue_boats(weights: list[int], limit: int) -> int:
    raise NotImplementedError("TODO: CI0027")


def self_test() -> None:
    assert sorting_bridge_rescue_boats([], 3) == 0 and sorting_bridge_rescue_boats([1, 2], 3) == 1
    assert sorting_bridge_rescue_boats([3, 2, 2, 1], 3) == 3 and sorting_bridge_rescue_boats([3, 3, 3, 3], 5) == 4
    assert ((_bridge_1_arg_0 := [1, 1, 1]), (_bridge_1_arg_1 := 3), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_rescue_boats(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [2, 2, 2]), (_bridge_2_arg_1 := 4), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_rescue_boats(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2
