"""
PB0577 — 두 값을 번갈아 담기

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
pairs가 0 이상이라고 가정해 [first, second] 순서를 pairs번 반복한 리스트를 반환한다.

연습 초점
---------
작은 리스트 단위의 반복과 원소 순서 보존을 연습한다.

구현할 함수
-----------
def alternating_values(first: object, second: object, pairs: int) -> list[object]:

예시 및 필수 테스트
-------------------
- alternating_values('A', 'B', 3) == ['A', 'B', 'A', 'B', 'A', 'B']
- alternating_values(1, 2, 1) == [1, 2]
- alternating_values(True, False, 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0577 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def alternating_values(first: object, second: object, pairs: int) -> list[object]:
    raise NotImplementedError("TODO: PB0577")


def self_test() -> None:
    assert alternating_values('A', 'B', 3) == ['A', 'B', 'A', 'B', 'A', 'B']
    assert alternating_values(1, 2, 1) == [1, 2]
    assert alternating_values(True, False, 0) == []
