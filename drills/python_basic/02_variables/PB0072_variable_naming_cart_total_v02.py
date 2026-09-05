"""
PB0072 — 장바구니 총액

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
축약어 대신 의미 있는 변수명을 사용해 단가와 수량의 곱을 반환하세요.

연습 초점
---------
도메인을 설명하는 변수명

구현할 함수
-----------
def calculate_cart_total(unit_price: float, item_quantity: int) -> float:

예시 및 필수 테스트
-------------------
- calculate_cart_total(2.5, 4) == 10.0
- calculate_cart_total(0, 5) == 0
- calculate_cart_total(3, 1) == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0072 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_cart_total(unit_price: float, item_quantity: int) -> float:
    raise NotImplementedError("TODO: PB0072")


def self_test() -> None:
    assert calculate_cart_total(2.5, 4) == 10.0
    assert calculate_cart_total(0, 5) == 0
    assert calculate_cart_total(3, 1) == 3
