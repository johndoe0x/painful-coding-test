"""
PB0331 — 무료 배송 경계

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 fee를 5.0으로 정하고 total이 50 이상이면 if 안에서 0.0으로 바꿔 반환한다.

연습 초점
---------
if 밖에서 선언한 지역 변수를 안에서 갱신

구현할 함수
-----------
def shipping_fee(total: float) -> float:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- shipping_fee(50.0) == 0.0
- shipping_fee(10.0) == 5.0
- shipping_fee(0.0) == 5.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0331 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def shipping_fee(total: float) -> float:
    raise NotImplementedError("TODO: PB0331")


def self_test() -> None:
    assert shipping_fee(50.0) == 0.0
    assert shipping_fee(10.0) == 5.0
    assert shipping_fee(0.0) == 5.0
