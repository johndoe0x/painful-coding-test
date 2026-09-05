"""
PB0647 — 일정 크기 조각으로 나누기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
size가 양수라고 가정해 values를 최대 size개씩의 연속된 새 리스트들로 나눈다.

연습 초점
---------
range의 step과 리스트 슬라이스를 조합해 마지막 짧은 조각까지 처리한다.

구현할 함수
-----------
def chunk_list(values: list[int], size: int) -> list[list[int]]:

예시 및 필수 테스트
-------------------
- chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
- chunk_list([1, 2], 5) == [[1, 2]]
- chunk_list([], 3) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0647 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def chunk_list(values: list[int], size: int) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0647")


def self_test() -> None:
    assert chunk_list([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list([1, 2], 5) == [[1, 2]]
    assert chunk_list([], 3) == []
