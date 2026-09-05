"""
PB0592 — 반복문으로 리스트 곱

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for loop로 모든 정수를 곱하며 빈 리스트는 1을 반환한다.

연습 초점
---------
곱셈 누적 변수의 항등원 1을 초기값으로 사용한다.

구현할 함수
-----------
def product_list(values: list[int]) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- product_list([2, 3, 4]) == 24
- product_list([-2, 3]) == -6
- product_list([]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0592 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def product_list(values: list[int]) -> int:
    raise NotImplementedError("TODO: PB0592")


def self_test() -> None:
    assert product_list([2, 3, 4]) == 24
    assert product_list([-2, 3]) == -6
    assert product_list([]) == 1
