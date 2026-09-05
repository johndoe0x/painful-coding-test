"""
PB0617 — 처음 본 값만 추가하기

Chapter: Lists
Topic: List Append
Seed: 62 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: append_call

문제
----
values를 순회하며 결과 리스트에 아직 없는 정수만 append해 최초 등장 순서를 보존한다.

연습 초점
---------
결과 리스트 membership 검사와 append를 조합한다.

구현할 함수
-----------
def append_unique_values(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- append_unique_values([2, 1, 2, 3, 1]) == [2, 1, 3]
- append_unique_values([5, 5, 5]) == [5]
- append_unique_values([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0617 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def append_unique_values(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0617")


def self_test() -> None:
    assert append_unique_values([2, 1, 2, 3, 1]) == [2, 1, 3]
    assert append_unique_values([5, 5, 5]) == [5]
    assert append_unique_values([]) == []
