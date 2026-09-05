"""
PB0261 — 최솟값과 최댓값 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 리스트의 최솟값과 최댓값을 tuple로 반환한다.

연습 초점
---------
하나의 return으로 복수 결과 전달

구현할 함수
-----------
def min_max(numbers: list[int]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- min_max([3, 1, 8]) == (1, 8)
- min_max([5]) == (5, 5)
- min_max([-7, -2, -9]) == (-9, -2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0261 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def min_max(numbers: list[int]) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0261")


def self_test() -> None:
    assert min_max([3, 1, 8]) == (1, 8)
    assert min_max([5]) == (5, 5)
    assert min_max([-7, -2, -9]) == (-9, -2)
