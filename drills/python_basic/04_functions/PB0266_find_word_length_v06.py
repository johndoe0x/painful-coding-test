"""
PB0266 — 단어 길이 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
target을 처음 만나면 길이를 즉시 반환하고 없으면 -1을 반환한다.

연습 초점
---------
반복 중 조기 반환과 기본 반환

구현할 함수
-----------
def find_word_length(words: list[str], target: str) -> int:

예시 및 필수 테스트
-------------------
- find_word_length(['cat', 'python'], 'python') == 6
- find_word_length([], 'x') == -1
- find_word_length(['aa', 'aa'], 'aa') == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0266 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def find_word_length(words: list[str], target: str) -> int:
    raise NotImplementedError("TODO: PB0266")


def self_test() -> None:
    assert find_word_length(['cat', 'python'], 'python') == 6
    assert find_word_length([], 'x') == -1
    assert find_word_length(['aa', 'aa'], 'aa') == 2
