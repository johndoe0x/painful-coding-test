"""
PB0508 — 문자와 숫자 외 글자 가리기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
영문자·한글·숫자 등 str.isalnum이 참인 글자는 유지하고 나머지는 mask로 바꾼다.

연습 초점
---------
문자 판별 메서드와 조건부 generator 표현식을 결합한다.

구현할 함수
-----------
def mask_non_alphanumeric(text: str, mask: str = '_') -> str:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- mask_non_alphanumeric('a-b c') == 'a_b_c'
- mask_non_alphanumeric('A1!', '*') == 'A1*'
- mask_non_alphanumeric('한글2') == '한글2'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0508 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mask_non_alphanumeric(text: str, mask: str = '_') -> str:
    raise NotImplementedError("TODO: PB0508")


def self_test() -> None:
    assert mask_non_alphanumeric('a-b c') == 'a_b_c'
    assert mask_non_alphanumeric('A1!', '*') == 'A1*'
    assert mask_non_alphanumeric('한글2') == '한글2'
