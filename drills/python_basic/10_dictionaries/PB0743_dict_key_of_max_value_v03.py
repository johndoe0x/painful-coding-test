"""
PB0743 — 최댓값의 key

Chapter: Dictionaries
Topic: Dict Values
Seed: 75 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 가장 큰 key를 반환한다. 동률이면 먼저 나온 key, 비어 있으면 None을 반환한다.

연습 초점
---------
items에서 안정적인 최댓값 선택

구현할 함수
-----------
def dict_key_of_max_value(mapping: dict[str, int]) -> str | None:

예시 및 필수 테스트
-------------------
- dict_key_of_max_value({'a': 1, 'b': 3}) == 'b'
- dict_key_of_max_value({}) is None
- dict_key_of_max_value({'a': 2, 'b': 2}) == 'a'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0743 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_key_of_max_value(mapping: dict[str, int]) -> str | None:
    raise NotImplementedError("TODO: PB0743")


def self_test() -> None:
    assert dict_key_of_max_value({'a': 1, 'b': 3}) == 'b'
    assert dict_key_of_max_value({}) is None
    assert dict_key_of_max_value({'a': 2, 'b': 2}) == 'a'
