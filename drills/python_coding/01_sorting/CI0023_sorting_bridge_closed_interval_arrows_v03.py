"""
CI0023 — 정렬 → 닫힌 구간 관통

Chapter: Sorting
Seed: 02 / 40
Variant: 03 / 20
Time cap: 420 seconds
Source checks:

문제
----
최대 200개의 닫힌 구간 [start,end], start<=end를 모두 관통하는 최소 점 개수를 반환하세요. 하나의 점은 그 점을 포함하는 모든 구간을 관통합니다. 빈 입력은 0, 입력은 보존합니다.

연습 초점
---------
닫힌 끝점 공유와 종료점 그리디

구현할 함수
-----------
def sorting_bridge_closed_interval_arrows(intervals: list[tuple[int, int]]) -> int:

예시 및 필수 테스트
-------------------
- sorting_bridge_closed_interval_arrows([]) == 0 and sorting_bridge_closed_interval_arrows([(1, 2), (2, 3)]) == 1
- sorting_bridge_closed_interval_arrows([(1, 5), (2, 3), (4, 6)]) == 2
- ((_bridge_1_arg_0 := [(0, 0), (1, 1), (0, 0)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_closed_interval_arrows(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0023 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_bridge_closed_interval_arrows(intervals: list[tuple[int, int]]) -> int:
    raise NotImplementedError("TODO: CI0023")


def self_test() -> None:
    assert sorting_bridge_closed_interval_arrows([]) == 0 and sorting_bridge_closed_interval_arrows([(1, 2), (2, 3)]) == 1
    assert sorting_bridge_closed_interval_arrows([(1, 5), (2, 3), (4, 6)]) == 2
    assert ((_bridge_1_arg_0 := [(0, 0), (1, 1), (0, 0)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorting_bridge_closed_interval_arrows(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2
