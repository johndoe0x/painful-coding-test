"""
PB0009 — 이름이 있을 때만 인사

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
name이 빈 문자열이면 'Hello!'를, 아니면 'Hello, <name>!'을 반환하세요.

연습 초점
---------
빈 문자열 경계 처리

구현할 함수
-----------
def greet_if_present(name: str) -> str:

예시 및 필수 테스트
-------------------
- greet_if_present('Ada') == 'Hello, Ada!'
- greet_if_present('') == 'Hello!'
- greet_if_present('0') == 'Hello, 0!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0009 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greet_if_present(name: str) -> str:
    raise NotImplementedError("TODO: PB0009")


def self_test() -> None:
    assert greet_if_present('Ada') == 'Hello, Ada!'
    assert greet_if_present('') == 'Hello!'
    assert greet_if_present('0') == 'Hello, 0!'
