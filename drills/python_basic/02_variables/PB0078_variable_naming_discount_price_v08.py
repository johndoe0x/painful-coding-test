"""
PB0078 — 할인 후 가격

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
discount_percentage를 0~100 비율로 해석해 할인 후 가격을 반환하세요.

연습 초점
---------
단위까지 표현한 변수명

구현할 함수
-----------
def calculate_price_after_discount(original_price: float, discount_percentage: float) -> float:

예시 및 필수 테스트
-------------------
- calculate_price_after_discount(100, 25) == 75.0
- calculate_price_after_discount(0, 50) == 0.0
- calculate_price_after_discount(80, 0) == 80.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0078 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_price_after_discount(original_price: float, discount_percentage: float) -> float:
    raise NotImplementedError("TODO: PB0078")


def self_test() -> None:
    assert calculate_price_after_discount(100, 25) == 75.0
    assert calculate_price_after_discount(0, 50) == 0.0
    assert calculate_price_after_discount(80, 0) == 80.0
