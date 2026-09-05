"""
PB0355 — 신호등 행동

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
red는 'stop', yellow는 'wait', green은 'go', 나머지는 'unknown'을 반환한다.

연습 초점
---------
문자열 동등 조건을 elif로 연결

구현할 함수
-----------
def traffic_light_action(color: str) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- traffic_light_action('red') == 'stop'
- traffic_light_action('green') == 'go'
- traffic_light_action('blue') == 'unknown'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0355 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def traffic_light_action(color: str) -> str:
    raise NotImplementedError("TODO: PB0355")


def self_test() -> None:
    assert traffic_light_action('red') == 'stop'
    assert traffic_light_action('green') == 'go'
    assert traffic_light_action('blue') == 'unknown'
