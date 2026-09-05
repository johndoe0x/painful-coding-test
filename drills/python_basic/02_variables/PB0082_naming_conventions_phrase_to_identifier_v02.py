"""
PB0082 — 문구를 식별자로

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞뒤 공백을 제거하고 공백으로 나뉜 단어를 소문자 밑줄로 연결하세요.

연습 초점
---------
사람이 읽는 문구를 Python 식별자 형식으로 변환

구현할 함수
-----------
def phrase_to_identifier(phrase: str) -> str:

예시 및 필수 테스트
-------------------
- phrase_to_identifier('User Display Name') == 'user_display_name'
- phrase_to_identifier('') == ''
- phrase_to_identifier('  One   Two ') == 'one_two'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0082 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def phrase_to_identifier(phrase: str) -> str:
    raise NotImplementedError("TODO: PB0082")


def self_test() -> None:
    assert phrase_to_identifier('User Display Name') == 'user_display_name'
    assert phrase_to_identifier('') == ''
    assert phrase_to_identifier('  One   Two ') == 'one_two'
