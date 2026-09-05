"""
PB0458 — 모든 두 리스트 합

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
각 left 원소마다 모든 right 원소와의 합을 한 행으로 만들어 반환한다.

연습 초점
---------
바깥 입력과 안쪽 입력의 조합

구현할 함수
-----------
def all_pair_sums_nested(left: list[int], right: list[int]) -> list[list[int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- all_pair_sums_nested([1, 2], [10, 20]) == [[11, 21], [12, 22]]
- all_pair_sums_nested([], [1]) == []
- all_pair_sums_nested([3], []) == [[]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0458 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def all_pair_sums_nested(left: list[int], right: list[int]) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0458")


def self_test() -> None:
    assert all_pair_sums_nested([1, 2], [10, 20]) == [[11, 21], [12, 22]]
    assert all_pair_sums_nested([], [1]) == []
    assert all_pair_sums_nested([3], []) == [[]]
