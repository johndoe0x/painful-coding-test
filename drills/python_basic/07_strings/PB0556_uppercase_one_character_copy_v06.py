"""
PB0556 — 한 위치만 대문자로 바꾸기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정해 그 위치의 글자만 upper 결과로 교체한 새 문자열을 반환한다.

연습 초점
---------
읽은 한 글자를 변환하고 원본의 나머지 조각과 결합한다.

구현할 함수
-----------
def uppercase_character_at(text: str, index: int) -> str:

예시 및 필수 테스트
-------------------
- uppercase_character_at('python', 0) == 'Python'
- uppercase_character_at('abc', 1) == 'aBc'
- uppercase_character_at('A', 0) == 'A'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0556 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_character_at(text: str, index: int) -> str:
    raise NotImplementedError("TODO: PB0556")


def self_test() -> None:
    assert uppercase_character_at('python', 0) == 'Python'
    assert uppercase_character_at('abc', 1) == 'aBc'
    assert uppercase_character_at('A', 0) == 'A'
