"""
CI0422 — 격자 → 장애물 경로 수 DP

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 02 / 20
Time cap: 600 seconds
Source checks:

문제
----
0~30행/열의 직사각형 0/1 격자에서 1은 장애물입니다. 좌상단에서 우하단까지 오른쪽/아래로만 가는 경로 수를 반환하세요. 빈 격자/빈 열 또는 출발·도착 장애물은 0입니다. 입력은 보존합니다.

연습 초점
---------
2차원 경로 수 점화식과 막힌 경계

구현할 함수
-----------
def grid_bridge_obstacle_path_count(grid: list[list[int]]) -> int:

예시 및 필수 테스트
-------------------
- grid_bridge_obstacle_path_count([]) == 0 and grid_bridge_obstacle_path_count([[]]) == 0 and grid_bridge_obstacle_path_count([[0]]) == 1
- grid_bridge_obstacle_path_count([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
- ((_bridge_1_arg_0 := [[0, 1, 0]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_obstacle_path_count(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 0 and ((_bridge_2_arg_0 := [[1]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_obstacle_path_count(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 0 and (((_bridge_3_arg_0 := [[0, 0], [0, 0]]), (_bridge_3_before := repr((_bridge_3_arg_0,))), (_bridge_3_result := grid_bridge_obstacle_path_count(_bridge_3_arg_0)), _bridge_3_result if repr((_bridge_3_arg_0,)) == _bridge_3_before else object())[-1] == 2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0422 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_bridge_obstacle_path_count(grid: list[list[int]]) -> int:
    raise NotImplementedError("TODO: CI0422")


def self_test() -> None:
    assert grid_bridge_obstacle_path_count([]) == 0 and grid_bridge_obstacle_path_count([[]]) == 0 and grid_bridge_obstacle_path_count([[0]]) == 1
    assert grid_bridge_obstacle_path_count([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert ((_bridge_1_arg_0 := [[0, 1, 0]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_obstacle_path_count(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 0 and ((_bridge_2_arg_0 := [[1]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_obstacle_path_count(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 0 and (((_bridge_3_arg_0 := [[0, 0], [0, 0]]), (_bridge_3_before := repr((_bridge_3_arg_0,))), (_bridge_3_result := grid_bridge_obstacle_path_count(_bridge_3_arg_0)), _bridge_3_result if repr((_bridge_3_arg_0,)) == _bridge_3_before else object())[-1] == 2)
