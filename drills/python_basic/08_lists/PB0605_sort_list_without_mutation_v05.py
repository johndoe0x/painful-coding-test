"""
PB0605 — 정렬된 새 리스트

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
values를 변경하지 않고 오름차순 또는 descending이 참이면 내림차순으로 정렬된 새 리스트를 반환한다.

연습 초점
---------
sorted의 새 리스트 반환과 reverse 인자를 사용한다.

구현할 함수
-----------
def sorted_list_copy(values: list[int], descending: bool = False) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [3, 1, 2]), sorted_list_copy(items) == [1, 2, 3] and items == [3, 1, 2])[-1] is True
- sorted_list_copy([3, 1, 2], True) == [3, 2, 1]
- sorted_list_copy([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0605 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sorted_list_copy(values: list[int], descending: bool = False) -> list[int]:
    raise NotImplementedError("TODO: PB0605")


def self_test() -> None:
    assert ((items := [3, 1, 2]), sorted_list_copy(items) == [1, 2, 3] and items == [3, 1, 2])[-1] is True
    assert sorted_list_copy([3, 1, 2], True) == [3, 2, 1]
    assert sorted_list_copy([]) == []
