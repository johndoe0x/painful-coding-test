"""
PB0066 — 잔액 변수 구성

Chapter: Variables
Topic: Variable Declaration
Seed: 07 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: assignment

문제
----
opening_balance=opening, deposit_amount=deposit, closing_balance=opening_balance+deposit_amount로 각각 선언하고 같은 이름의 키로 반환하세요.

연습 초점
---------
도메인 의미를 가진 변수 선언

구현할 함수
-----------
def declare_balance(opening: float, deposit: float) -> dict[str, float]:

필수 구현 방식
--------------
- 함수 본문에서 지역 변수 할당을 사용한다.

예시 및 필수 테스트
-------------------
- declare_balance(100, 25) == {'opening_balance': 100, 'deposit_amount': 25, 'closing_balance': 125}
- declare_balance(0, 0) == {'opening_balance': 0, 'deposit_amount': 0, 'closing_balance': 0}
- declare_balance(10, -3) == {'opening_balance': 10, 'deposit_amount': -3, 'closing_balance': 7}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0066 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def declare_balance(opening: float, deposit: float) -> dict[str, float]:
    raise NotImplementedError("TODO: PB0066")


def self_test() -> None:
    assert declare_balance(100, 25) == {'opening_balance': 100, 'deposit_amount': 25, 'closing_balance': 125}
    assert declare_balance(0, 0) == {'opening_balance': 0, 'deposit_amount': 0, 'closing_balance': 0}
    assert declare_balance(10, -3) == {'opening_balance': 10, 'deposit_amount': -3, 'closing_balance': 7}
