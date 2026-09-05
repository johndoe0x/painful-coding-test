"""
CI0646 — merge iterator에서 앞 K개 소비

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 06 / 20
Time cap: 240 seconds
Source checks: heapq_call, itertools_call

문제
----
각 배치는 오름차순입니다. heapq.merge(*batches)를 itertools.islice로 count개만 소비해 리스트로 반환하세요. 0<=count<=1000이며 중복을 유지하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
정렬 iterable과 제한된 소비 조합

구현할 함수
-----------
def heap_fluency_merge_islice_prefix(batches: list[list[int]], count: int) -> list[int]:

필수 구현 방식
--------------
- heapq API를 사용한다.
- itertools API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_fluency_merge_islice_prefix([[1, 4], [1, 3], []], 3) == [1, 1, 3]
- heap_fluency_merge_islice_prefix([[-1]], 0) == []
- ((_practice_1_0 := [[], [-2, 0]]), (_practice_1_1 := 9), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_merge_islice_prefix(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [-2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0646 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_fluency_merge_islice_prefix(batches: list[list[int]], count: int) -> list[int]:
    raise NotImplementedError("TODO: CI0646")


def self_test() -> None:
    assert heap_fluency_merge_islice_prefix([[1, 4], [1, 3], []], 3) == [1, 1, 3]
    assert heap_fluency_merge_islice_prefix([[-1]], 0) == []
    assert ((_practice_1_0 := [[], [-2, 0]]), (_practice_1_1 := 9), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_merge_islice_prefix(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [-2, 0]
