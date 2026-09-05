"""
PB0129 — 현재 slot 설명

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
현재 value를 repr 형식으로 넣어 '<타입이름>:<repr(value)>'를 반환하세요.

연습 초점
---------
어떤 타입도 받을 수 있는 변수 표현

구현할 함수
-----------
def describe_dynamic_slot(value: object) -> str:

예시 및 필수 테스트
-------------------
- describe_dynamic_slot('x') == "str:'x'"
- describe_dynamic_slot(None) == 'NoneType:None'
- describe_dynamic_slot(False) == 'bool:False'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0129 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def describe_dynamic_slot(value: object) -> str:
    raise NotImplementedError("TODO: PB0129")


def self_test() -> None:
    assert describe_dynamic_slot('x') == "str:'x'"
    assert describe_dynamic_slot(None) == 'NoneType:None'
    assert describe_dynamic_slot(False) == 'bool:False'
