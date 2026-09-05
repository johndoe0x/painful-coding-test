"""
PB0597 — 중첩 리스트 한 단계 펼치기

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: for

문제
----
각 안쪽 리스트를 순서대로 순회해 모든 정수를 하나의 리스트로 반환한다.

연습 초점
---------
중첩 for loop와 append로 원소 순서를 보존한다.

구현할 함수
-----------
def flatten_lists(groups: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- flatten_lists([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
- flatten_lists([[], [1], []]) == [1]
- flatten_lists([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0597 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def flatten_lists(groups: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: PB0597")


def self_test() -> None:
    assert flatten_lists([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_lists([[], [1], []]) == [1]
    assert flatten_lists([]) == []
