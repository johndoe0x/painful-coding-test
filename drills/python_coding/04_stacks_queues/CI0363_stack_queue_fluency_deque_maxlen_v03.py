"""
CI0363 — maxlen deque의 자동 제거

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 03 / 20
Time cap: 150 seconds
Source checks: deque_call, append_call

문제
----
0<=capacity<=1000입니다. deque(maxlen=capacity)에 values를 순서대로 append하고 최종 리스트를 반환하세요. capacity=0은 빈 리스트이며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
bounded deque 반대쪽 자동 제거

구현할 함수
-----------
def stack_queue_fluency_deque_maxlen(values: list[int], capacity: int) -> list[int]:

필수 구현 방식
--------------
- collections.deque를 사용한다.
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_fluency_deque_maxlen([1, 2, 3, 4], 2) == [3, 4]
- stack_queue_fluency_deque_maxlen([1], 0) == []
- ((_practice_1_0 := [1, 2]), (_practice_1_1 := 5), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := stack_queue_fluency_deque_maxlen(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0363 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_fluency_deque_maxlen(values: list[int], capacity: int) -> list[int]:
    raise NotImplementedError("TODO: CI0363")


def self_test() -> None:
    assert stack_queue_fluency_deque_maxlen([1, 2, 3, 4], 2) == [3, 4]
    assert stack_queue_fluency_deque_maxlen([1], 0) == []
    assert ((_practice_1_0 := [1, 2]), (_practice_1_1 := 5), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := stack_queue_fluency_deque_maxlen(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [1, 2]
