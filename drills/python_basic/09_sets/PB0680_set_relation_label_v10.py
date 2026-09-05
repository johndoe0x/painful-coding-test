"""
PB0680 — 집합 관계 이름

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 10 / 10
Time cap: 150 seconds
Source checks:

문제
----
같으면 equal, left가 진부분집합이면 subset, 진상위집합이면 superset, 그 밖은 overlap_or_disjoint를 반환한다.

연습 초점
---------
집합 동등·진부분·진상위 관계 분기

구현할 함수
-----------
def set_relation_label(left: set[int], right: set[int]) -> str:

예시 및 필수 테스트
-------------------
- set_relation_label({1}, {1}) == 'equal'
- set_relation_label({1}, {1, 2}) == 'subset'
- set_relation_label({1, 2}, {1}) == 'superset'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0680 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_relation_label(left: set[int], right: set[int]) -> str:
    raise NotImplementedError("TODO: PB0680")


def self_test() -> None:
    assert set_relation_label({1}, {1}) == 'equal'
    assert set_relation_label({1}, {1, 2}) == 'subset'
    assert set_relation_label({1, 2}, {1}) == 'superset'
