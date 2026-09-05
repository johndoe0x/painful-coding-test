"""
PB0254 — 두 점 거리의 제곱

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 점 사이 거리의 제곱을 반환한다.

연습 초점
---------
네 좌표 매개변수를 올바르게 조합

구현할 함수
-----------
def point_distance_squared(x1: int, y1: int, x2: int, y2: int) -> int:

예시 및 필수 테스트
-------------------
- point_distance_squared(0, 0, 3, 4) == 25
- point_distance_squared(2, 2, 2, 2) == 0
- point_distance_squared(-1, -1, 1, 1) == 8

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0254 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def point_distance_squared(x1: int, y1: int, x2: int, y2: int) -> int:
    raise NotImplementedError("TODO: PB0254")


def self_test() -> None:
    assert point_distance_squared(0, 0, 3, 4) == 25
    assert point_distance_squared(2, 2, 2, 2) == 0
    assert point_distance_squared(-1, -1, 1, 1) == 8
