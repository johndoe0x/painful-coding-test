"""
PB0076 — 평균 기온

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
아침과 저녁 기온의 산술평균을 반환하세요.

연습 초점
---------
역할이 구분되는 긴 변수명

구현할 함수
-----------
def calculate_average_temperature(morning_temperature: float, evening_temperature: float) -> float:

예시 및 필수 테스트
-------------------
- calculate_average_temperature(10, 20) == 15.0
- calculate_average_temperature(0, 0) == 0.0
- calculate_average_temperature(-10, 10) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0076 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_average_temperature(morning_temperature: float, evening_temperature: float) -> float:
    raise NotImplementedError("TODO: PB0076")


def self_test() -> None:
    assert calculate_average_temperature(10, 20) == 15.0
    assert calculate_average_temperature(0, 0) == 0.0
    assert calculate_average_temperature(-10, 10) == 0.0
