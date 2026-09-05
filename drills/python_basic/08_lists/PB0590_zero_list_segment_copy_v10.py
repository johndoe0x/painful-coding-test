"""
PB0590 — 지정 구간을 0으로 바꾸기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 <= start <= stop <= len(values)라고 가정해 해당 반열린 구간의 원소만 0으로 바꾼 새 리스트를 반환한다.

연습 초점
---------
복사본의 연속된 여러 인덱스를 갱신한다.

구현할 함수
-----------
def zero_list_segment(values: list[int], start: int, stop: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3, 4]), zero_list_segment(items, 1, 3) == [1, 0, 0, 4] and items == [1, 2, 3, 4])[-1] is True
- zero_list_segment([5, 6], 0, 2) == [0, 0]
- zero_list_segment([1, 2], 1, 1) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0590 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def zero_list_segment(values: list[int], start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0590")


def self_test() -> None:
    assert ((items := [1, 2, 3, 4]), zero_list_segment(items, 1, 3) == [1, 0, 0, 4] and items == [1, 2, 3, 4])[-1] is True
    assert zero_list_segment([5, 6], 0, 2) == [0, 0]
    assert zero_list_segment([1, 2], 1, 1) == [1, 2]
