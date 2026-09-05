"""
PB0587 — 리스트 구간 교체하기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
values를 변경하지 않고 복사본의 values[start:stop] 구간을 replacement 원소들로 교체한다.

연습 초점
---------
슬라이스 할당으로 리스트 길이가 달라질 수 있음을 연습한다.

구현할 함수
-----------
def replace_list_slice(values: list[int], start: int, stop: int, replacement: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), replace_list_slice(items, 1, 3, [8, 9]) == [1, 8, 9, 4] and items == [1, 2, 3, 4])[-1] is True
- replace_list_slice([1, 2], 1, 1, [7]) == [1, 7, 2]
- replace_list_slice([1, 2, 3], 0, 3, []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0587 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_list_slice(values: list[int], start: int, stop: int, replacement: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0587")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), replace_list_slice(items, 1, 3, [8, 9]) == [1, 8, 9, 4] and items == [1, 2, 3, 4])[-1] is True
    assert replace_list_slice([1, 2], 1, 1, [7]) == [1, 7, 2]
    assert replace_list_slice([1, 2, 3], 0, 3, []) == []
