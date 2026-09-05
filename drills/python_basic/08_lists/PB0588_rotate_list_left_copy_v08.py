"""
PB0588 — 리스트 왼쪽 회전 복사본

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
values가 비어 있으면 []를 반환하고, 아니면 amount를 길이로 나눈 나머지만큼 왼쪽으로 회전한 새 리스트를 반환한다.

연습 초점
---------
두 리스트 슬라이스를 재결합하고 원본은 수정하지 않는다.

구현할 함수
-----------
def rotate_list_items_left(values: list[int], amount: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), rotate_list_items_left(items, 1) == [2, 3, 4, 1] and items == [1, 2, 3, 4])[-1] is True
- rotate_list_items_left([1, 2, 3], 4) == [2, 3, 1]
- rotate_list_items_left([], 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0588 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rotate_list_items_left(values: list[int], amount: int) -> list[int]:
    raise NotImplementedError("TODO: PB0588")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), rotate_list_items_left(items, 1) == [2, 3, 4, 1] and items == [1, 2, 3, 4])[-1] is True
    assert rotate_list_items_left([1, 2, 3], 4) == [2, 3, 1]
    assert rotate_list_items_left([], 2) == []
