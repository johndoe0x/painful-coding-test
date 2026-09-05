"""
PB0002 — 이름을 넣은 인사

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
name을 'Hello, <name>!' 형식의 인사말로 만드세요. 빈 이름도 그대로 처리하세요.

연습 초점
---------
매개변수와 f-string

구현할 함수
-----------
def greet_person(name: str) -> str:

예시 및 필수 테스트
-------------------
- greet_person('Ada') == 'Hello, Ada!'
- greet_person('') == 'Hello, !'
- greet_person('World') == 'Hello, World!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0002 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greet_person(name: str) -> str:
    raise NotImplementedError("TODO: PB0002")


def self_test() -> None:
    assert greet_person('Ada') == 'Hello, Ada!'
    assert greet_person('') == 'Hello, !'
    assert greet_person('World') == 'Hello, World!'
