"""
CI0365 — extendleft가 뒤집는 순서

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 05 / 20
Time cap: 150 seconds
Source checks: deque_call

문제
----
deque(start)에 extendleft(additions)를 한 번 호출한 최종 리스트를 반환하세요. additions를 미리 뒤집지 않으며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
왼쪽에 차례로 넣는 순서

구현할 함수
-----------
def stack_queue_fluency_deque_extendleft(start: list[int], additions: list[int]) -> list[int]:

필수 구현 방식
--------------
- collections.deque를 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_fluency_deque_extendleft([9], [1, 2, 3]) == [3, 2, 1, 9]
- stack_queue_fluency_deque_extendleft([], []) == []
- ((_practice_1_0 := [1]), (_practice_1_1 := [2, 2]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := stack_queue_fluency_deque_extendleft(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [2, 2, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0365 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_fluency_deque_extendleft(start: list[int], additions: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0365")


def self_test() -> None:
    assert stack_queue_fluency_deque_extendleft([9], [1, 2, 3]) == [3, 2, 1, 9]
    assert stack_queue_fluency_deque_extendleft([], []) == []
    assert ((_practice_1_0 := [1]), (_practice_1_1 := [2, 2]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := stack_queue_fluency_deque_extendleft(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [2, 2, 1]
