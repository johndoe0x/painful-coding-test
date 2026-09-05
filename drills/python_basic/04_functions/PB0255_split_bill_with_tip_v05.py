"""
PB0255 — 인원별 결제액

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
subtotal에 tip_rate 비율의 팁을 더해 people명으로 나눈다.

연습 초점
---------
금액·비율·개수 매개변수 처리

구현할 함수
-----------
def split_bill_with_tip(subtotal: float, tip_rate: float, people: int) -> float:

예시 및 필수 테스트
-------------------
- split_bill_with_tip(100.0, 0.2, 4) == 30.0
- split_bill_with_tip(50.0, 0.0, 2) == 25.0
- split_bill_with_tip(0.0, 0.1, 3) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0255 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_bill_with_tip(subtotal: float, tip_rate: float, people: int) -> float:
    raise NotImplementedError("TODO: PB0255")


def self_test() -> None:
    assert split_bill_with_tip(100.0, 0.2, 4) == 30.0
    assert split_bill_with_tip(50.0, 0.0, 2) == 25.0
    assert split_bill_with_tip(0.0, 0.1, 3) == 0.0
