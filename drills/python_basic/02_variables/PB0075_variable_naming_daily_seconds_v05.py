"""
PB0075 — 하루의 초

Chapter: Variables
Topic: Variable Naming
Seed: 08 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
하루 24시간, 한 시간 60분, 한 분 60초를 의미 있는 변수로 표현해 총 초를 반환하세요.

연습 초점
---------
매직 넘버를 설명하는 변수

구현할 함수
-----------
def calculate_seconds_in_days(number_of_days: int) -> int:

예시 및 필수 테스트
-------------------
- calculate_seconds_in_days(1) == 86400
- calculate_seconds_in_days(0) == 0
- calculate_seconds_in_days(2) == 172800

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0075 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_seconds_in_days(number_of_days: int) -> int:
    raise NotImplementedError("TODO: PB0075")


def self_test() -> None:
    assert calculate_seconds_in_days(1) == 86400
    assert calculate_seconds_in_days(0) == 0
    assert calculate_seconds_in_days(2) == 172800
