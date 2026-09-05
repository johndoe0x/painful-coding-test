"""
PB0671 — 세 가지 집합 연산

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
union, intersection, difference(left-right)를 가진 딕셔너리를 반환한다.

연습 초점
---------
합집합, 교집합, 차집합

구현할 함수
-----------
def set_report(left: set[int], right: set[int]) -> dict[str, set[int]]:

예시 및 필수 테스트
-------------------
- set_report({1, 2}, {2, 3}) == {'union': {1, 2, 3}, 'intersection': {2}, 'difference': {1}}
- set_report(set(), {1}) == {'union': {1}, 'intersection': set(), 'difference': set()}
- set_report({1}, {1}) == {'union': {1}, 'intersection': {1}, 'difference': set()}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0671 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_report(left: set[int], right: set[int]) -> dict[str, set[int]]:
    raise NotImplementedError("TODO: PB0671")


def self_test() -> None:
    assert set_report({1, 2}, {2, 3}) == {'union': {1, 2, 3}, 'intersection': {2}, 'difference': {1}}
    assert set_report(set(), {1}) == {'union': {1}, 'intersection': set(), 'difference': set()}
    assert set_report({1}, {1}) == {'union': {1}, 'intersection': {1}, 'difference': set()}
