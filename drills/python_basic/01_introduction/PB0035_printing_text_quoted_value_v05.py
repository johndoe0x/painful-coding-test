"""
PB0035 — 따옴표로 감싸기

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
quote를 text의 양쪽에 한 번씩 붙여 반환하세요.

연습 초점
---------
특수문자를 포함한 출력 조립

구현할 함수
-----------
def quote_text(text: str, quote: str) -> str:

예시 및 필수 테스트
-------------------
- quote_text('hello', '"') == '"hello"'
- quote_text('', "'") == "''"
- quote_text('x', '[]') == '[]x[]'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0035 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def quote_text(text: str, quote: str) -> str:
    raise NotImplementedError("TODO: PB0035")


def self_test() -> None:
    assert quote_text('hello', '"') == '"hello"'
    assert quote_text('', "'") == "''"
    assert quote_text('x', '[]') == '[]x[]'
