"""
PB0004 — 끝기호 바꾸기

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
'Hello, world' 뒤에 punctuation을 한 번 붙여 반환하세요.

연습 초점
---------
문자열 이어 붙이기

구현할 함수
-----------
def punctuate_hello(punctuation: str) -> str:

예시 및 필수 테스트
-------------------
- punctuate_hello('!') == 'Hello, world!'
- punctuate_hello('') == 'Hello, world'
- punctuate_hello('?!') == 'Hello, world?!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0004 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def punctuate_hello(punctuation: str) -> str:
    raise NotImplementedError("TODO: PB0004")


def self_test() -> None:
    assert punctuate_hello('!') == 'Hello, world!'
    assert punctuate_hello('') == 'Hello, world'
    assert punctuate_hello('?!') == 'Hello, world?!'
