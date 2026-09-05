"""
PB0515 — 양쪽 장식 붙이기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
left, text, right 순서로 이어 붙여 반환한다.

연습 초점
---------
세 문자열의 결합 순서를 정확히 유지한다.

구현할 함수
-----------
def surround_text(text: str, left: str, right: str) -> str:

예시 및 필수 테스트
-------------------
- surround_text('title', '[', ']') == '[title]'
- surround_text('', '<', '>') == '<>'
- surround_text('x', '', '!') == 'x!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0515 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def surround_text(text: str, left: str, right: str) -> str:
    raise NotImplementedError("TODO: PB0515")


def self_test() -> None:
    assert surround_text('title', '[', ']') == '[title]'
    assert surround_text('', '<', '>') == '<>'
    assert surround_text('x', '', '!') == 'x!'
