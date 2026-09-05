"""
PB0685 — 공통값을 원래 순서로

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
values 중 allowed에 속한 값을 최초 한 번씩만 원래 순서로 반환한다.

연습 초점
---------
membership set과 중복 방지 set

구현할 함수
-----------
def set_shared_in_order(values: list[int], allowed: set[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- set_shared_in_order([3, 1, 3, 2], {1, 3}) == [3, 1]
- set_shared_in_order([], {1}) == []
- set_shared_in_order([1, 2], set()) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0685 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_shared_in_order(values: list[int], allowed: set[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0685")


def self_test() -> None:
    assert set_shared_in_order([3, 1, 3, 2], {1, 3}) == [3, 1]
    assert set_shared_in_order([], {1}) == []
    assert set_shared_in_order([1, 2], set()) == []
