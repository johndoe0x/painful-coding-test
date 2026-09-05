"""
PB0611 — 없는 값만 복사본에 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
value가 values에 없을 때만 복사본 끝에 추가하고 원본은 변경하지 않는다.

연습 초점
---------
membership 검사 후 복사본에 append하는 조건부 갱신을 연습한다.

구현할 함수
-----------
def append_if_missing(values: list[int], value: int) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- ((items := [1, 2]), append_if_missing(items, 3) == [1, 2, 3] and items == [1, 2])[-1] is True
- append_if_missing([1, 2], 2) == [1, 2]
- append_if_missing([], 5) == [5]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0611 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_if_missing(values: list[int], value: int) -> list[int]:
    raise NotImplementedError("TODO: PB0611")


def self_test() -> None:
    assert ((items := [1, 2]), append_if_missing(items, 3) == [1, 2, 3] and items == [1, 2])[-1] is True
    assert append_if_missing([1, 2], 2) == [1, 2]
    assert append_if_missing([], 5) == [5]
