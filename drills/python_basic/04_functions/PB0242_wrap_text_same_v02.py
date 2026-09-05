"""
PB0242 — 문자열 감싸기

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
text의 앞뒤에 wrapper를 한 번씩 붙인다.

연습 초점
---------
두 문자열 매개변수 구분

구현할 함수
-----------
def wrap_text_same(text: str, wrapper: str) -> str:

예시 및 필수 테스트
-------------------
- wrap_text_same('hi', '*') == '*hi*'
- wrap_text_same('', '#') == '##'
- wrap_text_same('A', '') == 'A'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0242 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def wrap_text_same(text: str, wrapper: str) -> str:
    raise NotImplementedError("TODO: PB0242")


def self_test() -> None:
    assert wrap_text_same('hi', '*') == '*hi*'
    assert wrap_text_same('', '#') == '##'
    assert wrap_text_same('A', '') == 'A'
