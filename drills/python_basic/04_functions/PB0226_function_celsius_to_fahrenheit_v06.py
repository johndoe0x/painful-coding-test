"""
PB0226 — 섭씨 변환 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
섭씨 온도를 화씨 온도로 변환해 반환한다.

연습 초점
---------
하나의 입력으로 계산 결과 반환

구현할 함수
-----------
def function_celsius_to_fahrenheit(celsius: float) -> float:

예시 및 필수 테스트
-------------------
- function_celsius_to_fahrenheit(0.0) == 32.0
- function_celsius_to_fahrenheit(100.0) == 212.0
- function_celsius_to_fahrenheit(-40.0) == -40.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0226 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def function_celsius_to_fahrenheit(celsius: float) -> float:
    raise NotImplementedError("TODO: PB0226")


def self_test() -> None:
    assert function_celsius_to_fahrenheit(0.0) == 32.0
    assert function_celsius_to_fahrenheit(100.0) == 212.0
    assert function_celsius_to_fahrenheit(-40.0) == -40.0
