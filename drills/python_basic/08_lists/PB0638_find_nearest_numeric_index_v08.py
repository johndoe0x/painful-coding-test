"""
PB0638 — 목표에 가장 가까운 값의 위치

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 values에서 target과 절댓값 차이가 가장 작은 원소의 인덱스를 반환하며 동률이면 앞 인덱스를 선택한다.

연습 초점
---------
현재 최선의 차이와 인덱스를 갱신하는 검색을 구현한다.

구현할 함수
-----------
def nearest_value_index(values: list[int], target: int) -> int:

예시 및 필수 테스트
-------------------
- nearest_value_index([1, 6, 10], 8) == 1
- nearest_value_index([2, 4], 3) == 0
- nearest_value_index([-5], 100) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0638 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def nearest_value_index(values: list[int], target: int) -> int:
    raise NotImplementedError("TODO: PB0638")


def self_test() -> None:
    assert nearest_value_index([1, 6, 10], 8) == 1
    assert nearest_value_index([2, 4], 3) == 0
    assert nearest_value_index([-5], 100) == 0
