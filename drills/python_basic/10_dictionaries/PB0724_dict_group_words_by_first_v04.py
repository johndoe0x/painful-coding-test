"""
PB0724 — 첫 글자로 단어 묶기

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
비어 있지 않은 단어를 첫 글자별 리스트로 입력 순서대로 묶는다.

연습 초점
---------
동적 key와 리스트 누적

구현할 함수
-----------
def dict_group_words_by_first(words: list[str]) -> dict[str, list[str]]:

예시 및 필수 테스트
-------------------
- dict_group_words_by_first(['apple', 'ant', 'banana']) == {'a': ['apple', 'ant'], 'b': ['banana']}
- dict_group_words_by_first([]) == {}
- dict_group_words_by_first(['x']) == {'x': ['x']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0724 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_group_words_by_first(words: list[str]) -> dict[str, list[str]]:
    raise NotImplementedError("TODO: PB0724")


def self_test() -> None:
    assert dict_group_words_by_first(['apple', 'ant', 'banana']) == {'a': ['apple', 'ant'], 'b': ['banana']}
    assert dict_group_words_by_first([]) == {}
    assert dict_group_words_by_first(['x']) == {'x': ['x']}
