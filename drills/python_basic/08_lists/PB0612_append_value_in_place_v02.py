"""
PB0612 — 원본 리스트 끝에 직접 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values 자체의 끝에 value를 한 번 append하고 None을 반환한다.

연습 초점
---------
반환용 복사본을 만들지 않는 제자리 변경과 None 반환을 구분한다.

구현할 함수
-----------
def append_value_in_place(values: list[int], value: int) -> None:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2]), append_value_in_place(items, 3) is None and items == [1, 2, 3])[-1] is True
- ((items := []), append_value_in_place(items, 0) is None and items == [0])[-1] is True
- ((items := [5]), append_value_in_place(items, 5) is None and items == [5, 5])[-1] is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0612 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_value_in_place(values: list[int], value: int) -> None:
    raise NotImplementedError("TODO: PB0612")


def self_test() -> None:
    assert ((items := [1, 2]), append_value_in_place(items, 3) is None and items == [1, 2, 3])[-1] is True
    assert ((items := []), append_value_in_place(items, 0) is None and items == [0])[-1] is True
    assert ((items := [5]), append_value_in_place(items, 5) is None and items == [5, 5])[-1] is True
