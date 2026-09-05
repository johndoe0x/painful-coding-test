"""
PB0598 — 짝수만 새 리스트에 담기

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for loop로 values의 짝수만 원래 순서대로 반환한다.

연습 초점
---------
나머지 조건과 조건부 append를 사용한다.

구현할 함수
-----------
def even_list_items(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- even_list_items([1, 2, 4, 5]) == [2, 4]
- even_list_items([-2, -1, 0]) == [-2, 0]
- even_list_items([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0598 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def even_list_items(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0598")


def self_test() -> None:
    assert even_list_items([1, 2, 4, 5]) == [2, 4]
    assert even_list_items([-2, -1, 0]) == [-2, 0]
    assert even_list_items([]) == []
