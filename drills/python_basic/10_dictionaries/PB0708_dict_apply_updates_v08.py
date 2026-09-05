"""
PB0708 — 여러 갱신 순서대로 적용

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 updates를 왼쪽부터 적용한 결과를 반환한다.

연습 초점
---------
반복되는 item 할당과 마지막 값 우선

구현할 함수
-----------
def dict_apply_updates(mapping: dict[str, int], updates: list[tuple[str, int]]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- ((items := {'a': 1}), (updates := [('b', 2), ('a', 3)]), dict_apply_updates(items, updates) == {'a': 3, 'b': 2} and items == {'a': 1} and updates == [('b', 2), ('a', 3)])[-1] is True
- dict_apply_updates({}, []) == {}
- dict_apply_updates({}, [('x', 1), ('x', 2)]) == {'x': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0708 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_apply_updates(mapping: dict[str, int], updates: list[tuple[str, int]]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0708")


def self_test() -> None:
    assert ((items := {'a': 1}), (updates := [('b', 2), ('a', 3)]), dict_apply_updates(items, updates) == {'a': 3, 'b': 2} and items == {'a': 1} and updates == [('b', 2), ('a', 3)])[-1] is True
    assert dict_apply_updates({}, []) == {}
    assert dict_apply_updates({}, [('x', 1), ('x', 2)]) == {'x': 2}
