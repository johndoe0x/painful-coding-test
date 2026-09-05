"""
PB0051 — 소계 계산 설명

Chapter: Introduction
Topic: Comments
Seed: 06 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: comment

문제
----
가격 합계를 반환하고, 합계를 계산하는 이유를 설명하는 유용한 주석 한 줄을 구현 안에 작성하세요.

연습 초점
---------
무엇이 아니라 왜를 설명하는 주석

구현할 함수
-----------
def calculate_subtotal(prices: list[float]) -> float:

필수 구현 방식
--------------
- 함수 본문에 계산 이유를 설명하는 주석을 한 줄 이상 작성한다.

예시 및 필수 테스트
-------------------
- calculate_subtotal([1.5, 2.0]) == 3.5
- calculate_subtotal([]) == 0
- calculate_subtotal([0.0]) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0051 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_subtotal(prices: list[float]) -> float:
    raise NotImplementedError("TODO: PB0051")


def self_test() -> None:
    assert calculate_subtotal([1.5, 2.0]) == 3.5
    assert calculate_subtotal([]) == 0
    assert calculate_subtotal([0.0]) == 0.0
