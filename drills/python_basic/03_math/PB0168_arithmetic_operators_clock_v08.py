"""
PB0168 — 24시간 시계 이동

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
0~23시 hour에서 added_hours만큼 지난 시각을 0~23 범위로 반환하세요.

연습 초점
---------
나머지 연산으로 순환 범위 처리

구현할 함수
-----------
def clock_hour_after(hour: int, added_hours: int) -> int:

예시 및 필수 테스트
-------------------
- clock_hour_after(22, 5) == 3
- clock_hour_after(0, 0) == 0
- clock_hour_after(23, 1) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0168 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def clock_hour_after(hour: int, added_hours: int) -> int:
    raise NotImplementedError("TODO: PB0168")


def self_test() -> None:
    assert clock_hour_after(22, 5) == 3
    assert clock_hour_after(0, 0) == 0
    assert clock_hour_after(23, 1) == 0
