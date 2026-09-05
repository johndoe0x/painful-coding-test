"""
PB0047 — 문자열 마지막 인덱스 오류 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 text[len(text)]에 접근해 비어 있지 않은 문자열에서도 IndexError가 납니다. 빈 문자열이면 '', 아니면 유효한 마지막 글자를 반환하세요.

연습 초점
---------
길이는 마지막 인덱스보다 1 크다는 규칙

구현할 함수
-----------
def corrected_last_character(text: str) -> str:

예시 및 필수 테스트
-------------------
- corrected_last_character('code') == 'e'
- corrected_last_character('') == ''
- corrected_last_character('x') == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0047 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def corrected_last_character(text: str) -> str:
    if not text:
        return ''
    return text[len(text)]


def self_test() -> None:
    assert corrected_last_character('code') == 'e'
    assert corrected_last_character('') == ''
    assert corrected_last_character('x') == 'x'
