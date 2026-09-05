"""
PB0460 — 단어별 문자 라벨

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
바깥 for로 단어를, 안쪽 for로 문자를 순회해 각 문자를 '<단어>:<문자>' 형식으로 만든 행들을 반환한다.

연습 초점
---------
길이가 다른 내부 컬렉션 중첩 순회

구현할 함수
-----------
def word_character_grid(words: list[str]) -> list[list[str]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- word_character_grid(['ab', 'x']) == [['ab:a', 'ab:b'], ['x:x']]
- word_character_grid([]) == []
- word_character_grid(['']) == [[]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0460 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def word_character_grid(words: list[str]) -> list[list[str]]:
    raise NotImplementedError("TODO: PB0460")


def self_test() -> None:
    assert word_character_grid(['ab', 'x']) == [['ab:a', 'ab:b'], ['x:x']]
    assert word_character_grid([]) == []
    assert word_character_grid(['']) == [[]]
