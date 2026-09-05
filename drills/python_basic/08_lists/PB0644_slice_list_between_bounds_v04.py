"""
PB0644 — 두 경계 사이 복사하기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
Python의 values[start:stop]과 같은 새 리스트를 반환한다.

연습 초점
---------
양수·음수·범위 밖 슬라이스 경계를 그대로 활용한다.

구현할 함수
-----------
def list_slice_between(values: list[int], start: int, stop: int) -> list[int]:

예시 및 필수 테스트
-------------------
- list_slice_between([0, 1, 2, 3], 1, 3) == [1, 2]
- list_slice_between([1, 2, 3], -2, 3) == [2, 3]
- list_slice_between([1, 2], 5, 9) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0644 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_slice_between(values: list[int], start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0644")


def self_test() -> None:
    assert list_slice_between([0, 1, 2, 3], 1, 3) == [1, 2]
    assert list_slice_between([1, 2, 3], -2, 3) == [2, 3]
    assert list_slice_between([1, 2], 5, 9) == []
