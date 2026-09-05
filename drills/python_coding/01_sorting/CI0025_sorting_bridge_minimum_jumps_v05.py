"""
CI0025 — 정렬 사고 → 점프 도달 경계

Chapter: Sorting
Seed: 02 / 40
Variant: 05 / 20
Time cap: 600 seconds
Source checks:

문제
----
길이 0~200, 원소 0~200의 배열에서 0번 위치에서 마지막 위치까지 필요한 최소 점프 수를 반환하세요. i에서는 앞으로 1~jumps[i]칸 이동합니다. 도달 불가면 -1, 길이 0 또는 1이면 0입니다. 입력은 보존합니다.

연습 초점
---------
현재 층과 다음 도달 범위의 그리디

구현할 함수
-----------
def sorting_bridge_minimum_jumps(jumps: list[int]) -> int:

예시 및 필수 테스트
-------------------
- sorting_bridge_minimum_jumps([]) == 0 and sorting_bridge_minimum_jumps([0]) == 0 and sorting_bridge_minimum_jumps([0, 1]) == -1
- sorting_bridge_minimum_jumps([2, 3, 1, 1, 4]) == 2 and sorting_bridge_minimum_jumps([3, 2, 1, 0, 4]) == -1
- ((_bridge_1_arg_0 := [2, 0, 1, 1]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_minimum_jumps(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [1, 1, 1, 1]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_minimum_jumps(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0025 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_minimum_jumps(jumps: list[int]) -> int:
    raise NotImplementedError("TODO: CI0025")


def self_test() -> None:
    assert sorting_bridge_minimum_jumps([]) == 0 and sorting_bridge_minimum_jumps([0]) == 0 and sorting_bridge_minimum_jumps([0, 1]) == -1
    assert sorting_bridge_minimum_jumps([2, 3, 1, 1, 4]) == 2 and sorting_bridge_minimum_jumps([3, 2, 1, 0, 4]) == -1
    assert ((_bridge_1_arg_0 := [2, 0, 1, 1]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_minimum_jumps(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [1, 1, 1, 1]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorting_bridge_minimum_jumps(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 3
