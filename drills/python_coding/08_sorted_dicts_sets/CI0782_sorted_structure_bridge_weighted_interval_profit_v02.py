"""
CI0782 — 정렬 구조 → 가중 일정 DP

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 02 / 20
Time cap: 900 seconds
Source checks:

문제
----
최대 200개 jobs=(시작,종료,이익), 시작<종료, 이익은 -1000~1000입니다. 반열린 구간으로 겹치지 않는 작업의 최대 이익 합을 반환하세요. 끝=다음 시작은 호환되며 아무것도 고르지 않아도 됩니다. 빈 입력은 0, 입력은 보존합니다.

연습 초점
---------
정렬과 이진 탐색으로 이전 호환 DP 상태 연결

구현할 함수
-----------
def sorted_structure_bridge_weighted_interval_profit(jobs: list[tuple[int, int, int]]) -> int:

예시 및 필수 테스트
-------------------
- sorted_structure_bridge_weighted_interval_profit([]) == 0 and sorted_structure_bridge_weighted_interval_profit([(0, 1, -2)]) == 0
- sorted_structure_bridge_weighted_interval_profit([(0, 3, 10), (0, 1, 4), (1, 2, 4), (2, 3, 4)]) == 12
- ((_bridge_1_arg_0 := [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_weighted_interval_profit(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 120

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0782 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_bridge_weighted_interval_profit(jobs: list[tuple[int, int, int]]) -> int:
    raise NotImplementedError("TODO: CI0782")


def self_test() -> None:
    assert sorted_structure_bridge_weighted_interval_profit([]) == 0 and sorted_structure_bridge_weighted_interval_profit([(0, 1, -2)]) == 0
    assert sorted_structure_bridge_weighted_interval_profit([(0, 3, 10), (0, 1, 4), (1, 2, 4), (2, 3, 4)]) == 12
    assert ((_bridge_1_arg_0 := [(1, 3, 50), (2, 4, 10), (3, 5, 40), (3, 6, 70)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_weighted_interval_profit(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 120
