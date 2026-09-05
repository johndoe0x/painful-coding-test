"""
PB0747 — value 자체의 빈도

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
mapping의 value마다 등장 횟수를 반환한다.

연습 초점
---------
values 순회와 빈도 딕셔너리

구현할 함수
-----------
def dict_value_frequencies(mapping: dict[str, int]) -> dict[int, int]:

예시 및 필수 테스트
-------------------
- dict_value_frequencies({'a': 1, 'b': 2, 'c': 1}) == {1: 2, 2: 1}
- dict_value_frequencies({}) == {}
- dict_value_frequencies({'x': 0}) == {0: 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0747 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_value_frequencies(mapping: dict[str, int]) -> dict[int, int]:
    raise NotImplementedError("TODO: PB0747")


def self_test() -> None:
    assert dict_value_frequencies({'a': 1, 'b': 2, 'c': 1}) == {1: 2, 2: 1}
    assert dict_value_frequencies({}) == {}
    assert dict_value_frequencies({'x': 0}) == {0: 1}
