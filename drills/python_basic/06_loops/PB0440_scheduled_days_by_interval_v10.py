"""
PB0440 — 주기별 일정 날짜

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 interval로 start_day부터 end_day 이하까지 일정 날짜를 반환한다.

연습 초점
---------
포함 상한을 위한 range stop 조정

구현할 함수
-----------
def scheduled_days_by_interval(start_day: int, end_day: int, interval: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- scheduled_days_by_interval(1, 10, 3) == [1, 4, 7, 10]
- scheduled_days_by_interval(5, 4, 2) == []
- scheduled_days_by_interval(7, 7, 5) == [7]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0440 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def scheduled_days_by_interval(start_day: int, end_day: int, interval: int) -> list[int]:
    raise NotImplementedError("TODO: PB0440")


def self_test() -> None:
    assert scheduled_days_by_interval(1, 10, 3) == [1, 4, 7, 10]
    assert scheduled_days_by_interval(5, 4, 2) == []
    assert scheduled_days_by_interval(7, 7, 5) == [7]
