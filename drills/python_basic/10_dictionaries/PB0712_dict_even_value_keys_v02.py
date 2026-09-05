"""
PB0712 — 짝수 value의 key

Chapter: Dictionaries
Topic: Dict Looping
Seed: 72 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for, dict_items_call

문제
----
value가 짝수인 key를 입력 딕셔너리 순서대로 반환한다.

연습 초점
---------
items 순회와 조건 필터

구현할 함수
-----------
def dict_even_value_keys(mapping: dict[str, int]) -> list[str]:

필수 구현 방식
--------------
- for문을 사용한다.
- dict.items()를 사용한다.

예시 및 필수 테스트
-------------------
- dict_even_value_keys({'a': 1, 'b': 2, 'c': 4}) == ['b', 'c']
- dict_even_value_keys({}) == []
- dict_even_value_keys({'x': 3}) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0712 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_even_value_keys(mapping: dict[str, int]) -> list[str]:
    raise NotImplementedError("TODO: PB0712")


def self_test() -> None:
    assert dict_even_value_keys({'a': 1, 'b': 2, 'c': 4}) == ['b', 'c']
    assert dict_even_value_keys({}) == []
    assert dict_even_value_keys({'x': 3}) == []
