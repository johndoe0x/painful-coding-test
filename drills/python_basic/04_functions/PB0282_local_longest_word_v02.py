"""
PB0282 — 지역 후보로 가장 긴 단어 찾기

Chapter: Functions
Topic: Scope
Seed: 29 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: no_global

문제
----
함수 내부 candidate를 None에서 시작해 더 긴 단어를 만날 때만 재할당하고 반환한다. 길이가 같으면 먼저 나온 단어를 유지하며 빈 리스트는 None을 반환한다.

연습 초점
---------
지역 후보 상태와 동률 규칙

구현할 함수
-----------
def longest_word_local(words: list[str]) -> str | None:

필수 구현 방식
--------------
- global 또는 nonlocal 문으로 외부 상태를 수정하지 않는다.

예시 및 필수 테스트
-------------------
- longest_word_local(['cat', 'python', 'ruby']) == 'python'
- longest_word_local(['aa', 'bb']) == 'aa'
- longest_word_local([]) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0282 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def longest_word_local(words: list[str]) -> str | None:
    raise NotImplementedError("TODO: PB0282")


def self_test() -> None:
    assert longest_word_local(['cat', 'python', 'ruby']) == 'python'
    assert longest_word_local(['aa', 'bb']) == 'aa'
    assert longest_word_local([]) is None
