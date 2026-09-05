"""
PB0645 — 일정 간격으로 원소 고르기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
step이 양수라고 가정해 0번 인덱스부터 step 간격의 원소를 반환한다.

연습 초점
---------
리스트 슬라이스의 보폭을 매개변수로 적용한다.

구현할 함수
-----------
def every_nth_list_item(values: list[int], step: int) -> list[int]:

예시 및 필수 테스트
-------------------
- every_nth_list_item([0, 1, 2, 3, 4], 2) == [0, 2, 4]
- every_nth_list_item([1, 2, 3, 4], 3) == [1, 4]
- every_nth_list_item([], 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0645 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def every_nth_list_item(values: list[int], step: int) -> list[int]:
    raise NotImplementedError("TODO: PB0645")


def self_test() -> None:
    assert every_nth_list_item([0, 1, 2, 3, 4], 2) == [0, 2, 4]
    assert every_nth_list_item([1, 2, 3, 4], 3) == [1, 4]
    assert every_nth_list_item([], 2) == []
