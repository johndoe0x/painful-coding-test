"""
PB0334 — 어린이 입장료

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 price를 20으로 정하고 age가 13 미만이면 if 안에서 10으로 바꿔 반환한다.

연습 초점
---------
분기 전 기본값 선언

구현할 함수
-----------
def ticket_price_for_child(age: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- ticket_price_for_child(12) == 10
- ticket_price_for_child(13) == 20
- ticket_price_for_child(0) == 10

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0334 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def ticket_price_for_child(age: int) -> int:
    raise NotImplementedError("TODO: PB0334")


def self_test() -> None:
    assert ticket_price_for_child(12) == 10
    assert ticket_price_for_child(13) == 20
    assert ticket_price_for_child(0) == 10
