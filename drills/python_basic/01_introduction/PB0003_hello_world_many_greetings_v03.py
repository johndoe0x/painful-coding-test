"""
PB0003 — 여러 사람에게 인사

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 이름을 'Hello, <name>!' 형식으로 바꾼 새 리스트를 순서대로 반환하세요.

연습 초점
---------
리스트 입력을 문자열 리스트로 변환

구현할 함수
-----------
def greet_people(names: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- greet_people(['Ada', 'Lin']) == ['Hello, Ada!', 'Hello, Lin!']
- greet_people([]) == []
- greet_people(['']) == ['Hello, !']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0003 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greet_people(names: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0003")


def self_test() -> None:
    assert greet_people(['Ada', 'Lin']) == ['Hello, Ada!', 'Hello, Lin!']
    assert greet_people([]) == []
    assert greet_people(['']) == ['Hello, !']
