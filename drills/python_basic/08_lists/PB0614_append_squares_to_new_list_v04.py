"""
PB0614 — 제곱값을 차례로 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
빈 결과 리스트에서 시작해 values 각 원소의 제곱을 append하여 반환한다.

연습 초점
---------
원소 변환과 append를 반복해 결과 리스트를 구축한다.

구현할 함수
-----------
def append_squares(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- append_squares([1, 2, 3]) == [1, 4, 9]
- append_squares([-2, 0]) == [4, 0]
- append_squares([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0614 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_squares(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0614")


def self_test() -> None:
    assert append_squares([1, 2, 3]) == [1, 4, 9]
    assert append_squares([-2, 0]) == [4, 0]
    assert append_squares([]) == []
