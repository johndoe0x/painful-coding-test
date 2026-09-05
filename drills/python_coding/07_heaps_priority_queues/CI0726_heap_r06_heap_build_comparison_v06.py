"""
CI0726 — heapify와 반복 push 비교 — 반복 세트 6

Chapter: Heaps / Priority Queues
Seed: 37 / 40
Variant: 06 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
사본을 heapify한 heap과 빈 heap에 하나씩 push한 heap에서 모두 pop하세요. (heapify 쪽 pop 결과, 반복 push 쪽 pop 결과)를 실제 두 리스트로 반환하고 원본은 보존하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
두 heap 구성 방법의 관찰 가능한 결과

구현할 함수
-----------
def heap_r06_heap_build_comparison(values: list[int]) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r06_heap_build_comparison([3, 1, 2]) == ([1, 2, 3], [1, 2, 3])
- heap_r06_heap_build_comparison([]) == ([], [])
- ((data := [2, 2, -1]), heap_r06_heap_build_comparison(data), data) == ([2, 2, -1], ([-1, 2, 2], [-1, 2, 2]), [2, 2, -1])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0726 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r06_heap_build_comparison(values: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: CI0726")


def self_test() -> None:
    assert heap_r06_heap_build_comparison([3, 1, 2]) == ([1, 2, 3], [1, 2, 3])
    assert heap_r06_heap_build_comparison([]) == ([], [])
    assert ((data := [2, 2, -1]), heap_r06_heap_build_comparison(data), data) == ([2, 2, -1], ([-1, 2, 2], [-1, 2, 2]), [2, 2, -1])
