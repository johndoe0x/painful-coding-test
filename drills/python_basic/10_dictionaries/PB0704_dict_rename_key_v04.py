"""
PB0704 — key 이름 바꾸기

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 04 / 10
Time cap: 150 seconds
Source checks:

문제
----
원본을 바꾸지 않고 old가 존재하면 그 value를 new key로 옮긴다. old가 없으면 복사본을 그대로 반환한다.

연습 초점
---------
membership, pop, 재할당

구현할 함수
-----------
def dict_rename_key(mapping: dict[str, int], old: str, new: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1}), dict_rename_key(items, 'a', 'b') == {'b': 1} and items == {'a': 1})[-1] is True
- dict_rename_key({'a': 1}, 'x', 'b') == {'a': 1}
- dict_rename_key({'a': 1, 'b': 2}, 'a', 'b') == {'b': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0704 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_rename_key(mapping: dict[str, int], old: str, new: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0704")


def self_test() -> None:
    assert ((items := {'a': 1}), dict_rename_key(items, 'a', 'b') == {'b': 1} and items == {'a': 1})[-1] is True
    assert dict_rename_key({'a': 1}, 'x', 'b') == {'a': 1}
    assert dict_rename_key({'a': 1, 'b': 2}, 'a', 'b') == {'b': 1}
