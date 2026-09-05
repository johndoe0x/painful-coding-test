"""
PB0722 — 단어별 길이

Chapter: Dictionaries
Topic: Dict Practice
Seed: 73 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단어를 key, 길이를 value로 저장한다. 중복 단어는 하나의 key로 남는다.

연습 초점
---------
문자열 리스트를 파생 value 딕셔너리로 변환

구현할 함수
-----------
def dict_word_lengths(words: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- dict_word_lengths(['cat', 'python']) == {'cat': 3, 'python': 6}
- dict_word_lengths([]) == {}
- dict_word_lengths(['a', 'a']) == {'a': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0722 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_word_lengths(words: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0722")


def self_test() -> None:
    assert dict_word_lengths(['cat', 'python']) == {'cat': 3, 'python': 6}
    assert dict_word_lengths([]) == {}
    assert dict_word_lengths(['a', 'a']) == {'a': 1}
