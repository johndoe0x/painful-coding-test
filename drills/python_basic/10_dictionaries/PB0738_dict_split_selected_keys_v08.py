"""
PB0738 — 선택 key와 나머지 분리

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 08 / 10
Time cap: 150 seconds
Source checks:

문제
----
selected에 포함된 item은 selected 딕셔너리, 나머지는 remaining 딕셔너리에 담는다.

연습 초점
---------
하나의 딕셔너리를 두 딕셔너리로 분기

구현할 함수
-----------
def dict_split_selected_keys(mapping: dict[str, int], selected: set[str]) -> dict[str, dict[str, int]]:

예시 및 필수 테스트
-------------------
- dict_split_selected_keys({'a': 1, 'b': 2}, {'a'}) == {'selected': {'a': 1}, 'remaining': {'b': 2}}
- dict_split_selected_keys({}, {'a'}) == {'selected': {}, 'remaining': {}}
- dict_split_selected_keys({'a': 1}, set()) == {'selected': {}, 'remaining': {'a': 1}}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0738 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_split_selected_keys(mapping: dict[str, int], selected: set[str]) -> dict[str, dict[str, int]]:
    raise NotImplementedError("TODO: PB0738")


def self_test() -> None:
    assert dict_split_selected_keys({'a': 1, 'b': 2}, {'a'}) == {'selected': {'a': 1}, 'remaining': {'b': 2}}
    assert dict_split_selected_keys({}, {'a'}) == {'selected': {}, 'remaining': {}}
    assert dict_split_selected_keys({'a': 1}, set()) == {'selected': {}, 'remaining': {'a': 1}}
