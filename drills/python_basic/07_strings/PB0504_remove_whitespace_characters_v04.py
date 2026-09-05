"""
PB0504 — 공백 문자 제거하기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
str.isspace가 True인 모든 문자를 제거한 새 문자열을 반환한다.

연습 초점
---------
generator 표현식의 부정 조건과 join을 결합한다.

구현할 함수
-----------
def without_whitespace(text: str) -> str:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- without_whitespace('a b c') == 'abc'
- without_whitespace(' a\\t b\\n') == 'ab'
- without_whitespace('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0504 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def without_whitespace(text: str) -> str:
    raise NotImplementedError("TODO: PB0504")


def self_test() -> None:
    assert without_whitespace('a b c') == 'abc'
    assert without_whitespace(' a\t b\n') == 'ab'
    assert without_whitespace('') == ''
