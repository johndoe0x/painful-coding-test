"""
CI0644 — nsmallest의 record key

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 04 / 20
Time cap: 180 seconds
Source checks: heapq_call

문제
----
heapq.nsmallest로 (이름, 점수)의 점수가 작은 count개를 반환하세요. 0<=count<=1000이고 동률은 입력 순서, count가 크면 전부 반환하며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
Top-K API의 key와 안정성

구현할 함수
-----------
def heap_fluency_nsmallest_records(records: list[tuple[str, int]], count: int) -> list[tuple[str, int]]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_fluency_nsmallest_records([('b', 2), ('a', 2), ('c', 1)], 2) == [('c', 1), ('b', 2)]
- heap_fluency_nsmallest_records([('x', 1)], 0) == []
- ((_practice_1_0 := [('x', -1), ('y', 0)]), (_practice_1_1 := 9), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_nsmallest_records(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [('x', -1), ('y', 0)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0644 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_fluency_nsmallest_records(records: list[tuple[str, int]], count: int) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: CI0644")


def self_test() -> None:
    assert heap_fluency_nsmallest_records([('b', 2), ('a', 2), ('c', 1)], 2) == [('c', 1), ('b', 2)]
    assert heap_fluency_nsmallest_records([('x', 1)], 0) == []
    assert ((_practice_1_0 := [('x', -1), ('y', 0)]), (_practice_1_1 := 9), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_nsmallest_records(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [('x', -1), ('y', 0)]
