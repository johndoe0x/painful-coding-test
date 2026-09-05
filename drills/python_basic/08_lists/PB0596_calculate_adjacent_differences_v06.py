"""
PB0596 — 이웃 원소 차이

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for

문제
----
각 i >= 1에 대해 values[i] - values[i-1]을 순서대로 반환한다.

연습 초점
---------
이전 원소와 현재 원소를 인덱스 반복에서 함께 읽는다.

구현할 함수
-----------
def adjacent_differences(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- adjacent_differences([3, 8, 6]) == [5, -2]
- adjacent_differences([4]) == []
- adjacent_differences([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0596 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def adjacent_differences(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0596")


def self_test() -> None:
    assert adjacent_differences([3, 8, 6]) == [5, -2]
    assert adjacent_differences([4]) == []
    assert adjacent_differences([]) == []
