"""
PB0079 — 수직선 거리

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
수직선 위 두 위치 사이의 절댓값 거리를 반환하세요.

연습 초점
---------
대상 간 관계를 드러내는 변수명

구현할 함수
-----------
def calculate_distance_between_points(first_position: float, second_position: float) -> float:

예시 및 필수 테스트
-------------------
- calculate_distance_between_points(2, 7) == 5
- calculate_distance_between_points(0, 0) == 0
- calculate_distance_between_points(-3, 2) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0079 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_distance_between_points(first_position: float, second_position: float) -> float:
    raise NotImplementedError("TODO: PB0079")


def self_test() -> None:
    assert calculate_distance_between_points(2, 7) == 5
    assert calculate_distance_between_points(0, 0) == 0
    assert calculate_distance_between_points(-3, 2) == 5
