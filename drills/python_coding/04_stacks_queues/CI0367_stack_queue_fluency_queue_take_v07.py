"""
CI0367 — deque에서 앞 N개만 소비

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 07 / 20
Time cap: 150 seconds
Source checks: deque_call

문제
----
deque.popleft로 앞에서 최대 count개를 꺼내 (꺼낸 값, 남은 값)을 반환하세요. 0<=count<=1000이며 부족하면 있는 만큼만 꺼냅니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
FIFO 소비량 경계

구현할 함수
-----------
def stack_queue_fluency_queue_take(values: list[int], count: int) -> tuple[list[int], list[int]]:

필수 구현 방식
--------------
- collections.deque를 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_fluency_queue_take([1, 2, 3], 2) == ([1, 2], [3])
- stack_queue_fluency_queue_take([1], 0) == ([], [1])
- ((_practice_1_0 := [1]), (_practice_1_1 := 3), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := stack_queue_fluency_queue_take(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ([1], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0367 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_fluency_queue_take(values: list[int], count: int) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: CI0367")


def self_test() -> None:
    assert stack_queue_fluency_queue_take([1, 2, 3], 2) == ([1, 2], [3])
    assert stack_queue_fluency_queue_take([1], 0) == ([], [1])
    assert ((_practice_1_0 := [1]), (_practice_1_1 := 3), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := stack_queue_fluency_queue_take(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ([1], [])
