"""
PB0084 — 상수 이름 만들기

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
단어들을 대문자 밑줄 형식의 상수 이름으로 결합하세요.

연습 초점
---------
Python 상수의 UPPER_SNAKE_CASE 관례

구현할 함수
-----------
def to_constant_name(words: list[str]) -> str:

예시 및 필수 테스트
-------------------
- to_constant_name(['max', 'retry', 'count']) == 'MAX_RETRY_COUNT'
- to_constant_name([]) == ''
- to_constant_name(['pi']) == 'PI'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0084 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def to_constant_name(words: list[str]) -> str:
    raise NotImplementedError("TODO: PB0084")


def self_test() -> None:
    assert to_constant_name(['max', 'retry', 'count']) == 'MAX_RETRY_COUNT'
    assert to_constant_name([]) == ''
    assert to_constant_name(['pi']) == 'PI'
