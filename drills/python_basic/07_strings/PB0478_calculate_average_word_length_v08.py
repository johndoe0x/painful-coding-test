"""
PB0478 — 평균 단어 길이

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열 길이의 평균을 반환하고 words가 비어 있으면 0.0을 반환한다.

연습 초점
---------
전체 문자 수와 원소 수를 각각 구해 평균을 계산한다.

구현할 함수
-----------
def average_text_length(words: list[str]) -> float:

예시 및 필수 테스트
-------------------
- average_text_length(['a', 'abc']) == 2.0
- average_text_length(['', 'ab']) == 1.0
- average_text_length([]) == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0478 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def average_text_length(words: list[str]) -> float:
    raise NotImplementedError("TODO: PB0478")


def self_test() -> None:
    assert average_text_length(['a', 'abc']) == 2.0
    assert average_text_length(['', 'ab']) == 1.0
    assert average_text_length([]) == 0.0
