"""
PB0517 — 이름 첫 글자 연결하기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 각 단어의 첫 글자를 대문자로 바꾸어 이어 붙인다.

연습 초점
---------
인덱싱한 한 글자를 변환한 뒤 결과 문자열에 누적한다.

구현할 함수
-----------
def make_initials(words: list[str]) -> str:

예시 및 필수 테스트
-------------------
- make_initials(['ada', 'lovelace']) == 'AL'
- make_initials(['grace', '', 'hopper']) == 'GH'
- make_initials([]) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0517 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_initials(words: list[str]) -> str:
    raise NotImplementedError("TODO: PB0517")


def self_test() -> None:
    assert make_initials(['ada', 'lovelace']) == 'AL'
    assert make_initials(['grace', '', 'hopper']) == 'GH'
    assert make_initials([]) == ''
