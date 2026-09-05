"""
CI0366 — stack 추가와 여러 번 pop

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 06 / 20
Time cap: 180 seconds
Source checks: append_call, pop_call

문제
----
start 사본에 additions를 append한 뒤 count번 pop하세요. 빈 stack에서는 None을 기록합니다. 0<=count<=1000이며 (pop 기록, 최종 stack)을 반환하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
LIFO와 underflow 처리

구현할 함수
-----------
def stack_queue_fluency_stack_push_pop_batch(start: list[int], additions: list[int], count: int) -> tuple[list[int | None], list[int]]:

필수 구현 방식
--------------
- list.append()를 사용한다.
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_fluency_stack_push_pop_batch([1], [2, 3], 2) == ([3, 2], [1])
- stack_queue_fluency_stack_push_pop_batch([], [], 2) == ([None, None], [])
- ((_practice_1_0 := [7]), (_practice_1_1 := []), (_practice_1_2 := 0), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := stack_queue_fluency_stack_push_pop_batch(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == ([], [7])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0366 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_fluency_stack_push_pop_batch(start: list[int], additions: list[int], count: int) -> tuple[list[int | None], list[int]]:
    raise NotImplementedError("TODO: CI0366")


def self_test() -> None:
    assert stack_queue_fluency_stack_push_pop_batch([1], [2, 3], 2) == ([3, 2], [1])
    assert stack_queue_fluency_stack_push_pop_batch([], [], 2) == ([None, None], [])
    assert ((_practice_1_0 := [7]), (_practice_1_1 := []), (_practice_1_2 := 0), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := stack_queue_fluency_stack_push_pop_batch(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == ([], [7])
