"""
CI0395 — 고정 길이 원형 버퍼 — 반복 세트 3

Chapter: Stacks and Queues
Seed: 20 / 40
Variant: 15 / 20
Time cap: 240 seconds
Source checks: deque_call

문제
----
deque(maxlen=capacity)에 값을 넣어 마지막 capacity개를 순서대로 반환하세요. 이 파일은 Stacks and Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
deque maxlen

구현할 함수
-----------
def stack_queue_r03_circular_buffer(values: list[int], capacity: int) -> list[int]:

필수 구현 방식
--------------
- collections.deque를 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_r03_circular_buffer([1, 2, 3, 4], 3) == [2, 3, 4]
- stack_queue_r03_circular_buffer([], 2) == []
- stack_queue_r03_circular_buffer([1, 2], 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0395 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r03_circular_buffer(values: list[int], capacity: int) -> list[int]:
    raise NotImplementedError("TODO: CI0395")


def self_test() -> None:
    assert stack_queue_r03_circular_buffer([1, 2, 3, 4], 3) == [2, 3, 4]
    assert stack_queue_r03_circular_buffer([], 2) == []
    assert stack_queue_r03_circular_buffer([1, 2], 0) == []
