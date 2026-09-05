"""
PB0687 — 고유한 두 수의 합

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 07 / 10
Time cap: 150 seconds
Source checks:

문제
----
서로 다른 인덱스 i<j의 두 값을 더해 가능한 합을 set으로 반환한다.

연습 초점
---------
중첩 순회와 set 누적

구현할 함수
-----------
def set_unique_pair_sums(values: list[int]) -> set[int]:

예시 및 필수 테스트
-------------------
- set_unique_pair_sums([1, 2, 3]) == {3, 4, 5}
- set_unique_pair_sums([1]) == set()
- set_unique_pair_sums([1, 1, 1]) == {2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0687 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_unique_pair_sums(values: list[int]) -> set[int]:
    raise NotImplementedError("TODO: PB0687")


def self_test() -> None:
    assert set_unique_pair_sums([1, 2, 3]) == {3, 4, 5}
    assert set_unique_pair_sums([1]) == set()
    assert set_unique_pair_sums([1, 1, 1]) == {2}
