"""
PB0583 — 일치하는 원소 모두 바꾸기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
values는 변경하지 않고 old와 같은 모든 원소를 new로 바꾼 리스트를 반환한다.

연습 초점
---------
원소별 조건으로 변경된 새 리스트를 생성한다.

구현할 함수
-----------
def replace_list_values(values: list[int], old: int, new: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 1]), replace_list_values(items, 1, 9) == [9, 2, 9] and items == [1, 2, 1])[-1] is True
- replace_list_values([3, 4], 8, 0) == [3, 4]
- replace_list_values([], 1, 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0583 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_list_values(values: list[int], old: int, new: int) -> list[int]:
    raise NotImplementedError("TODO: PB0583")


def self_test() -> None:
    assert ((items := [1, 2, 1]), replace_list_values(items, 1, 9) == [9, 2, 9] and items == [1, 2, 1])[-1] is True
    assert replace_list_values([3, 4], 8, 0) == [3, 4]
    assert replace_list_values([], 1, 2) == []
