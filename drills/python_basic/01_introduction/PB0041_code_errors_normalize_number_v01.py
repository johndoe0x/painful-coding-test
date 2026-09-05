"""
PB0041 — 첫 글자만 변환하는 오류 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 strip한 문자열의 첫 글자만 int로 바꾸는 버그가 있습니다. 앞뒤 공백을 제거한 전체 문자열을 정수로 변환하세요.

연습 초점
---------
부분 인덱싱을 제거하고 전체 입력을 올바른 시점에 변환

구현할 함수
-----------
def normalize_number(text: str) -> int:

예시 및 필수 테스트
-------------------
- normalize_number(' 42 ') == 42
- normalize_number('0') == 0
- normalize_number('-7') == -7

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0041 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalize_number(text: str) -> int:
    return int(text.strip()[0])


def self_test() -> None:
    assert normalize_number(' 42 ') == 42
    assert normalize_number('0') == 0
    assert normalize_number('-7') == -7
