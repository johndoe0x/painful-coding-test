"""
PB0234 — 원 넓이 계산

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
원주율을 3.14로 사용해 원의 넓이를 반환한다.

연습 초점
---------
명세를 함수 본문으로 옮기기

구현할 함수
-----------
def circle_area_314(radius: float) -> float:

예시 및 필수 테스트
-------------------
- circle_area_314(2.0) == 12.56
- circle_area_314(0.0) == 0.0
- circle_area_314(10.0) == 314.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0234 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def circle_area_314(radius: float) -> float:
    raise NotImplementedError("TODO: PB0234")


def self_test() -> None:
    assert circle_area_314(2.0) == 12.56
    assert circle_area_314(0.0) == 0.0
    assert circle_area_314(10.0) == 314.0
