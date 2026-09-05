"""
CI0631 — prefix별 Top-K — 반복 세트 1

Chapter: Heaps / Priority Queues
Seed: 32 / 40
Variant: 11 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
값이 하나씩 도착할 때 크기 k min heap을 유지하고 각 prefix의 큰 값들을 내림차순으로 기록하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
bounded streaming heap

구현할 함수
-----------
def heap_r01_streaming_top_k(values: list[int], k: int) -> list[list[int]]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r01_streaming_top_k([3, 1, 5], 2) == [[3], [3, 1], [5, 3]]
- heap_r01_streaming_top_k([], 2) == []
- heap_r01_streaming_top_k([1, 2], 0) == [[], []]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0631 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r01_streaming_top_k(values: list[int], k: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0631")


def self_test() -> None:
    assert heap_r01_streaming_top_k([3, 1, 5], 2) == [[3], [3, 1], [5, 3]]
    assert heap_r01_streaming_top_k([], 2) == []
    assert heap_r01_streaming_top_k([1, 2], 0) == [[], []]
