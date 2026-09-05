"""
PB0252 — 구매 총액

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
단가*수량에 배송비를 더한 총액을 반환한다.

연습 초점
---------
타입과 의미가 다른 세 매개변수 결합

구현할 함수
-----------
def purchase_total(unit_price: float, quantity: int, shipping: float) -> float:

예시 및 필수 테스트
-------------------
- purchase_total(3.5, 2, 1.0) == 8.0
- purchase_total(9.0, 0, 2.0) == 2.0
- purchase_total(1.25, 4, 0.0) == 5.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0252 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def purchase_total(unit_price: float, quantity: int, shipping: float) -> float:
    raise NotImplementedError("TODO: PB0252")


def self_test() -> None:
    assert purchase_total(3.5, 2, 1.0) == 8.0
    assert purchase_total(9.0, 0, 2.0) == 2.0
    assert purchase_total(1.25, 4, 0.0) == 5.0
