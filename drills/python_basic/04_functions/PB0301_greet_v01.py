"""
PB0301 — 기본 인사말

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
prefix와 name을 '<prefix>, <name>' 형식으로 반환하며 prefix 생략 시 'Hello'를 사용한다.

연습 초점
---------
기본 인자 사용과 명시적 덮어쓰기

구현할 함수
-----------
def greet(name: str, prefix: str = 'Hello') -> str:

예시 및 필수 테스트
-------------------
- greet('Ada') == 'Hello, Ada'
- greet('Ada', 'Hi') == 'Hi, Ada'
- greet('', 'Welcome') == 'Welcome, '

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0301 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greet(name: str, prefix: str = 'Hello') -> str:
    raise NotImplementedError("TODO: PB0301")


def self_test() -> None:
    assert greet('Ada') == 'Hello, Ada'
    assert greet('Ada', 'Hi') == 'Hi, Ada'
    assert greet('', 'Welcome') == 'Welcome, '
