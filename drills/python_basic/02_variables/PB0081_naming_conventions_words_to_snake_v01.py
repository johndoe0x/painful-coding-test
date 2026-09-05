"""
PB0081 — 단어를 snake_case로

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단어를 소문자로 바꾸고 밑줄로 연결하세요.

연습 초점
---------
Python 변수의 snake_case 관례

구현할 함수
-----------
def to_snake_case(words: list[str]) -> str:

예시 및 필수 테스트
-------------------
- to_snake_case(['First', 'User', 'Name']) == 'first_user_name'
- to_snake_case([]) == ''
- to_snake_case(['Already']) == 'already'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0081 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def to_snake_case(words: list[str]) -> str:
    raise NotImplementedError("TODO: PB0081")


def self_test() -> None:
    assert to_snake_case(['First', 'User', 'Name']) == 'first_user_name'
    assert to_snake_case([]) == ''
    assert to_snake_case(['Already']) == 'already'
