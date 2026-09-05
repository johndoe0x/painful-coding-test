"""
PB0274 — 정렬된 고유 정수

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
중복을 제거하고 오름차순으로 정렬한 정수 리스트를 반환한다.

연습 초점
---------
구체적인 컬렉션 원소 타입 유지

구현할 함수
-----------
def unique_sorted_typed(values: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- unique_sorted_typed([3, 1, 3, 2]) == [1, 2, 3]
- unique_sorted_typed([]) == []
- unique_sorted_typed([-1, -2, -1]) == [-2, -1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0274 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unique_sorted_typed(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0274")


def self_test() -> None:
    assert unique_sorted_typed([3, 1, 3, 2]) == [1, 2, 3]
    assert unique_sorted_typed([]) == []
    assert unique_sorted_typed([-1, -2, -1]) == [-2, -1]
