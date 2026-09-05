"""
PB0613 — 여러 값을 하나씩 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values의 복사본에 additions의 각 원소를 append해 반환하고 두 입력 리스트는 변경하지 않는다.

연습 초점
---------
extend 대신 반복문과 append로 여러 원소를 추가한다.

구현할 함수
-----------
def append_many(values: list[int], additions: list[int]) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1]), (extras := [2, 3]), append_many(items, extras) == [1, 2, 3] and items == [1] and extras == [2, 3])[-1] is True
- append_many([], [4]) == [4]
- append_many([1, 2], []) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0613 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_many(values: list[int], additions: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0613")


def self_test() -> None:
    assert ((items := [1]), (extras := [2, 3]), append_many(items, extras) == [1, 2, 3] and items == [1] and extras == [2, 3])[-1] is True
    assert append_many([], [4]) == [4]
    assert append_many([1, 2], []) == [1, 2]
