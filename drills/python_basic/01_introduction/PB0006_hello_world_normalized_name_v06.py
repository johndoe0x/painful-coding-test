"""
PB0006 — 공백을 다듬은 인사

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
name의 앞뒤 공백을 제거한 뒤 'Hello, <name>!'을 반환하세요.

연습 초점
---------
strip과 문자열 포매팅 결합

구현할 함수
-----------
def normalize_name_greeting(name: str) -> str:

예시 및 필수 테스트
-------------------
- normalize_name_greeting('  Ada ') == 'Hello, Ada!'
- normalize_name_greeting('') == 'Hello, !'
- normalize_name_greeting('  A B  ') == 'Hello, A B!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0006 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalize_name_greeting(name: str) -> str:
    raise NotImplementedError("TODO: PB0006")


def self_test() -> None:
    assert normalize_name_greeting('  Ada ') == 'Hello, Ada!'
    assert normalize_name_greeting('') == 'Hello, !'
    assert normalize_name_greeting('  A B  ') == 'Hello, A B!'
