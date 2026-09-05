"""
CI0386 — 두 stack으로 queue — 반복 세트 3

Chapter: Stacks and Queues
Seed: 20 / 40
Variant: 06 / 20
Time cap: 240 seconds
Source checks:

문제
----
list stack 두 개로 enqueue/dequeue를 처리하고 빈 dequeue는 None을 기록하세요. 이 파일은 Stacks and Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
두 stack의 amortized FIFO

구현할 함수
-----------
def stack_queue_r03_queue_two_stacks(operations: list[tuple[str, int | None]]) -> list[int | None]:

예시 및 필수 테스트
-------------------
- stack_queue_r03_queue_two_stacks([('enqueue', 1), ('enqueue', 2), ('dequeue', None)]) == [1]
- stack_queue_r03_queue_two_stacks([('dequeue', None)]) == [None]
- stack_queue_r03_queue_two_stacks([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0386 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r03_queue_two_stacks(operations: list[tuple[str, int | None]]) -> list[int | None]:
    raise NotImplementedError("TODO: CI0386")


def self_test() -> None:
    assert stack_queue_r03_queue_two_stacks([('enqueue', 1), ('enqueue', 2), ('dequeue', None)]) == [1]
    assert stack_queue_r03_queue_two_stacks([('dequeue', None)]) == [None]
    assert stack_queue_r03_queue_two_stacks([]) == []
