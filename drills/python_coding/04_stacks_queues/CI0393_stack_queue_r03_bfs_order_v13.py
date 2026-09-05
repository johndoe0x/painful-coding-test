"""
CI0393 — deque BFS 순회 — 반복 세트 3

Chapter: Stacks and Queues
Seed: 20 / 40
Variant: 13 / 20
Time cap: 240 seconds
Source checks: deque_call

문제
----
collections.deque로 start부터 BFS 방문 순서를 반환하고 이웃은 주어진 순서를 따르세요. 각 정점은 한 번만 방문하며 key가 없는 정점의 이웃은 빈 목록입니다. 이 파일은 Stacks and Queues 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
FIFO graph traversal과 순환·합류 처리

구현할 함수
-----------
def stack_queue_r03_bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:

필수 구현 방식
--------------
- collections.deque를 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_r03_bfs_order({'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': []}, 'a') == ['a', 'b', 'c', 'd']
- stack_queue_r03_bfs_order({'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['d']}, 'a') == ['a', 'b', 'c', 'd']
- stack_queue_r03_bfs_order({}, 'x') == ['x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0393 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r03_bfs_order(graph: dict[str, list[str]], start: str) -> list[str]:
    raise NotImplementedError("TODO: CI0393")


def self_test() -> None:
    assert stack_queue_r03_bfs_order({'a': ['b', 'c'], 'b': ['d'], 'c': [], 'd': []}, 'a') == ['a', 'b', 'c', 'd']
    assert stack_queue_r03_bfs_order({'a': ['b', 'c'], 'b': ['a', 'd'], 'c': ['d']}, 'a') == ['a', 'b', 'c', 'd']
    assert stack_queue_r03_bfs_order({}, 'x') == ['x']
