"""
PB0365 — 무료배송 복합 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
total이 50 이상이거나, 회원이면서 쿠폰이 있으면 True를 반환한다.

연습 초점
---------
or 양쪽에 다른 형태의 조건 배치

구현할 함수
-----------
def qualifies_free_shipping(total: float, is_member: bool, has_coupon: bool) -> bool:

예시 및 필수 테스트
-------------------
- qualifies_free_shipping(50.0, False, False) is True
- qualifies_free_shipping(20.0, True, True) is True
- qualifies_free_shipping(20.0, True, False) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0365 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def qualifies_free_shipping(total: float, is_member: bool, has_coupon: bool) -> bool:
    raise NotImplementedError("TODO: PB0365")


def self_test() -> None:
    assert qualifies_free_shipping(50.0, False, False) is True
    assert qualifies_free_shipping(20.0, True, True) is True
    assert qualifies_free_shipping(20.0, True, False) is False
