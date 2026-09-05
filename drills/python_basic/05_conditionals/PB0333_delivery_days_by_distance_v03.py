"""
PB0333 — 근거리 배송일

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 days를 5로 정하고 distance가 20 이하이면 if 안에서 2로 바꿔 반환한다.

연습 초점
---------
조건문 내부 할당과 함수 지역 범위

구현할 함수
-----------
def delivery_days_by_distance(distance: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- delivery_days_by_distance(20) == 2
- delivery_days_by_distance(21) == 5
- delivery_days_by_distance(0) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0333 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def delivery_days_by_distance(distance: int) -> int:
    raise NotImplementedError("TODO: PB0333")


def self_test() -> None:
    assert delivery_days_by_distance(20) == 2
    assert delivery_days_by_distance(21) == 5
    assert delivery_days_by_distance(0) == 2
