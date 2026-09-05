"""
CI0427 — 격자 → 증가 경로 DAG

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 07 / 20
Time cap: 900 seconds
Source checks:

문제
----
0~20행/열의 직사각형 정수 격자에서 어느 셀에서나 시작해 상하좌우로 이동할 수 있습니다. 다음 값이 엄격히 커야 하는 최장 경로의 셀 수를 반환하세요. 빈 격자/빈 열은 0, 입력은 보존합니다.

연습 초점
---------
값이 유도하는 DAG와 메모이제이션

구현할 함수
-----------
def grid_bridge_longest_increasing_grid_path(grid: list[list[int]]) -> int:

예시 및 필수 테스트
-------------------
- grid_bridge_longest_increasing_grid_path([]) == 0 and grid_bridge_longest_increasing_grid_path([[]]) == 0 and grid_bridge_longest_increasing_grid_path([[9]]) == 1
- grid_bridge_longest_increasing_grid_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
- ((_bridge_1_arg_0 := [[1, 1], [1, 1]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_longest_increasing_grid_path(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 1 and ((_bridge_2_arg_0 := [[1, 2], [4, 3]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_longest_increasing_grid_path(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 4

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0427 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_bridge_longest_increasing_grid_path(grid: list[list[int]]) -> int:
    raise NotImplementedError("TODO: CI0427")


def self_test() -> None:
    assert grid_bridge_longest_increasing_grid_path([]) == 0 and grid_bridge_longest_increasing_grid_path([[]]) == 0 and grid_bridge_longest_increasing_grid_path([[9]]) == 1
    assert grid_bridge_longest_increasing_grid_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]) == 4
    assert ((_bridge_1_arg_0 := [[1, 1], [1, 1]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_longest_increasing_grid_path(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 1 and ((_bridge_2_arg_0 := [[1, 2], [4, 3]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_longest_increasing_grid_path(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 4
