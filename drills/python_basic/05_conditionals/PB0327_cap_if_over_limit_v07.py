"""
PB0327 — 상한 초과값 제한

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: if

문제
----
value를 기본 결과로 두고 limit보다 클 때만 limit로 바꿔 반환한다.

연습 초점
---------
상한 조건의 단일 if

구현할 함수
-----------
def cap_if_over_limit(value: int, limit: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- cap_if_over_limit(12, 10) == 10
- cap_if_over_limit(10, 10) == 10
- cap_if_over_limit(-3, 0) == -3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0327 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cap_if_over_limit(value: int, limit: int) -> int:
    raise NotImplementedError("TODO: PB0327")


def self_test() -> None:
    assert cap_if_over_limit(12, 10) == 10
    assert cap_if_over_limit(10, 10) == 10
    assert cap_if_over_limit(-3, 0) == -3
