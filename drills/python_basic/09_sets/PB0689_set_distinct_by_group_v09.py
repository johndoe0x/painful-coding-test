"""
PB0689 — 그룹별 고유값 개수

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 그룹 리스트의 고유값 개수를 같은 key로 반환한다.

연습 초점
---------
딕셔너리 순회와 그룹별 set 변환

구현할 함수
-----------
def set_distinct_by_group(groups: dict[str, list[int]]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- set_distinct_by_group({'a': [1, 1, 2], 'b': []}) == {'a': 2, 'b': 0}
- set_distinct_by_group({}) == {}
- set_distinct_by_group({'x': [3]}) == {'x': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0689 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_distinct_by_group(groups: dict[str, list[int]]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0689")


def self_test() -> None:
    assert set_distinct_by_group({'a': [1, 1, 2], 'b': []}) == {'a': 2, 'b': 0}
    assert set_distinct_by_group({}) == {}
    assert set_distinct_by_group({'x': [3]}) == {'x': 1}
