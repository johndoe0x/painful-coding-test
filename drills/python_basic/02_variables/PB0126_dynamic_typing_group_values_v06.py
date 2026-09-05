"""
PB0126 — 런타임 타입별 그룹

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
실제 타입 이름을 키로 하여 값을 입력 순서대로 그룹화하세요.

연습 초점
---------
동적 타입을 분류 키로 사용

구현할 함수
-----------
def group_by_runtime_type(values: list[object]) -> dict[str, list[object]]:

예시 및 필수 테스트
-------------------
- group_by_runtime_type([1, 'a', 2]) == {'int': [1, 2], 'str': ['a']}
- group_by_runtime_type([]) == {}
- group_by_runtime_type([True, 1]) == {'bool': [True], 'int': [1]}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0126 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def group_by_runtime_type(values: list[object]) -> dict[str, list[object]]:
    raise NotImplementedError("TODO: PB0126")


def self_test() -> None:
    assert group_by_runtime_type([1, 'a', 2]) == {'int': [1, 2], 'str': ['a']}
    assert group_by_runtime_type([]) == {}
    assert group_by_runtime_type([True, 1]) == {'bool': [True], 'int': [1]}
