"""
PB0195 — 쿠폰 적용 조건

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
회원이거나 주문 금액이 100 이상이면 True를 반환하세요.

연습 초점
---------
서로 다른 자격 조건의 OR

구현할 함수
-----------
def coupon_available(is_member: bool, order_total: float) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- coupon_available(False, 100) is True
- coupon_available(False, 0) is False
- coupon_available(True, 0) is True and coupon_available(True, 100) is True and coupon_available(False, 99) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0195 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def coupon_available(is_member: bool, order_total: float) -> bool:
    raise NotImplementedError("TODO: PB0195")


def self_test() -> None:
    assert coupon_available(False, 100) is True
    assert coupon_available(False, 0) is False
    assert coupon_available(True, 0) is True and coupon_available(True, 100) is True and coupon_available(False, 99) is False
