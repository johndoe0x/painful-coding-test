"""
PB0520 — 각 단어에 접미사 붙이기

Chapter: Strings
Topic: String Concatenation
Seed: 52 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단어 뒤에 suffix를 붙인 뒤 결과들을 공백 하나로 연결한다.

연습 초점
---------
원소별 문자열 결합과 전체 결과 결합의 두 단계를 구분한다.

구현할 함수
-----------
def words_with_suffix(words: list[str], suffix: str) -> str:

예시 및 필수 테스트
-------------------
- words_with_suffix(['read', 'walk'], 'ing') == 'reading walking'
- words_with_suffix(['cat'], 's') == 'cats'
- words_with_suffix([], '!') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0520 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def words_with_suffix(words: list[str], suffix: str) -> str:
    raise NotImplementedError("TODO: PB0520")


def self_test() -> None:
    assert words_with_suffix(['read', 'walk'], 'ing') == 'reading walking'
    assert words_with_suffix(['cat'], 's') == 'cats'
    assert words_with_suffix([], '!') == ''
