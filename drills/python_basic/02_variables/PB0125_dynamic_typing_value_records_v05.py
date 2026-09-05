"""
PB0125 — 값과 타입 기록

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 값을 {'value': 값, 'type': 실제 타입 이름} 딕셔너리로 바꿔 반환하세요.

연습 초점
---------
런타임 값과 타입의 결합

구현할 함수
-----------
def runtime_value_records(values: list[object]) -> list[dict[str, object]]:

예시 및 필수 테스트
-------------------
- runtime_value_records([1, 'x']) == [{'value': 1, 'type': 'int'}, {'value': 'x', 'type': 'str'}]
- runtime_value_records([]) == []
- runtime_value_records([None]) == [{'value': None, 'type': 'NoneType'}]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0125 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def runtime_value_records(values: list[object]) -> list[dict[str, object]]:
    raise NotImplementedError("TODO: PB0125")


def self_test() -> None:
    assert runtime_value_records([1, 'x']) == [{'value': 1, 'type': 'int'}, {'value': 'x', 'type': 'str'}]
    assert runtime_value_records([]) == []
    assert runtime_value_records([None]) == [{'value': None, 'type': 'NoneType'}]
