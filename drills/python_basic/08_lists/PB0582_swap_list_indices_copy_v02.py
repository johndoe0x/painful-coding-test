"""
PB0582 — 복사본에서 두 원소 맞바꾸기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 인덱스가 유효하다고 가정해 values의 복사본에서 두 원소의 위치를 바꾸어 반환한다.

연습 초점
---------
리스트 복사와 다중 할당을 함께 사용한다.

구현할 함수
-----------
def swap_list_items(values: list[int], first: int, second: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), swap_list_items(items, 0, 2) == [3, 2, 1] and items == [1, 2, 3])[-1] is True
- swap_list_items([4, 5], 1, 1) == [4, 5]
- swap_list_items([1, 2, 3], -1, 0) == [3, 2, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0582 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def swap_list_items(values: list[int], first: int, second: int) -> list[int]:
    raise NotImplementedError("TODO: PB0582")


def self_test() -> None:
    assert ((items := [1, 2, 3]), swap_list_items(items, 0, 2) == [3, 2, 1] and items == [1, 2, 3])[-1] is True
    assert swap_list_items([4, 5], 1, 1) == [4, 5]
    assert swap_list_items([1, 2, 3], -1, 0) == [3, 2, 1]
