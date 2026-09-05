"""
PB0052 — 할인 정책 주석

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
price에서 rate 비율만큼 할인한 값을 반환하고, rate의 의미를 설명하는 주석을 작성하세요.

연습 초점
---------
도메인 규칙을 밝히는 주석

구현할 함수
-----------
def discounted_price(price: float, rate: float) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- discounted_price(100, 0.2) == 80.0
- discounted_price(0, 0.5) == 0.0
- discounted_price(50, 0) == 50.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0052 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def discounted_price(price: float, rate: float) -> float:
    raise NotImplementedError("TODO: PB0052")


def self_test() -> None:
    assert discounted_price(100, 0.2) == 80.0
    assert discounted_price(0, 0.5) == 0.0
    assert discounted_price(50, 0) == 50.0
