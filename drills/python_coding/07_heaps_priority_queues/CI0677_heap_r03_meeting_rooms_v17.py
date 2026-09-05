"""
CI0677 — 필요 회의실 수 — 반복 세트 3

Chapter: Heaps / Priority Queues
Seed: 34 / 40
Variant: 17 / 20
Time cap: 240 seconds
Source checks: heapq_call, sorted_call

문제
----
시작 시각 순으로 보며 종료 시각 min heap으로 동시에 필요한 최소 회의실 수를 반환하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
interval scheduling heap

구현할 함수
-----------
def heap_r03_meeting_rooms(intervals: list[tuple[int, int]]) -> int:

필수 구현 방식
--------------
- heapq API를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r03_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
- heap_r03_meeting_rooms([]) == 0
- heap_r03_meeting_rooms([(1, 2), (2, 3)]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0677 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r03_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
    raise NotImplementedError("TODO: CI0677")


def self_test() -> None:
    assert heap_r03_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2
    assert heap_r03_meeting_rooms([]) == 0
    assert heap_r03_meeting_rooms([(1, 2), (2, 3)]) == 1
