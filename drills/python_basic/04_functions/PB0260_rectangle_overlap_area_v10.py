"""
PB0260 — 두 직사각형 겹침 넓이

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 높이의 두 가로 구간이 겹치는 폭에 height를 곱하고, 겹치지 않으면 0을 반환한다.

연습 초점
---------
여러 경계 매개변수의 역할 분리

구현할 함수
-----------
def rectangle_overlap_area(left1: int, right1: int, left2: int, right2: int, height: int) -> int:

예시 및 필수 테스트
-------------------
- rectangle_overlap_area(0, 5, 3, 8, 2) == 4
- rectangle_overlap_area(0, 2, 2, 4, 9) == 0
- rectangle_overlap_area(-5, 5, -2, 2, 3) == 12

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0260 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rectangle_overlap_area(left1: int, right1: int, left2: int, right2: int, height: int) -> int:
    raise NotImplementedError("TODO: PB0260")


def self_test() -> None:
    assert rectangle_overlap_area(0, 5, 3, 8, 2) == 4
    assert rectangle_overlap_area(0, 2, 2, 4, 9) == 0
    assert rectangle_overlap_area(-5, 5, -2, 2, 3) == 12
