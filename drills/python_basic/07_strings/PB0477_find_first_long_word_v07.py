"""
PB0477 — 처음 나오는 긴 단어

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
길이가 minimum 이상인 첫 문자열을 반환하고 없으면 None을 반환한다.

연습 초점
---------
순서대로 길이를 검사하며 첫 일치에서 반환한다.

구현할 함수
-----------
def first_word_at_least(words: list[str], minimum: int) -> str | None:

예시 및 필수 테스트
-------------------
- first_word_at_least(['a', 'tree', 'forest'], 4) == 'tree'
- first_word_at_least(['hi', 'ok'], 3) is None
- first_word_at_least([''], 0) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0477 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_word_at_least(words: list[str], minimum: int) -> str | None:
    raise NotImplementedError("TODO: PB0477")


def self_test() -> None:
    assert first_word_at_least(['a', 'tree', 'forest'], 4) == 'tree'
    assert first_word_at_least(['hi', 'ok'], 3) is None
    assert first_word_at_least([''], 0) == ''
