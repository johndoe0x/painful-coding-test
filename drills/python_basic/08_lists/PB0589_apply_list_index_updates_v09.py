"""
PB0589 — 여러 위치 갱신하기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
updates의 인덱스가 모두 유효하다고 가정해 각 (index, value)을 순서대로 복사본에 적용한다.

연습 초점
---------
하나의 복사본에 여러 인덱스 할당을 누적하고 원본을 보존한다.

구현할 함수
-----------
def apply_list_updates(values: list[int], updates: list[tuple[int, int]]) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), apply_list_updates(items, [(0, 9), (2, 7)]) == [9, 2, 7] and items == [1, 2, 3])[-1] is True
- apply_list_updates([1, 2], [(1, 5), (1, 8)]) == [1, 8]
- apply_list_updates([], []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0589 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_list_updates(values: list[int], updates: list[tuple[int, int]]) -> list[int]:
    raise NotImplementedError("TODO: PB0589")


def self_test() -> None:
    assert ((items := [1, 2, 3]), apply_list_updates(items, [(0, 9), (2, 7)]) == [9, 2, 7] and items == [1, 2, 3])[-1] is True
    assert apply_list_updates([1, 2], [(1, 5), (1, 8)]) == [1, 8]
    assert apply_list_updates([], []) == []
