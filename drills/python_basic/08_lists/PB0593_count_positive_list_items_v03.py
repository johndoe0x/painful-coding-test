"""
PB0593 — 양수 원소 개수

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for

문제
----
values를 순회해 0보다 큰 원소의 개수를 반환한다.

연습 초점
---------
반복 중 조건을 만족할 때만 카운터를 증가시킨다.

구현할 함수
-----------
def count_positive_items(values: list[int]) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- count_positive_items([-1, 0, 2, 3]) == 2
- count_positive_items([1, 1]) == 2
- count_positive_items([]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0593 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_positive_items(values: list[int]) -> int:
    raise NotImplementedError("TODO: PB0593")


def self_test() -> None:
    assert count_positive_items([-1, 0, 2, 3]) == 2
    assert count_positive_items([1, 1]) == 2
    assert count_positive_items([]) == 0
