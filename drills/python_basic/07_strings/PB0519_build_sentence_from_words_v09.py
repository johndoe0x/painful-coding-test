"""
PB0519 — 단어로 문장 만들기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
words를 공백 하나로 연결하고, 단어가 있으면 끝에 마침표 하나를 붙이며 빈 리스트는 ''를 반환한다.

연습 초점
---------
단어 사이 결합과 문장 끝 구두점을 별도로 처리한다.

구현할 함수
-----------
def sentence_from_words(words: list[str]) -> str:

예시 및 필수 테스트
-------------------
- sentence_from_words(['Python', 'is', 'fun']) == 'Python is fun.'
- sentence_from_words(['Hello']) == 'Hello.'
- sentence_from_words([]) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0519 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sentence_from_words(words: list[str]) -> str:
    raise NotImplementedError("TODO: PB0519")


def self_test() -> None:
    assert sentence_from_words(['Python', 'is', 'fun']) == 'Python is fun.'
    assert sentence_from_words(['Hello']) == 'Hello.'
    assert sentence_from_words([]) == ''
