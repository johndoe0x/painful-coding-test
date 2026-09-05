"""
PB0727 — 두 빈도표 합치기

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 key의 count를 더해 새 딕셔너리로 반환한다.

연습 초점
---------
key별 누적 병합

구현할 함수
-----------
def dict_merge_counts(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_merge_counts({'a': 2}, {'a': 3, 'b': 1}) == {'a': 5, 'b': 1}
- dict_merge_counts({}, {}) == {}
- dict_merge_counts({'x': 0}, {'y': 2}) == {'x': 0, 'y': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0727 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_merge_counts(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0727")


def self_test() -> None:
    assert dict_merge_counts({'a': 2}, {'a': 3, 'b': 1}) == {'a': 5, 'b': 1}
    assert dict_merge_counts({}, {}) == {}
    assert dict_merge_counts({'x': 0}, {'y': 2}) == {'x': 0, 'y': 2}
