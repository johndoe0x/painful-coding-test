"""
PB0672 — 한쪽에만 있는 값

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 set 중 정확히 한쪽에만 존재하는 값을 반환한다.

연습 초점
---------
대칭차집합

구현할 함수
-----------
def set_symmetric_only(left: set[str], right: set[str]) -> set[str]:

예시 및 필수 테스트
-------------------
- set_symmetric_only({'a', 'b'}, {'b', 'c'}) == {'a', 'c'}
- set_symmetric_only(set(), {'x'}) == {'x'}
- set_symmetric_only({'x'}, {'x'}) == set()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0672 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_symmetric_only(left: set[str], right: set[str]) -> set[str]:
    raise NotImplementedError("TODO: PB0672")


def self_test() -> None:
    assert set_symmetric_only({'a', 'b'}, {'b', 'c'}) == {'a', 'c'}
    assert set_symmetric_only(set(), {'x'}) == {'x'}
    assert set_symmetric_only({'x'}, {'x'}) == set()
