"""
CI0384 — 용량 제한 stack — 반복 세트 3

Chapter: Stacks and Queues
Seed: 20 / 40
Variant: 04 / 20
Time cap: 240 seconds
Source checks:

문제
----
값을 차례로 push하되 capacity를 넘으면 가장 아래의 오래된 값을 제거해 최종 stack을 반환하세요. 이 파일은 Stacks and Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
bounded LIFO 저장소

구현할 함수
-----------
def stack_queue_r03_bounded_stack(values: list[int], capacity: int) -> list[int]:

예시 및 필수 테스트
-------------------
- stack_queue_r03_bounded_stack([1, 2, 3], 2) == [2, 3]
- stack_queue_r03_bounded_stack([], 3) == []
- stack_queue_r03_bounded_stack([1, 2], 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0384 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r03_bounded_stack(values: list[int], capacity: int) -> list[int]:
    raise NotImplementedError("TODO: CI0384")


def self_test() -> None:
    assert stack_queue_r03_bounded_stack([1, 2, 3], 2) == [2, 3]
    assert stack_queue_r03_bounded_stack([], 3) == []
    assert stack_queue_r03_bounded_stack([1, 2], 0) == []
