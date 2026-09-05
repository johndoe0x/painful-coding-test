"""
PB0678 — 여러 set 합치기

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
groups의 모든 set을 하나의 합집합으로 반환한다.

연습 초점
---------
반복 누적 union

구현할 함수
-----------
def set_union_many(groups: list[set[int]]) -> set[int]:

예시 및 필수 테스트
-------------------
- set_union_many([{1, 2}, {2, 3}, {4}]) == {1, 2, 3, 4}
- set_union_many([]) == set()
- set_union_many([set(), {1}]) == {1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0678 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_union_many(groups: list[set[int]]) -> set[int]:
    raise NotImplementedError("TODO: PB0678")


def self_test() -> None:
    assert set_union_many([{1, 2}, {2, 3}, {4}]) == {1, 2, 3, 4}
    assert set_union_many([]) == set()
    assert set_union_many([set(), {1}]) == {1}
