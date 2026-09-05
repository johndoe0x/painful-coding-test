"""
PB0646 — 리스트를 절반으로 나누기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
len(values) // 2를 경계로 두 새 리스트를 반환하며 홀수 길이의 가운데 원소는 오른쪽에 포함한다.

연습 초점
---------
계산한 중간 인덱스로 서로 겹치지 않는 두 슬라이스를 만든다.

구현할 함수
-----------
def split_list_halves(values: list[int]) -> tuple[list[int], list[int]]:

예시 및 필수 테스트
-------------------
- split_list_halves([1, 2, 3, 4]) == ([1, 2], [3, 4])
- split_list_halves([1, 2, 3]) == ([1], [2, 3])
- split_list_halves([]) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0646 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_list_halves(values: list[int]) -> tuple[list[int], list[int]]:
    raise NotImplementedError("TODO: PB0646")


def self_test() -> None:
    assert split_list_halves([1, 2, 3, 4]) == ([1, 2], [3, 4])
    assert split_list_halves([1, 2, 3]) == ([1], [2, 3])
    assert split_list_halves([]) == ([], [])
