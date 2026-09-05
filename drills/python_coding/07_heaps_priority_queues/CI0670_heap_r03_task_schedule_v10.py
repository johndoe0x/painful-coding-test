"""
CI0670 — 작업 스케줄러 — 반복 세트 3

Chapter: Heaps / Priority Queues
Seed: 34 / 40
Variant: 10 / 20
Time cap: 300 seconds
Source checks: heapq_call, sorted_call

문제
----
(0 이상 도착시각, 양수 처리시간, 고유 이름) 작업을 단일 CPU에서 비선점 실행하세요. CPU가 빌 때 도착한 작업 중 처리시간이 짧은 순서, 동률이면 이름순으로 고르고, 대기 작업이 없으면 다음 도착시각으로 이동합니다. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
event sorting과 available-task heap

구현할 함수
-----------
def heap_r03_task_schedule(tasks: list[tuple[int, int, str]]) -> list[str]:

필수 구현 방식
--------------
- heapq API를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r03_task_schedule([(0, 3, 'a'), (1, 1, 'b'), (1, 1, 'c')]) == ['a', 'b', 'c']
- heap_r03_task_schedule([]) == []
- heap_r03_task_schedule([(0, 4, 'a'), (1, 3, 'b'), (1, 1, 'c'), (10, 1, 'd')]) == ['a', 'c', 'b', 'd']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0670 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r03_task_schedule(tasks: list[tuple[int, int, str]]) -> list[str]:
    raise NotImplementedError("TODO: CI0670")


def self_test() -> None:
    assert heap_r03_task_schedule([(0, 3, 'a'), (1, 1, 'b'), (1, 1, 'c')]) == ['a', 'b', 'c']
    assert heap_r03_task_schedule([]) == []
    assert heap_r03_task_schedule([(0, 4, 'a'), (1, 3, 'b'), (1, 1, 'c'), (10, 1, 'd')]) == ['a', 'c', 'b', 'd']
