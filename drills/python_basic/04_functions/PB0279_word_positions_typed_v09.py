"""
PB0279 — 단어 위치 목록 사전

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단어를 등장한 모든 인덱스 목록에 연결한다.

연습 초점
---------
dict 안의 list까지 타입으로 명시

구현할 함수
-----------
def word_positions_typed(words: list[str]) -> dict[str, list[int]]:

예시 및 필수 테스트
-------------------
- word_positions_typed(['a', 'b', 'a']) == {'a': [0, 2], 'b': [1]}
- word_positions_typed([]) == {}
- word_positions_typed(['']) == {'': [0]}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0279 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def word_positions_typed(words: list[str]) -> dict[str, list[int]]:
    raise NotImplementedError("TODO: PB0279")


def self_test() -> None:
    assert word_positions_typed(['a', 'b', 'a']) == {'a': [0, 2], 'b': [1]}
    assert word_positions_typed([]) == {}
    assert word_positions_typed(['']) == {'': [0]}
