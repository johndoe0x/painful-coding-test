"""
PB0031 — 이름 출력 형식

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
name을 'Hello, <name>!' 형식으로 반환하세요.

연습 초점
---------
출력할 문자열을 정확히 조립

구현할 함수
-----------
def format_greeting(name: str) -> str:

예시 및 필수 테스트
-------------------
- format_greeting('Devan') == 'Hello, Devan!'
- format_greeting('') == 'Hello, !'
- format_greeting('A B') == 'Hello, A B!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0031 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_greeting(name: str) -> str:
    raise NotImplementedError("TODO: PB0031")


def self_test() -> None:
    assert format_greeting('Devan') == 'Hello, Devan!'
    assert format_greeting('') == 'Hello, !'
    assert format_greeting('A B') == 'Hello, A B!'
