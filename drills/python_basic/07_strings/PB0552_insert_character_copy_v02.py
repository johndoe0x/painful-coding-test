"""
PB0552 — 문자를 끼워 넣은 새 문자열

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 <= index <= len(text)이고 character가 한 글자라고 가정해 index 위치에 삽입한 새 문자열을 반환한다.

연습 초점
---------
삽입 지점 앞뒤 슬라이스 사이에 새 글자를 결합한다.

구현할 함수
-----------
def insert_character(text: str, index: int, character: str) -> str:

예시 및 필수 테스트
-------------------
- insert_character('cat', 1, 'r') == 'crat'
- insert_character('abc', 0, '!') == '!abc'
- insert_character('abc', 3, '!') == 'abc!'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0552 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def insert_character(text: str, index: int, character: str) -> str:
    raise NotImplementedError("TODO: PB0552")


def self_test() -> None:
    assert insert_character('cat', 1, 'r') == 'crat'
    assert insert_character('abc', 0, '!') == '!abc'
    assert insert_character('abc', 3, '!') == 'abc!'
