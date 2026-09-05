"""
PB0238 — 두 수의 중간값

Chapter: Functions
Topic: Function Declaration
Seed: 24 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 수 사이의 중간값을 반환한다.

연습 초점
---------
재사용 가능한 계산 함수 선언

구현할 함수
-----------
def number_midpoint(left: float, right: float) -> float:

예시 및 필수 테스트
-------------------
- number_midpoint(2.0, 8.0) == 5.0
- number_midpoint(-4.0, 4.0) == 0.0
- number_midpoint(3.0, 3.0) == 3.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0238 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def number_midpoint(left: float, right: float) -> float:
    raise NotImplementedError("TODO: PB0238")


def self_test() -> None:
    assert number_midpoint(2.0, 8.0) == 5.0
    assert number_midpoint(-4.0, 4.0) == 0.0
    assert number_midpoint(3.0, 3.0) == 3.0
