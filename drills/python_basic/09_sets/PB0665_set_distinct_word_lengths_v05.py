"""
PB0665 — 단어 길이 종류

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단어의 길이를 모아 서로 다른 길이의 set을 반환한다.

연습 초점
---------
set comprehension

구현할 함수
-----------
def set_distinct_word_lengths(words: list[str]) -> set[int]:

예시 및 필수 테스트
-------------------
- set_distinct_word_lengths(['a', 'to', 'tea']) == {1, 2, 3}
- set_distinct_word_lengths([]) == set()
- set_distinct_word_lengths(['ab', 'cd']) == {2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0665 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_distinct_word_lengths(words: list[str]) -> set[int]:
    raise NotImplementedError("TODO: PB0665")


def self_test() -> None:
    assert set_distinct_word_lengths(['a', 'to', 'tea']) == {1, 2, 3}
    assert set_distinct_word_lengths([]) == set()
    assert set_distinct_word_lengths(['ab', 'cd']) == {2}
