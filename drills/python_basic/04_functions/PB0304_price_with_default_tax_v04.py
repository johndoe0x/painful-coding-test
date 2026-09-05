"""
PB0304 — 기본 세율 가격

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
round(price * (1 + rate), 2)로 세금 포함 가격을 센트 단위 반올림해 반환하며 rate 생략 시 0.1을 사용한다.

연습 초점
---------
float 기본값과 명시적인 소수점 반올림

구현할 함수
-----------
def price_with_default_tax(price: float, rate: float = 0.1) -> float:

예시 및 필수 테스트
-------------------
- price_with_default_tax(100.0) == 110.0
- price_with_default_tax(19.99, 0.075) == 21.49
- price_with_default_tax(50.0, 0.0) == 50.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0304 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def price_with_default_tax(price: float, rate: float = 0.1) -> float:
    raise NotImplementedError("TODO: PB0304")


def self_test() -> None:
    assert price_with_default_tax(100.0) == 110.0
    assert price_with_default_tax(19.99, 0.075) == 21.49
    assert price_with_default_tax(50.0, 0.0) == 50.0
