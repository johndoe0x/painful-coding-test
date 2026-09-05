"""
PB0662 — 서로 다른 단어 수

Chapter: Sets
Topic: Intro to Sets
Seed: 67 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
대소문자를 구분해 서로 다른 단어의 개수를 반환한다.

연습 초점
---------
list를 set으로 바꾸고 len 사용

구현할 함수
-----------
def set_unique_word_count(words: list[str]) -> int:

예시 및 필수 테스트
-------------------
- set_unique_word_count(['red', 'blue', 'red']) == 2
- set_unique_word_count([]) == 0
- set_unique_word_count(['A', 'a']) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0662 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def set_unique_word_count(words: list[str]) -> int:
    raise NotImplementedError("TODO: PB0662")


def self_test() -> None:
    assert set_unique_word_count(['red', 'blue', 'red']) == 2
    assert set_unique_word_count([]) == 0
    assert set_unique_word_count(['A', 'a']) == 2
