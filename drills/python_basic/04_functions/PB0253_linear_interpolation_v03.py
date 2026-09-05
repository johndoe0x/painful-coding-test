"""
PB0253 — 선형 보간

Chapter: Functions
Topic: Multiple Parameters
Seed: 26 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
start + (end-start)*ratio를 반환한다.

연습 초점
---------
여러 인자의 수학적 관계 표현

구현할 함수
-----------
def linear_interpolation(start: float, end: float, ratio: float) -> float:

예시 및 필수 테스트
-------------------
- linear_interpolation(0.0, 10.0, 0.3) == 3.0
- linear_interpolation(5.0, 9.0, 0.0) == 5.0
- linear_interpolation(-10.0, 10.0, 0.5) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0253 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def linear_interpolation(start: float, end: float, ratio: float) -> float:
    raise NotImplementedError("TODO: PB0253")


def self_test() -> None:
    assert linear_interpolation(0.0, 10.0, 0.3) == 3.0
    assert linear_interpolation(5.0, 9.0, 0.0) == 5.0
    assert linear_interpolation(-10.0, 10.0, 0.5) == 0.0
