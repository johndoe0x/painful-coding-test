"""
PB0731 — 여러 key 안전하게 제거

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 존재하는 keys만 제거한다.

연습 초점
---------
dict 복사와 pop 기본값

구현할 함수
-----------
def remove_keys(mapping: dict[str, int], keys: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1, 'b': 2}), (keys := ['a', 'x']), remove_keys(items, keys) == {'b': 2} and items == {'a': 1, 'b': 2} and keys == ['a', 'x'])[-1] is True
- remove_keys({}, ['x']) == {}
- remove_keys({'a': 1}, []) == {'a': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0731 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def remove_keys(mapping: dict[str, int], keys: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0731")


def self_test() -> None:
    assert ((items := {'a': 1, 'b': 2}), (keys := ['a', 'x']), remove_keys(items, keys) == {'b': 2} and items == {'a': 1, 'b': 2} and keys == ['a', 'x'])[-1] is True
    assert remove_keys({}, ['x']) == {}
    assert remove_keys({'a': 1}, []) == {'a': 1}
