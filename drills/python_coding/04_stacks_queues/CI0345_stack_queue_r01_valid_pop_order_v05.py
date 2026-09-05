"""
CI0345 — stack pop 순서 판정 — 반복 세트 1

Chapter: Stacks and Queues
Seed: 18 / 40
Variant: 05 / 20
Time cap: 240 seconds
Source checks: append_call, pop_call

문제
----
pushed 순서로 push할 때 popped가 가능한 pop 순서인지 판정하세요. 이 파일은 Stacks and Queues 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
stack 시뮬레이션

구현할 함수
-----------
def stack_queue_r01_valid_pop_order(pushed: list[int], popped: list[int]) -> bool:

필수 구현 방식
--------------
- list.append()를 사용한다.
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_r01_valid_pop_order([1, 2, 3], [2, 3, 1]) is True
- stack_queue_r01_valid_pop_order([1, 2, 3], [3, 1, 2]) is False
- stack_queue_r01_valid_pop_order([], []) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0345 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r01_valid_pop_order(pushed: list[int], popped: list[int]) -> bool:
    raise NotImplementedError("TODO: CI0345")


def self_test() -> None:
    assert stack_queue_r01_valid_pop_order([1, 2, 3], [2, 3, 1]) is True
    assert stack_queue_r01_valid_pop_order([1, 2, 3], [3, 1, 2]) is False
    assert stack_queue_r01_valid_pop_order([], []) is True
