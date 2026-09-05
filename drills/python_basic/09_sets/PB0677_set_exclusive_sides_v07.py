"""
PB0677 — 좌우 전용 원소 분리

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
left_only와 right_only 차집합을 딕셔너리로 반환한다.

연습 초점
---------
양방향 차집합

구현할 함수
-----------
def set_exclusive_sides(left: set[int], right: set[int]) -> dict[str, set[int]]:

예시 및 필수 테스트
-------------------
- set_exclusive_sides({1, 2}, {2, 3}) == {'left_only': {1}, 'right_only': {3}}
- set_exclusive_sides(set(), {1}) == {'left_only': set(), 'right_only': {1}}
- set_exclusive_sides({1}, {1}) == {'left_only': set(), 'right_only': set()}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0677 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_exclusive_sides(left: set[int], right: set[int]) -> dict[str, set[int]]:
    raise NotImplementedError("TODO: PB0677")


def self_test() -> None:
    assert set_exclusive_sides({1, 2}, {2, 3}) == {'left_only': {1}, 'right_only': {3}}
    assert set_exclusive_sides(set(), {1}) == {'left_only': set(), 'right_only': {1}}
    assert set_exclusive_sides({1}, {1}) == {'left_only': set(), 'right_only': set()}
