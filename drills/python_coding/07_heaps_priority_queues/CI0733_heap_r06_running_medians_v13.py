"""
CI0733 — 실시간 중앙값 — 반복 세트 6

Chapter: Heaps / Priority Queues
Seed: 37 / 40
Variant: 13 / 20
Time cap: 300 seconds
Source checks: heapq_call

문제
----
max heap과 min heap 두 개로 각 prefix의 중앙값을 반환하세요. 짝수 개면 두 중앙값 평균입니다. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
two-heaps median

구현할 함수
-----------
def heap_r06_running_medians(values: list[int]) -> list[float]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r06_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]
- heap_r06_running_medians([]) == []
- heap_r06_running_medians([1, 3]) == [1.0, 2.0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0733 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r06_running_medians(values: list[int]) -> list[float]:
    raise NotImplementedError("TODO: CI0733")


def self_test() -> None:
    assert heap_r06_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2.0, 1.5, 2.0, 3.5, 2.0, 2.0, 2.0]
    assert heap_r06_running_medians([]) == []
    assert heap_r06_running_medians([1, 3]) == [1.0, 2.0]
