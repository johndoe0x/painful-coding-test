"""
PB0230 — 불리언 단어 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
True이면 'yes', False이면 'no'를 반환한다.

연습 초점
---------
서로 다른 반환값을 갖는 함수 호출 연습

구현할 함수
-----------
def boolean_to_word(flag: bool) -> str:

예시 및 필수 테스트
-------------------
- boolean_to_word(True) == 'yes'
- boolean_to_word(False) == 'no'
- boolean_to_word(not False) == 'yes'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0230 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def boolean_to_word(flag: bool) -> str:
    raise NotImplementedError("TODO: PB0230")


def self_test() -> None:
    assert boolean_to_word(True) == 'yes'
    assert boolean_to_word(False) == 'no'
    assert boolean_to_word(not False) == 'yes'
