"""
CI0092 — 거의 정렬된 배열 — 반복 세트 5

Chapter: Sorting
Seed: 05 / 40
Variant: 12 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
각 값이 최종 위치에서 최대 distance만큼 떨어진 배열을 크기 distance+1 heap으로 정렬하세요. 이 파일은 Sorting 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
작은 heap을 이용한 O(n log k) 정렬

구현할 함수
-----------
def sorting_r05_nearly_sorted_heap(values: list[int], distance: int) -> list[int]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r05_nearly_sorted_heap([3, 1, 2, 5, 4], 2) == [1, 2, 3, 4, 5]
- sorting_r05_nearly_sorted_heap([], 3) == []
- sorting_r05_nearly_sorted_heap([2, 1], 1) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0092 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r05_nearly_sorted_heap(values: list[int], distance: int) -> list[int]:
    raise NotImplementedError("TODO: CI0092")


def self_test() -> None:
    assert sorting_r05_nearly_sorted_heap([3, 1, 2, 5, 4], 2) == [1, 2, 3, 4, 5]
    assert sorting_r05_nearly_sorted_heap([], 3) == []
    assert sorting_r05_nearly_sorted_heap([2, 1], 1) == [1, 2]
