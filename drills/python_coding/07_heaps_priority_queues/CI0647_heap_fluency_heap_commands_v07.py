"""
CI0647 — heap의 push·peek·pop

Chapter: Heaps / Priority Queues
Seed: 33 / 40
Variant: 07 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
빈 min heap에서 push, peek, pop을 순서대로 처리하세요. push에는 정수, 나머지에는 None이 주어집니다. peek와 pop 결과만 기록하고 빈 heap이면 None입니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
힙 API의 조회와 제거 구분

구현할 함수
-----------
def heap_fluency_heap_commands(operations: list[tuple[str, int | None]]) -> list[int | None]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_fluency_heap_commands([('push', 3), ('push', 1), ('peek', None), ('pop', None), ('peek', None)]) == [1, 1, 3]
- heap_fluency_heap_commands([]) == []
- ((_practice_1_0 := [('pop', None), ('push', 0), ('pop', None), ('pop', None)]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_heap_commands(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [None, 0, None]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0647 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_fluency_heap_commands(operations: list[tuple[str, int | None]]) -> list[int | None]:
    raise NotImplementedError("TODO: CI0647")


def self_test() -> None:
    assert heap_fluency_heap_commands([('push', 3), ('push', 1), ('peek', None), ('pop', None), ('peek', None)]) == [1, 1, 3]
    assert heap_fluency_heap_commands([]) == []
    assert ((_practice_1_0 := [('pop', None), ('push', 0), ('pop', None), ('pop', None)]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := heap_fluency_heap_commands(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [None, 0, None]
