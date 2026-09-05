"""
PB0594 — 각 원소 제곱하기

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for loop에서 각 정수의 제곱을 새 리스트에 추가해 반환한다.

연습 초점
---------
입력 순서를 유지하며 변환 결과를 append한다.

구현할 함수
-----------
def square_list_items(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- square_list_items([1, 3, -2]) == [1, 9, 4]
- square_list_items([0]) == [0]
- square_list_items([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0594 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def square_list_items(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0594")


def self_test() -> None:
    assert square_list_items([1, 3, -2]) == [1, 9, 4]
    assert square_list_items([0]) == [0]
    assert square_list_items([]) == []
