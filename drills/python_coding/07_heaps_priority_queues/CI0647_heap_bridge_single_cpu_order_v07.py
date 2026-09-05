"""
CI0647 — 힙 → 도착 시각이 있는 CPU 스케줄

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 07 / 20
Time cap: 900 seconds
Source checks:

문제
----
최대 200개 tasks[i]=(도착 시각 0~10000, 실행 시간 1~1000)입니다. 시각 0부터 한 CPU가 비선점 실행하며, 대기 중 실행 시간이 가장 짧은 작업, 동률이면 작은 원래 인덱스를 고릅니다. 대기가 없으면 다음 도착까지 건너뜁니다. 처리한 인덱스 순서를 반환하고 입력은 보존합니다.

연습 초점
---------
도착 이벤트 정렬과 준비 큐의 별도 우선순위

구현할 함수
-----------
def heap_bridge_single_cpu_order(tasks: list[tuple[int, int]]) -> list[int]:

예시 및 필수 테스트
-------------------
- heap_bridge_single_cpu_order([]) == [] and heap_bridge_single_cpu_order([(8, 2)]) == [0]
- heap_bridge_single_cpu_order([(1, 2), (2, 4), (3, 2), (4, 1)]) == [0, 2, 3, 1]
- ((_bridge_1_arg_0 := [(0, 3), (0, 3), (9, 1), (0, 1)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := heap_bridge_single_cpu_order(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [3, 0, 1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0647 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_bridge_single_cpu_order(tasks: list[tuple[int, int]]) -> list[int]:
    raise NotImplementedError("TODO: CI0647")


def self_test() -> None:
    assert heap_bridge_single_cpu_order([]) == [] and heap_bridge_single_cpu_order([(8, 2)]) == [0]
    assert heap_bridge_single_cpu_order([(1, 2), (2, 4), (3, 2), (4, 1)]) == [0, 2, 3, 1]
    assert ((_bridge_1_arg_0 := [(0, 3), (0, 3), (9, 1), (0, 1)]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := heap_bridge_single_cpu_order(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [3, 0, 1, 2]
