"""
CI0743 — 안정적 우선순위 queue — 반복 세트 7

Chapter: Heaps / Priority Queues
Seed: 38 / 40
Variant: 03 / 20
Time cap: 240 seconds
Source checks: heapq_call

문제
----
priority가 작을수록 먼저 처리하고 동률이면 입력 순서를 유지하도록 heap tuple에 sequence를 포함하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 7이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
heap tie-break sequence

구현할 함수
-----------
def heap_r07_stable_priority(tasks: list[tuple[int, str]]) -> list[str]:

필수 구현 방식
--------------
- heapq API를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r07_stable_priority([(1, 'b'), (1, 'a'), (0, 'x')]) == ['x', 'b', 'a']
- heap_r07_stable_priority([]) == []
- heap_r07_stable_priority([(2, 'a')]) == ['a']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0743 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r07_stable_priority(tasks: list[tuple[int, str]]) -> list[str]:
    raise NotImplementedError("TODO: CI0743")


def self_test() -> None:
    assert heap_r07_stable_priority([(1, 'b'), (1, 'a'), (0, 'x')]) == ['x', 'b', 'a']
    assert heap_r07_stable_priority([]) == []
    assert heap_r07_stable_priority([(2, 'a')]) == ['a']
