"""
PB0338 — 관리자 시도 횟수

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 limit를 3으로 정하고 관리자이면 if 안에서 10으로 바꿔 반환한다.

연습 초점
---------
조건문 전후 동일 지역 이름 사용

구현할 함수
-----------
def attempt_limit_for_admin(is_admin: bool) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- attempt_limit_for_admin(True) == 10
- attempt_limit_for_admin(False) == 3
- attempt_limit_for_admin(not False) == 10

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0338 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def attempt_limit_for_admin(is_admin: bool) -> int:
    raise NotImplementedError("TODO: PB0338")


def self_test() -> None:
    assert attempt_limit_for_admin(True) == 10
    assert attempt_limit_for_admin(False) == 3
    assert attempt_limit_for_admin(not False) == 10
