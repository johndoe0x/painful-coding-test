"""
PB0711 — key와 value 뒤집기

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for, dict_items_call

문제
----
value가 모두 고유하다고 가정하고 key와 value를 뒤집는다.

연습 초점
---------
items 순회와 역방향 할당

구현할 함수
-----------
def invert_dict(mapping: dict[str, int]) -> dict[int, str]:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- invert_dict({'a': 1}) == {1: 'a'}
- invert_dict({}) == {}
- invert_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0711 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def invert_dict(mapping: dict[str, int]) -> dict[int, str]:
    raise NotImplementedError("TODO: PB0711")


def self_test() -> None:
    assert invert_dict({'a': 1}) == {1: 'a'}
    assert invert_dict({}) == {}
    assert invert_dict({'a': 1, 'b': 2}) == {1: 'a', 2: 'b'}
