"""
PB0123 — 타입 전환 기록

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
인접한 값의 타입이 달라질 때마다 '이전->다음'을 기록하세요.

연습 초점
---------
동적 타입 변화 감지

구현할 함수
-----------
def type_transitions(values: list[object]) -> list[str]:

예시 및 필수 테스트
-------------------
- type_transitions([1, 2, 'a', 3.0]) == ['int->str', 'str->float']
- type_transitions([]) == []
- type_transitions([True, 1]) == ['bool->int']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0123 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def type_transitions(values: list[object]) -> list[str]:
    raise NotImplementedError("TODO: PB0123")


def self_test() -> None:
    assert type_transitions([1, 2, 'a', 3.0]) == ['int->str', 'str->float']
    assert type_transitions([]) == []
    assert type_transitions([True, 1]) == ['bool->int']
