"""
PB0476 — 지정 길이 단어만 고르기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
words에서 길이가 size인 문자열만 원래 순서대로 반환한다.

연습 초점
---------
각 원소에 len을 적용해 리스트 필터 조건으로 사용한다.

구현할 함수
-----------
def words_of_length(words: list[str], size: int) -> list[str]:

예시 및 필수 테스트
-------------------
- words_of_length(['a', 'to', 'sun'], 2) == ['to']
- words_of_length(['', 'x', ''], 0) == ['', '']
- words_of_length([], 3) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0476 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def words_of_length(words: list[str], size: int) -> list[str]:
    raise NotImplementedError("TODO: PB0476")


def self_test() -> None:
    assert words_of_length(['a', 'to', 'sun'], 2) == ['to']
    assert words_of_length(['', 'x', ''], 0) == ['', '']
    assert words_of_length([], 3) == []
