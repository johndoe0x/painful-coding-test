"""
PB0227 — 첫 글자 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열이 비어 있으면 빈 문자열, 아니면 첫 글자를 반환한다.

연습 초점
---------
작은 동작을 이름 있는 함수로 분리

구현할 함수
-----------
def first_character_or_empty(text: str) -> str:

예시 및 필수 테스트
-------------------
- first_character_or_empty('code') == 'c'
- first_character_or_empty('') == ''
- first_character_or_empty('한') == '한'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0227 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_character_or_empty(text: str) -> str:
    raise NotImplementedError("TODO: PB0227")


def self_test() -> None:
    assert first_character_or_empty('code') == 'c'
    assert first_character_or_empty('') == ''
    assert first_character_or_empty('한') == '한'
