"""
PB0511 — 구분자로 단어 연결하기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
words를 separator로 연결하되 처음과 끝에는 separator를 붙이지 않는다.

연습 초점
---------
문자열 누적 시 구분자를 넣는 위치를 구분한다.

구현할 함수
-----------
def join_words(words: list[str], separator: str) -> str:

예시 및 필수 테스트
-------------------
- join_words(['a', 'b'], '-') == 'a-b'
- join_words(['solo'], ',') == 'solo'
- join_words([], '/') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0511 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def join_words(words: list[str], separator: str) -> str:
    raise NotImplementedError("TODO: PB0511")


def self_test() -> None:
    assert join_words(['a', 'b'], '-') == 'a-b'
    assert join_words(['solo'], ',') == 'solo'
    assert join_words([], '/') == ''
