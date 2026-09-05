"""
PB0643 — 뒤에서 n개 복사하기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
count가 0 이상이라고 가정해 뒤 count개 원소를 반환하되 count가 0이면 []를 반환한다.

연습 초점
---------
음수 시작 인덱스와 -0 슬라이스의 특수성을 구분한다.

구현할 함수
-----------
def last_list_items(values: list[int], count: int) -> list[int]:

예시 및 필수 테스트
-------------------
- last_list_items([1, 2, 3], 2) == [2, 3]
- last_list_items([1, 2], 5) == [1, 2]
- last_list_items([1], 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0643 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def last_list_items(values: list[int], count: int) -> list[int]:
    raise NotImplementedError("TODO: PB0643")


def self_test() -> None:
    assert last_list_items([1, 2, 3], 2) == [2, 3]
    assert last_list_items([1, 2], 5) == [1, 2]
    assert last_list_items([1], 0) == []
