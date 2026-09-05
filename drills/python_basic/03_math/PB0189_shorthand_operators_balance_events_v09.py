"""
PB0189 — 입출금 복합 할당

Chapter: Math
Topic: Shorthand Operators
Seed: 19 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: augassign

문제
----
'deposit' 금액은 +=, 'withdraw' 금액은 -=로 적용하세요.

연습 초점
---------
도메인 이벤트와 복합 할당 연결

구현할 함수
-----------
def apply_balance_events(balance: float, events: list[tuple[str, float]]) -> float:

필수 구현 방식
--------------
- +=, -=, *= 같은 복합 할당 연산자를 사용한다.

예시 및 필수 테스트
-------------------
- apply_balance_events(100, [('deposit', 20), ('withdraw', 5)]) == 115
- apply_balance_events(0, []) == 0
- apply_balance_events(10, [('withdraw', 10)]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0189 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_balance_events(balance: float, events: list[tuple[str, float]]) -> float:
    raise NotImplementedError("TODO: PB0189")


def self_test() -> None:
    assert apply_balance_events(100, [('deposit', 20), ('withdraw', 5)]) == 115
    assert apply_balance_events(0, []) == 0
    assert apply_balance_events(10, [('withdraw', 10)]) == 0
