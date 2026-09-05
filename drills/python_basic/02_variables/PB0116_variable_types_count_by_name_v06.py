"""
PB0116 — 타입별 개수

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 실제 타입 이름별 개수를 딕셔너리로 반환하세요.

연습 초점
---------
여러 런타임 타입 집계

구현할 함수
-----------
def count_value_types(values: list[object]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- count_value_types([1, True, 2, 'x']) == {'int': 2, 'bool': 1, 'str': 1}
- count_value_types([]) == {}
- count_value_types([None]) == {'NoneType': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0116 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_value_types(values: list[object]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0116")


def self_test() -> None:
    assert count_value_types([1, True, 2, 'x']) == {'int': 2, 'bool': 1, 'str': 1}
    assert count_value_types([]) == {}
    assert count_value_types([None]) == {'NoneType': 1}
