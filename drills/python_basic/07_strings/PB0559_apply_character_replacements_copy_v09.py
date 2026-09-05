"""
PB0559 — 여러 글자 교체 적용하기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 인덱스가 유효하고 각 대체값이 한 글자라고 가정해 모든 교체를 순서대로 반영한 새 문자열을 반환한다.

연습 초점
---------
하나의 변경 가능한 복사본에 여러 갱신을 적용한 뒤 불변 문자열로 변환한다.

구현할 함수
-----------
def apply_character_replacements(text: str, replacements: list[tuple[int, str]]) -> str:

예시 및 필수 테스트
-------------------
- apply_character_replacements('abcd', [(0, 'A'), (3, 'D')]) == 'AbcD'
- apply_character_replacements('cat', [(1, 'u')]) == 'cut'
- apply_character_replacements('abc', []) == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0559 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def apply_character_replacements(text: str, replacements: list[tuple[int, str]]) -> str:
    raise NotImplementedError("TODO: PB0559")


def self_test() -> None:
    assert apply_character_replacements('abcd', [(0, 'A'), (3, 'D')]) == 'AbcD'
    assert apply_character_replacements('cat', [(1, 'u')]) == 'cut'
    assert apply_character_replacements('abc', []) == 'abc'
