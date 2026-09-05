"""
PB0335 — 연속 출석 보너스

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 points를 days로 정하고 days가 7 이상이면 if 안에서 10을 더해 반환한다.

연습 초점
---------
if 블록의 지역 변수 갱신

구현할 함수
-----------
def bonus_points_for_streak(days: int) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- bonus_points_for_streak(7) == 17
- bonus_points_for_streak(6) == 6
- bonus_points_for_streak(0) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0335 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def bonus_points_for_streak(days: int) -> int:
    raise NotImplementedError("TODO: PB0335")


def self_test() -> None:
    assert bonus_points_for_streak(7) == 17
    assert bonus_points_for_streak(6) == 6
    assert bonus_points_for_streak(0) == 0
