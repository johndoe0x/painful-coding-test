"""
PB0162 — 영수증 금액 계산

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
subtotal=unit_price*quantity, total=subtotal+tax를 계산해 두 키로 반환하세요.

연습 초점
---------
곱셈과 덧셈의 계산 순서

구현할 함수
-----------
def invoice_amount(unit_price: int, quantity: int, tax: int) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- invoice_amount(5, 3, 2) == {'subtotal': 15, 'total': 17}
- invoice_amount(0, 10, 0) == {'subtotal': 0, 'total': 0}
- invoice_amount(7, 1, 3) == {'subtotal': 7, 'total': 10}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0162 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def invoice_amount(unit_price: int, quantity: int, tax: int) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0162")


def self_test() -> None:
    assert invoice_amount(5, 3, 2) == {'subtotal': 15, 'total': 17}
    assert invoice_amount(0, 10, 0) == {'subtotal': 0, 'total': 0}
    assert invoice_amount(7, 1, 3) == {'subtotal': 7, 'total': 10}
