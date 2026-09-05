"""
PB0744 — 기준 초과 value 목록

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
threshold보다 큰 value를 딕셔너리 순서대로 반환한다.

연습 초점
---------
values 순회와 비교 필터

구현할 함수
-----------
def dict_values_above(mapping: dict[str, int], threshold: int) -> list[int]:

예시 및 필수 테스트
-------------------
- dict_values_above({'a': 1, 'b': 3, 'c': 2}, 1) == [3, 2]
- dict_values_above({}, 0) == []
- dict_values_above({'a': 1}, 1) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0744 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_values_above(mapping: dict[str, int], threshold: int) -> list[int]:
    raise NotImplementedError("TODO: PB0744")


def self_test() -> None:
    assert dict_values_above({'a': 1, 'b': 3, 'c': 2}, 1) == [3, 2]
    assert dict_values_above({}, 0) == []
    assert dict_values_above({'a': 1}, 1) == []
