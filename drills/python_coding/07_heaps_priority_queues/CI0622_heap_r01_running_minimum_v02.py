"""
CI0622 — 삽입별 최솟값 — 반복 세트 1

Chapter: Heaps / Priority Queues
Seed: 32 / 40
Variant: 02 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
각 값을 heap에 push한 직후 현재 최솟값을 기록하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
heappush와 root peek

구현할 함수
-----------
def heap_r01_running_minimum(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r01_running_minimum([3, 1, 2]) == [3, 1, 1]
- heap_r01_running_minimum([]) == []
- heap_r01_running_minimum([-1, -2]) == [-1, -2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0622 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r01_running_minimum(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0622")


def self_test() -> None:
    assert heap_r01_running_minimum([3, 1, 2]) == [3, 1, 1]
    assert heap_r01_running_minimum([]) == []
    assert heap_r01_running_minimum([-1, -2]) == [-1, -2]
