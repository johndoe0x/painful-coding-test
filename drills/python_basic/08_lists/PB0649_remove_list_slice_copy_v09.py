"""
PB0649 — 선택 구간을 제외한 리스트

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 <= start <= stop <= len(values)라고 가정해 values[start:stop]을 제외한 새 리스트를 반환한다.

연습 초점
---------
선택 구간 양옆의 슬라이스를 더해 원본을 보존한다.

구현할 함수
-----------
def remove_list_slice(values: list[int], start: int, stop: int) -> list[int]:

예시 및 필수 테스트
-------------------
- remove_list_slice([1, 2, 3, 4], 1, 3) == [1, 4]
- remove_list_slice([1, 2], 0, 2) == []
- remove_list_slice([1, 2], 1, 1) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0649 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def remove_list_slice(values: list[int], start: int, stop: int) -> list[int]:
    raise NotImplementedError("TODO: PB0649")


def self_test() -> None:
    assert remove_list_slice([1, 2, 3, 4], 1, 3) == [1, 4]
    assert remove_list_slice([1, 2], 0, 2) == []
    assert remove_list_slice([1, 2], 1, 1) == [1, 2]
