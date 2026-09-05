"""
CI0732 — 두 heap 절반 분할 — 반복 세트 6

Chapter: Heaps / Priority Queues
Seed: 37 / 40
Variant: 12 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
max heap lower와 min heap upper를 유지해 lower 크기가 upper와 같거나 하나 크도록 한 뒤 두 절반을 오름차순 리스트로 반환하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
two-heaps balancing

구현할 함수
-----------
def heap_r06_balanced_halves(values: list[int]) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r06_balanced_halves([4, 1, 3, 2]) == ([1, 2], [3, 4])
- heap_r06_balanced_halves([3, 1, 2]) == ([1, 2], [3])
- heap_r06_balanced_halves([]) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0732 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r06_balanced_halves(values: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: CI0732")


def self_test() -> None:
    assert heap_r06_balanced_halves([4, 1, 3, 2]) == ([1, 2], [3, 4])
    assert heap_r06_balanced_halves([3, 1, 2]) == ([1, 2], [3])
    assert heap_r06_balanced_halves([]) == ([], [])
