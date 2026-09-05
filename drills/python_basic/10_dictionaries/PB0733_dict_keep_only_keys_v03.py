"""
PB0733 — 선택한 key만 유지

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
allowed에 포함된 key의 item만 유지한다.

연습 초점
---------
dict comprehension과 membership

구현할 함수
-----------
def dict_keep_only_keys(mapping: dict[str, int], allowed: set[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_keep_only_keys({'a': 1, 'b': 2}, {'b'}) == {'b': 2}
- dict_keep_only_keys({}, {'a'}) == {}
- dict_keep_only_keys({'a': 1}, set()) == {}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0733 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_keep_only_keys(mapping: dict[str, int], allowed: set[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0733")


def self_test() -> None:
    assert dict_keep_only_keys({'a': 1, 'b': 2}, {'b'}) == {'b': 2}
    assert dict_keep_only_keys({}, {'a'}) == {}
    assert dict_keep_only_keys({'a': 1}, set()) == {}
