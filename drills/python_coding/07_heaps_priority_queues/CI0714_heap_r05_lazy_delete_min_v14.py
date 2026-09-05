"""
CI0714 — Lazy deletion 최소값 — 반복 세트 5

Chapter: Heaps / Priority Queues
Seed: 36 / 40
Variant: 14 / 20
Time cap: 300 seconds
Source checks: heapq_call, counter_call

문제
----
add, remove, min 명령을 heap과 삭제 예약 Counter로 처리하세요. remove는 현재 존재하는 값 한 개만 제거하고 없는 값은 무시합니다. min마다 유효한 최솟값 또는 None을 기록하며 min의 값 인자는 무시합니다. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
heap lazy deletion과 실제 빈도 관리

구현할 함수
-----------
def heap_r05_lazy_delete_min(operations: list[tuple[str, int]]) -> list[int | None]:

필수 구현 방식
--------------
- heapq API를 사용한다.
- collections.Counter를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r05_lazy_delete_min([('add', 2), ('add', 1), ('remove', 1), ('min', 0)]) == [2]
- heap_r05_lazy_delete_min([('min', 0)]) == [None]
- heap_r05_lazy_delete_min([('remove', 1), ('add', 1), ('add', 1), ('remove', 1), ('min', 0), ('remove', 1), ('min', 0)]) == [1, None]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0714 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r05_lazy_delete_min(operations: list[tuple[str, int]]) -> list[int | None]:
    raise NotImplementedError("TODO: CI0714")


def self_test() -> None:
    assert heap_r05_lazy_delete_min([('add', 2), ('add', 1), ('remove', 1), ('min', 0)]) == [2]
    assert heap_r05_lazy_delete_min([('min', 0)]) == [None]
    assert heap_r05_lazy_delete_min([('remove', 1), ('add', 1), ('add', 1), ('remove', 1), ('min', 0), ('remove', 1), ('min', 0)]) == [1, None]
