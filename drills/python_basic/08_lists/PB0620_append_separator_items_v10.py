"""
PB0620 — 원소 사이에 구분값 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values의 원소 사이에만 separator를 append한 새 리스트를 반환한다.

연습 초점
---------
첫 원소 전과 마지막 원소 뒤에는 구분값을 넣지 않는 append 순서를 설계한다.

구현할 함수
-----------
def intersperse_items(values: list[int], separator: int) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- intersperse_items([1, 2, 3], 0) == [1, 0, 2, 0, 3]
- intersperse_items([5], 9) == [5]
- intersperse_items([], 1) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0620 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def intersperse_items(values: list[int], separator: int) -> list[int]:
    raise NotImplementedError("TODO: PB0620")


def self_test() -> None:
    assert intersperse_items([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse_items([5], 9) == [5]
    assert intersperse_items([], 1) == []
