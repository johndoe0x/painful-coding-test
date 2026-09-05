"""
PB0725 — 문자 빈도표

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백을 포함해 text의 각 문자 등장 횟수를 반환한다.

연습 초점
---------
문자열 순회와 딕셔너리 카운팅

구현할 함수
-----------
def dict_character_frequency(text: str) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_character_frequency('aba') == {'a': 2, 'b': 1}
- dict_character_frequency('') == {}
- dict_character_frequency('a a') == {'a': 2, ' ': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0725 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_character_frequency(text: str) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0725")


def self_test() -> None:
    assert dict_character_frequency('aba') == {'a': 2, 'b': 1}
    assert dict_character_frequency('') == {}
    assert dict_character_frequency('a a') == {'a': 2, ' ': 1}
