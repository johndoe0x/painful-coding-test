"""
PB0604 — 최댓값과 최솟값의 차이

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 values의 max(values) - min(values)를 반환한다.

연습 초점
---------
최댓값과 최솟값 함수를 결합해 산포 범위를 구한다.

구현할 함수
-----------
def list_value_range(values: list[int]) -> int:

예시 및 필수 테스트
-------------------
- list_value_range([2, 8, 5]) == 6
- list_value_range([-3, 4]) == 7
- list_value_range([9]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0604 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_value_range(values: list[int]) -> int:
    raise NotImplementedError("TODO: PB0604")


def self_test() -> None:
    assert list_value_range([2, 8, 5]) == 6
    assert list_value_range([-3, 4]) == 7
    assert list_value_range([9]) == 0
