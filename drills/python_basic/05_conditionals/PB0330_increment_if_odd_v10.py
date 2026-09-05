"""
PB0330 — 홀수만 증가

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: if

문제
----
number가 홀수일 때만 1을 더하고 아니면 그대로 반환한다.

연습 초점
---------
불린 조건 하나로 선택적 변환

구현할 함수
-----------
def increment_if_odd(number: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- increment_if_odd(3) == 4
- increment_if_odd(4) == 4
- increment_if_odd(-3) == -2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0330 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def increment_if_odd(number: int) -> int:
    raise NotImplementedError("TODO: PB0330")


def self_test() -> None:
    assert increment_if_odd(3) == 4
    assert increment_if_odd(4) == 4
    assert increment_if_odd(-3) == -2
