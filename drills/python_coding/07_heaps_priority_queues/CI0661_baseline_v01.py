"""
CI0661 — Heapify — 기본 계약

Chapter: Heaps / Priority Queues
Seed: 34 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks: heapq_call

문제
----
사본을 heapify하고 최솟값을 반환한다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def smallest_after_heapify(values: list[int]) -> int | None:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- smallest_after_heapify([]) is None
- smallest_after_heapify([4, 2, 3]) == 2
- smallest_after_heapify([-1, -3]) == -3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0661 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def smallest_after_heapify(values: list[int]) -> int | None:
    raise NotImplementedError("TODO: CI0661")


def self_test() -> None:
    assert smallest_after_heapify([]) is None
    assert smallest_after_heapify([4, 2, 3]) == 2
    assert smallest_after_heapify([-1, -3]) == -3
