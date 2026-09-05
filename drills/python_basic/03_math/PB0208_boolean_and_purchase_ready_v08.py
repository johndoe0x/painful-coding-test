"""
PB0208 — 구매 가능 상태

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
재고가 있고 balance가 price 이상일 때만 True를 반환하세요.

연습 초점
---------
상태와 금액 조건 동시 충족

구현할 함수
-----------
def can_purchase(in_stock: bool, balance: float, price: float) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- can_purchase(True, 10, 10) is True
- can_purchase(False, 100, 1) is False
- can_purchase(True, 0, 1) is False and can_purchase(False, 0, 1) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0208 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def can_purchase(in_stock: bool, balance: float, price: float) -> bool:
    raise NotImplementedError("TODO: PB0208")


def self_test() -> None:
    assert can_purchase(True, 10, 10) is True
    assert can_purchase(False, 100, 1) is False
    assert can_purchase(True, 0, 1) is False and can_purchase(False, 0, 1) is False
