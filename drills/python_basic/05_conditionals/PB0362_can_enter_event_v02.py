"""
PB0362 — 행사 입장 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
행사장이 열려 있고 티켓이 있거나 초대 명단에 있으면 True를 반환한다.

연습 초점
---------
and·or 우선순위를 괄호로 표현

구현할 함수
-----------
def can_enter_event(has_ticket: bool, on_guest_list: bool, venue_open: bool) -> bool:

예시 및 필수 테스트
-------------------
- can_enter_event(True, False, True) is True
- can_enter_event(False, True, True) is True
- can_enter_event(True, True, False) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0362 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def can_enter_event(has_ticket: bool, on_guest_list: bool, venue_open: bool) -> bool:
    raise NotImplementedError("TODO: PB0362")


def self_test() -> None:
    assert can_enter_event(True, False, True) is True
    assert can_enter_event(False, True, True) is True
    assert can_enter_event(True, True, False) is False
