"""
PB0237 — 할인 금액 계산

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
가격과 할인율(퍼센트)로 할인 금액을 반환한다.

연습 초점
---------
입력과 결과의 의미가 드러나는 선언

구현할 함수
-----------
def discount_value(price: float, percent: float) -> float:

예시 및 필수 테스트
-------------------
- discount_value(200.0, 10.0) == 20.0
- discount_value(50.0, 0.0) == 0.0
- discount_value(80.0, 25.0) == 20.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0237 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def discount_value(price: float, percent: float) -> float:
    raise NotImplementedError("TODO: PB0237")


def self_test() -> None:
    assert discount_value(200.0, 10.0) == 20.0
    assert discount_value(50.0, 0.0) == 0.0
    assert discount_value(80.0, 25.0) == 20.0
