"""
PB0528 — 문자열 앞 절반

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
text의 앞 len(text) // 2글자를 반환해 홀수 길이에서는 가운데 글자를 제외한다.

연습 초점
---------
정수 나눗셈 결과를 슬라이스 끝으로 사용한다.

구현할 함수
-----------
def first_half(text: str) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- first_half('abcdef') == 'abc'
- first_half('abcde') == 'ab'
- first_half('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0528 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_half(text: str) -> str:
    raise NotImplementedError("TODO: PB0528")


def self_test() -> None:
    assert first_half('abcdef') == 'abc'
    assert first_half('abcde') == 'ab'
    assert first_half('') == ''
