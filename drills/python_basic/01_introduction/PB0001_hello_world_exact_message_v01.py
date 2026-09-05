"""
PB0001 — 첫 인사말

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
대소문자·쉼표·느낌표를 포함해 정확히 'Hello, world!'를 반환하세요.

연습 초점
---------
문자열 리터럴과 정확한 반환값

구현할 함수
-----------
def make_message() -> str:

예시 및 필수 테스트
-------------------
- make_message() == 'Hello, world!'
- len(make_message()) == 13
- make_message().endswith('!')

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0001 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_message() -> str:
    raise NotImplementedError("TODO: PB0001")


def self_test() -> None:
    assert make_message() == 'Hello, world!'
    assert len(make_message()) == 13
    assert make_message().endswith('!')
