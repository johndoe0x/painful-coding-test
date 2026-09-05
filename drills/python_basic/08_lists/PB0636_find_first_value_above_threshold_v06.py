"""
PB0636 — 기준 초과 첫 위치

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
threshold보다 큰 첫 원소의 인덱스를 반환하고 없으면 -1을 반환한다.

연습 초점
---------
검색 조건이 값이 아니라 비교식인 경우의 선형 탐색을 연습한다.

구현할 함수
-----------
def first_index_above(values: list[int], threshold: int) -> int:

예시 및 필수 테스트
-------------------
- first_index_above([1, 7, 9], 5) == 1
- first_index_above([5, 5], 5) == -1
- first_index_above([], 0) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0636 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_index_above(values: list[int], threshold: int) -> int:
    raise NotImplementedError("TODO: PB0636")


def self_test() -> None:
    assert first_index_above([1, 7, 9], 5) == 1
    assert first_index_above([5, 5], 5) == -1
    assert first_index_above([], 0) == -1
