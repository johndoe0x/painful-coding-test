"""
PB0657 — 인접 원소를 tuple로 묶기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
서로 이웃한 원소 쌍을 왼쪽부터 tuple로 만들어 반환한다.

연습 초점
---------
리스트의 관련된 두 값을 고정 길이 tuple로 표현한다.

구현할 함수
-----------
def adjacent_tuples(values: list[int]) -> list[tuple[int, int]]:

예시 및 필수 테스트
-------------------
- adjacent_tuples([1, 2, 3]) == [(1, 2), (2, 3)]
- adjacent_tuples([5]) == []
- adjacent_tuples([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0657 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def adjacent_tuples(values: list[int]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: PB0657")


def self_test() -> None:
    assert adjacent_tuples([1, 2, 3]) == [(1, 2), (2, 3)]
    assert adjacent_tuples([5]) == []
    assert adjacent_tuples([]) == []
