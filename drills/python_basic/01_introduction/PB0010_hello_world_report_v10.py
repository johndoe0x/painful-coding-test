"""
PB0010 — 인사 보고서

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 name을 정확히 'Hello, <name>!' 형식으로 바꾸고 {'count': names의 길이, 'messages': 변환한 문자열 리스트}를 반환하세요.

연습 초점
---------
여러 기초 결과를 딕셔너리로 묶기

구현할 함수
-----------
def build_greeting_report(names: list[str]) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- build_greeting_report(['Ada', 'Lin']) == {'count': 2, 'messages': ['Hello, Ada!', 'Hello, Lin!']}
- build_greeting_report([]) == {'count': 0, 'messages': []}
- build_greeting_report(['']) == {'count': 1, 'messages': ['Hello, !']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0010 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_greeting_report(names: list[str]) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0010")


def self_test() -> None:
    assert build_greeting_report(['Ada', 'Lin']) == {'count': 2, 'messages': ['Hello, Ada!', 'Hello, Lin!']}
    assert build_greeting_report([]) == {'count': 0, 'messages': []}
    assert build_greeting_report(['']) == {'count': 1, 'messages': ['Hello, !']}
