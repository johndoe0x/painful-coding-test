"""
PB0718 — 같은 value의 key 묶기

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 08 / 10
Time cap: 150 seconds
Source checks: for, dict_items_call

문제
----
value별로 key 목록을 딕셔너리 입력 순서대로 묶는다.

연습 초점
---------
items 순회와 setdefault 리스트 누적

구현할 함수
-----------
def dict_group_keys_by_value(mapping: dict[str, int]) -> dict[int, list[str]]:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- dict_group_keys_by_value({'a': 1, 'b': 2, 'c': 1}) == {1: ['a', 'c'], 2: ['b']}
- dict_group_keys_by_value({}) == {}
- dict_group_keys_by_value({'x': 0}) == {0: ['x']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0718 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_group_keys_by_value(mapping: dict[str, int]) -> dict[int, list[str]]:
    raise NotImplementedError("TODO: PB0718")


def self_test() -> None:
    assert dict_group_keys_by_value({'a': 1, 'b': 2, 'c': 1}) == {1: ['a', 'c'], 2: ['b']}
    assert dict_group_keys_by_value({}) == {}
    assert dict_group_keys_by_value({'x': 0}) == {0: ['x']}
