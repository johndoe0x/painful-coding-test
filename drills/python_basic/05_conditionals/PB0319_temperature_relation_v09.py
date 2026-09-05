"""
PB0319 — 기준 온도 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
온도가 기준보다 낮으면 'below', 같으면 'at', 높으면 'above'를 반환한다.

연습 초점
---------
float 값의 관계 비교

구현할 함수
-----------
def temperature_relation(temperature: float, reference: float) -> str:

예시 및 필수 테스트
-------------------
- temperature_relation(18.0, 20.0) == 'below'
- temperature_relation(20.0, 20.0) == 'at'
- temperature_relation(-2.0, -5.0) == 'above'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0319 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def temperature_relation(temperature: float, reference: float) -> str:
    raise NotImplementedError("TODO: PB0319")


def self_test() -> None:
    assert temperature_relation(18.0, 20.0) == 'below'
    assert temperature_relation(20.0, 20.0) == 'at'
    assert temperature_relation(-2.0, -5.0) == 'above'
