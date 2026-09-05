"""
PB0684 — 범위에서 빠진 숫자

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
start 이상 stop 미만 정수 중 values에 없는 숫자를 반환한다.

연습 초점
---------
range를 set으로 만들고 차집합

구현할 함수
-----------
def set_missing_numbers(values: list[int], start: int, stop: int) -> set[int]:

예시 및 필수 테스트
-------------------
- set_missing_numbers([1, 3], 1, 5) == {2, 4}
- set_missing_numbers([], 0, 0) == set()
- set_missing_numbers([0, 1], 0, 2) == set()

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0684 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_missing_numbers(values: list[int], start: int, stop: int) -> set[int]:
    raise NotImplementedError("TODO: PB0684")


def self_test() -> None:
    assert set_missing_numbers([1, 3], 1, 5) == {2, 4}
    assert set_missing_numbers([], 0, 0) == set()
    assert set_missing_numbers([0, 1], 0, 2) == set()
