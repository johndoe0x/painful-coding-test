"""
PB0352 — 온도 구간

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
0 미만은 'freezing', 20 미만은 'cold', 30 미만은 'warm', 그 이상은 'hot'을 반환한다.

연습 초점
---------
연속 수치 구간을 elif로 분류

구현할 함수
-----------
def temperature_band(celsius: float) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- temperature_band(-1.0) == 'freezing'
- temperature_band(20.0) == 'warm'
- temperature_band(30.0) == 'hot'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0352 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def temperature_band(celsius: float) -> str:
    raise NotImplementedError("TODO: PB0352")


def self_test() -> None:
    assert temperature_band(-1.0) == 'freezing'
    assert temperature_band(20.0) == 'warm'
    assert temperature_band(30.0) == 'hot'
