"""
PB0553 — 한 글자를 제외한 새 문자열

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정해 해당 위치의 글자만 제외한 새 문자열을 반환한다.

연습 초점
---------
삭제 대상 앞과 뒤를 슬라이스해 새 값으로 결합한다.

구현할 함수
-----------
def remove_character_at(text: str, index: int) -> str:

예시 및 필수 테스트
-------------------
- remove_character_at('python', 1) == 'pthon'
- remove_character_at('abc', 0) == 'bc'
- remove_character_at('abc', 2) == 'ab'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0553 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def remove_character_at(text: str, index: int) -> str:
    raise NotImplementedError("TODO: PB0553")


def self_test() -> None:
    assert remove_character_at('python', 1) == 'pthon'
    assert remove_character_at('abc', 0) == 'bc'
    assert remove_character_at('abc', 2) == 'ab'
