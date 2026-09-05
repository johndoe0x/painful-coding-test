"""
PB0121 — 런타임 타입 이력

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
하나의 이름에 차례로 값이 할당된다고 보고 각 값의 런타임 타입 이름을 반환하세요.

연습 초점
---------
값에 따라 타입이 결정되는 동적 타이핑

구현할 함수
-----------
def type_history(values: list[object]) -> list[str]:

예시 및 필수 테스트
-------------------
- type_history([1, '1', 1.0]) == ['int', 'str', 'float']
- type_history([]) == []
- type_history([None]) == ['NoneType']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0121 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def type_history(values: list[object]) -> list[str]:
    raise NotImplementedError("TODO: PB0121")


def self_test() -> None:
    assert type_history([1, '1', 1.0]) == ['int', 'str', 'float']
    assert type_history([]) == []
    assert type_history([None]) == ['NoneType']
