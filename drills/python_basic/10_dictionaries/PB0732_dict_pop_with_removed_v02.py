"""
PB0732 — 제거 결과와 value 반환

Chapter: Dictionaries
Topic: Dict Remove
Seed: 74 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 key를 제거한 딕셔너리와 제거된 value를 반환한다. key가 없으면 value는 None이다.

연습 초점
---------
pop과 반환값 처리

구현할 함수
-----------
def dict_pop_with_removed(mapping: dict[str, int], key: str) -> tuple[dict[str, int], int | None]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1, 'b': 2}), dict_pop_with_removed(items, 'a') == ({'b': 2}, 1) and items == {'a': 1, 'b': 2})[-1] is True
- dict_pop_with_removed({'a': 1}, 'x') == ({'a': 1}, None)
- dict_pop_with_removed({}, 'x') == ({}, None)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0732 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_pop_with_removed(mapping: dict[str, int], key: str) -> tuple[dict[str, int], int | None]:
    raise NotImplementedError("TODO: PB0732")


def self_test() -> None:
    assert ((items := {'a': 1, 'b': 2}), dict_pop_with_removed(items, 'a') == ({'b': 2}, 1) and items == {'a': 1, 'b': 2})[-1] is True
    assert dict_pop_with_removed({'a': 1}, 'x') == ({'a': 1}, None)
    assert dict_pop_with_removed({}, 'x') == ({}, None)
