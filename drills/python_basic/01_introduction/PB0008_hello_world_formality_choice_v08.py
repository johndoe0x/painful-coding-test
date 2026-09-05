"""
PB0008 — 격식에 따른 인사

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
formal이 참이면 'Good day, <name>.'을, 거짓이면 'Hi, <name>!'을 반환하세요.

연습 초점
---------
불리언에 따른 문자열 선택

구현할 함수
-----------
def choose_greeting(name: str, formal: bool) -> str:

예시 및 필수 테스트
-------------------
- choose_greeting('Ada', True) == 'Good day, Ada.'
- choose_greeting('Ada', False) == 'Hi, Ada!'
- choose_greeting('', True) == 'Good day, .'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0008 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def choose_greeting(name: str, formal: bool) -> str:
    raise NotImplementedError("TODO: PB0008")


def self_test() -> None:
    assert choose_greeting('Ada', True) == 'Good day, Ada.'
    assert choose_greeting('Ada', False) == 'Hi, Ada!'
    assert choose_greeting('', True) == 'Good day, .'
