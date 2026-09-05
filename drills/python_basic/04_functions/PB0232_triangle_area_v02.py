"""
PB0232 — 삼각형 넓이

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
밑변과 높이로 삼각형 넓이를 반환한다.

연습 초점
---------
계산 책임을 하나의 함수로 선언

구현할 함수
-----------
def triangle_area(base: float, height: float) -> float:

예시 및 필수 테스트
-------------------
- triangle_area(6.0, 4.0) == 12.0
- triangle_area(0.0, 7.0) == 0.0
- triangle_area(2.5, 2.0) == 2.5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0232 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def triangle_area(base: float, height: float) -> float:
    raise NotImplementedError("TODO: PB0232")


def self_test() -> None:
    assert triangle_area(6.0, 4.0) == 12.0
    assert triangle_area(0.0, 7.0) == 0.0
    assert triangle_area(2.5, 2.0) == 2.5
