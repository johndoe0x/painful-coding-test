"""
PB0088 — 모듈 이름 만들기

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
title을 strip하고 공백으로 나눈 단어를 소문자 밑줄로 연결한 뒤 '.py'를 붙이세요.

연습 초점
---------
Python 모듈 파일 명명 관례

구현할 함수
-----------
def module_name_from_title(title: str) -> str:

예시 및 필수 테스트
-------------------
- module_name_from_title('Data Parser') == 'data_parser.py'
- module_name_from_title('') == '.py'
- module_name_from_title('  Main  App ') == 'main_app.py'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0088 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def module_name_from_title(title: str) -> str:
    raise NotImplementedError("TODO: PB0088")


def self_test() -> None:
    assert module_name_from_title('Data Parser') == 'data_parser.py'
    assert module_name_from_title('') == '.py'
    assert module_name_from_title('  Main  App ') == 'main_app.py'
