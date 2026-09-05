"""
CI0642 — heappushpop의 반환값

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 02 / 20
Time cap: 180 seconds
Source checks: heapq_call, sorted_call

문제
----
사본을 heapify한 뒤 heappushpop(incoming)을 한 번 호출하세요. (꺼낸 값, 남은 값을 오름차순 정렬한 리스트)를 반환하고 입력은 보존합니다. 빈 heap도 처리합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
push 후 최소값 pop 결합

구현할 함수
-----------
def heap_fluency_heap_pushpop_contract(values: list[int], incoming: int) -> tuple[int, list[int]]:

필수 구현 방식
--------------
- heapq API를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- heap_fluency_heap_pushpop_contract([2, 4], 1) == (1, [2, 4])
- heap_fluency_heap_pushpop_contract([], 3) == (3, [])
- ((_practice_1_0 := [2, 4]), (_practice_1_1 := 5), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_heap_pushpop_contract(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (2, [4, 5])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0642 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_fluency_heap_pushpop_contract(values: list[int], incoming: int) -> tuple[int, list[int]]:
    raise NotImplementedError("TODO: CI0642")


def self_test() -> None:
    assert heap_fluency_heap_pushpop_contract([2, 4], 1) == (1, [2, 4])
    assert heap_fluency_heap_pushpop_contract([], 3) == (3, [])
    assert ((_practice_1_0 := [2, 4]), (_practice_1_1 := 5), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_heap_pushpop_contract(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (2, [4, 5])
