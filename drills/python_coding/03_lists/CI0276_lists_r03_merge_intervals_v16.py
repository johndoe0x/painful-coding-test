"""
CI0276 — 겹치는 구간 병합 — 반복 세트 3

Chapter: Lists
Seed: 14 / 40
Variant: 16 / 20
Time cap: 240 seconds
Source checks: sorted_call

문제
----
닫힌 구간을 시작점 순으로 정렬한 뒤 겹치거나 맞닿는 구간을 병합하세요. 이 파일은 Lists 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
정렬 후 선형 병합

구현할 함수
-----------
def lists_r03_merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- lists_r03_merge_intervals([(1, 3), (2, 5), (8, 9)]) == [(1, 5), (8, 9)]
- lists_r03_merge_intervals([]) == []
- lists_r03_merge_intervals([(1, 2), (2, 3)]) == [(1, 3)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0276 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r03_merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: CI0276")


def self_test() -> None:
    assert lists_r03_merge_intervals([(1, 3), (2, 5), (8, 9)]) == [(1, 5), (8, 9)]
    assert lists_r03_merge_intervals([]) == []
    assert lists_r03_merge_intervals([(1, 2), (2, 3)]) == [(1, 3)]
