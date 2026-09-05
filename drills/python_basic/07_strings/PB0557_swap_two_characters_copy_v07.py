"""
PB0557 — 두 글자 위치 바꾸기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 인덱스가 유효하다고 가정해 해당 글자들의 위치를 바꾼 새 문자열을 반환한다.

연습 초점
---------
문자열을 변경 가능한 글자 리스트로 복사한 뒤 다시 문자열로 만든다.

구현할 함수
-----------
def swap_characters_at(text: str, first: int, second: int) -> str:

예시 및 필수 테스트
-------------------
- swap_characters_at('abcd', 0, 3) == 'dbca'
- swap_characters_at('abcd', 1, 2) == 'acbd'
- swap_characters_at('abc', 1, 1) == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0557 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def swap_characters_at(text: str, first: int, second: int) -> str:
    raise NotImplementedError("TODO: PB0557")


def self_test() -> None:
    assert swap_characters_at('abcd', 0, 3) == 'dbca'
    assert swap_characters_at('abcd', 1, 2) == 'acbd'
    assert swap_characters_at('abc', 1, 1) == 'abc'
