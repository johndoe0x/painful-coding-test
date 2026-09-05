"""
PB0554 — 구간을 새 문자열로 교체하기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 <= start <= stop <= len(text)라고 가정해 text[start:stop]을 replacement로 교체한 새 문자열을 반환한다.

연습 초점
---------
변경되지 않는 양쪽 슬라이스와 대체 문자열을 재조립한다.

구현할 함수
-----------
def replace_text_range(text: str, start: int, stop: int, replacement: str) -> str:

예시 및 필수 테스트
-------------------
- replace_text_range('abcdef', 2, 4, 'XY') == 'abXYef'
- replace_text_range('abc', 0, 3, '') == ''
- replace_text_range('abc', 1, 1, '-') == 'a-bc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0554 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_text_range(text: str, start: int, stop: int, replacement: str) -> str:
    raise NotImplementedError("TODO: PB0554")


def self_test() -> None:
    assert replace_text_range('abcdef', 2, 4, 'XY') == 'abXYef'
    assert replace_text_range('abc', 0, 3, '') == ''
    assert replace_text_range('abc', 1, 1, '-') == 'a-bc'
