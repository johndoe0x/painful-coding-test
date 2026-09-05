"""
PB0707 — 두 key의 value 교환

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 key가 모두 존재하면 복사본에서 value를 교환하고, 하나라도 없으면 복사본을 그대로 반환한다.

연습 초점
---------
membership와 다중 할당

구현할 함수
-----------
def dict_swap_key_values(mapping: dict[str, int], first: str, second: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1, 'b': 2}), dict_swap_key_values(items, 'a', 'b') == {'a': 2, 'b': 1} and items == {'a': 1, 'b': 2})[-1] is True
- dict_swap_key_values({'a': 1}, 'a', 'b') == {'a': 1}
- dict_swap_key_values({}, 'a', 'b') == {}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0707 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_swap_key_values(mapping: dict[str, int], first: str, second: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0707")


def self_test() -> None:
    assert ((items := {'a': 1, 'b': 2}), dict_swap_key_values(items, 'a', 'b') == {'a': 2, 'b': 1} and items == {'a': 1, 'b': 2})[-1] is True
    assert dict_swap_key_values({'a': 1}, 'a', 'b') == {'a': 1}
    assert dict_swap_key_values({}, 'a', 'b') == {}
