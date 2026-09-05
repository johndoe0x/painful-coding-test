"""
PB0323 — 짧은 문자열만 대문자

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: if

문제
----
text 길이가 5 이하일 때만 대문자로 바꾸고 그 밖에는 원문을 반환한다.

연습 초점
---------
단일 if와 기본 원본값

구현할 함수
-----------
def uppercase_if_short(text: str) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- uppercase_if_short('code') == 'CODE'
- uppercase_if_short('python') == 'python'
- uppercase_if_short('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0323 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_if_short(text: str) -> str:
    raise NotImplementedError("TODO: PB0323")


def self_test() -> None:
    assert uppercase_if_short('code') == 'CODE'
    assert uppercase_if_short('python') == 'python'
    assert uppercase_if_short('') == ''
