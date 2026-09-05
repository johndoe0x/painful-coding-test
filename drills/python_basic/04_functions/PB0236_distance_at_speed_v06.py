"""
PB0236 — 이동 거리 계산

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
속력과 시간을 곱해 이동 거리를 반환한다.

연습 초점
---------
현실 계산을 독립 함수로 선언

구현할 함수
-----------
def distance_at_speed(speed: float, hours: float) -> float:

예시 및 필수 테스트
-------------------
- distance_at_speed(60.0, 2.0) == 120.0
- distance_at_speed(10.0, 0.0) == 0.0
- distance_at_speed(2.5, 1.5) == 3.75

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0236 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def distance_at_speed(speed: float, hours: float) -> float:
    raise NotImplementedError("TODO: PB0236")


def self_test() -> None:
    assert distance_at_speed(60.0, 2.0) == 120.0
    assert distance_at_speed(10.0, 0.0) == 0.0
    assert distance_at_speed(2.5, 1.5) == 3.75
