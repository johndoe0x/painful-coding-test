"""
CI0646 — 힙 → 최소 병목 격자 경로

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 06 / 20
Time cap: 900 seconds
Source checks:

문제
----
0~30행/열의 직사각형 정수 높이 격자에서 좌상단부터 우하단까지 상하좌우로 이동합니다. 경로 노력은 연속 셀 높이 차이 절댓값 중 최댓값입니다. 가능한 최소 노력을 반환하세요. 빈 격자/빈 열/단일 셀은 0, 높이는 -1000~1000, 입력은 보존합니다.

연습 초점
---------
합이 아닌 max를 사용하는 다익스트라 완화

구현할 함수
-----------
def heap_bridge_minimum_effort_grid(heights: list[list[int]]) -> int:

예시 및 필수 테스트
-------------------
- heap_bridge_minimum_effort_grid([]) == 0 and heap_bridge_minimum_effort_grid([[]]) == 0 and heap_bridge_minimum_effort_grid([[7]]) == 0
- heap_bridge_minimum_effort_grid([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
- ((_bridge_1_arg_0 := [[1, 10], [2, 3]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := heap_bridge_minimum_effort_grid(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 1 and ((_bridge_2_arg_0 := [[1, 4, 2]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := heap_bridge_minimum_effort_grid(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0646 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_minimum_effort_grid(heights: list[list[int]]) -> int:
    raise NotImplementedError("TODO: CI0646")


def self_test() -> None:
    assert heap_bridge_minimum_effort_grid([]) == 0 and heap_bridge_minimum_effort_grid([[]]) == 0 and heap_bridge_minimum_effort_grid([[7]]) == 0
    assert heap_bridge_minimum_effort_grid([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert ((_bridge_1_arg_0 := [[1, 10], [2, 3]]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := heap_bridge_minimum_effort_grid(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 1 and ((_bridge_2_arg_0 := [[1, 4, 2]]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := heap_bridge_minimum_effort_grid(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 3
