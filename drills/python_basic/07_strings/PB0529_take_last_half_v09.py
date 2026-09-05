"""
PB0529 — 문자열 뒤 절반

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
text의 뒤 len(text) // 2글자를 반환해 홀수 길이에서는 가운데 글자를 제외한다.

연습 초점
---------
길이에서 절반을 뺀 위치를 슬라이스 시작으로 사용한다.

구현할 함수
-----------
def last_half(text: str) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- last_half('abcdef') == 'def'
- last_half('abcde') == 'de'
- last_half('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0529 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def last_half(text: str) -> str:
    raise NotImplementedError("TODO: PB0529")


def self_test() -> None:
    assert last_half('abcdef') == 'def'
    assert last_half('abcde') == 'de'
    assert last_half('') == ''
