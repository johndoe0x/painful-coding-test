"""
CI0022 — 정렬 → 최대 비중첩 일정

Chapter: Sorting
Seed: 02 / 40
Variant: 02 / 20
Time cap: 420 seconds
Source checks:

문제
----
최대 200개의 반열린 구간 [start,end), start<end에서 서로 겹치지 않게 선택할 수 있는 최대 개수를 반환하세요. 끝과 시작이 같으면 호환됩니다. 빈 입력은 0, 입력은 보존합니다.

연습 초점
---------
종료 시각 정렬과 그리디 선택

구현할 함수
-----------
def sorting_bridge_interval_schedule(intervals: list[tuple[int, int]]) -> int:

예시 및 필수 테스트
-------------------
- sorting_bridge_interval_schedule([]) == 0 and sorting_bridge_interval_schedule([(0, 2), (2, 4)]) == 2
- sorting_bridge_interval_schedule([(0, 10), (1, 2), (2, 3), (3, 4)]) == 3
- ((_bridge_1_arg_0 := [(-3, -1), (-2, 0), (0, 2), (0, 2)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_interval_schedule(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0022 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_interval_schedule(intervals: list[tuple[int, int]]) -> int:
    raise NotImplementedError("TODO: CI0022")


def self_test() -> None:
    assert sorting_bridge_interval_schedule([]) == 0 and sorting_bridge_interval_schedule([(0, 2), (2, 4)]) == 2
    assert sorting_bridge_interval_schedule([(0, 10), (1, 2), (2, 3), (3, 4)]) == 3
    assert ((_bridge_1_arg_0 := [(-3, -1), (-2, 0), (0, 2), (0, 2)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_interval_schedule(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2
