"""
PB0674 — 필수 기능 충족 검사

Chapter: Sets
Topic: Set Operations
Seed: 68 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
available이 required의 모든 기능을 가지면 True를 반환한다.

연습 초점
---------
상위집합 비교

구현할 함수
-----------
def set_is_superset(available: set[str], required: set[str]) -> bool:

예시 및 필수 테스트
-------------------
- set_is_superset({'a', 'b'}, {'a'}) is True
- set_is_superset({'a'}, {'a', 'b'}) is False
- set_is_superset(set(), set()) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0674 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_is_superset(available: set[str], required: set[str]) -> bool:
    raise NotImplementedError("TODO: PB0674")


def self_test() -> None:
    assert set_is_superset({'a', 'b'}, {'a'}) is True
    assert set_is_superset({'a'}, {'a', 'b'}) is False
    assert set_is_superset(set(), set()) is True
