"""
PB0575 — 문자열을 글자 리스트로

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
text의 각 글자를 순서대로 담은 새 리스트를 반환한다.

연습 초점
---------
list 생성자가 iterable을 원소 단위로 펼치는 동작을 확인한다.

구현할 함수
-----------
def text_as_character_list(text: str) -> list[str]:

예시 및 필수 테스트
-------------------
- text_as_character_list('cat') == ['c', 'a', 't']
- text_as_character_list(' ') == [' ']
- text_as_character_list('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0575 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def text_as_character_list(text: str) -> list[str]:
    raise NotImplementedError("TODO: PB0575")


def self_test() -> None:
    assert text_as_character_list('cat') == ['c', 'a', 't']
    assert text_as_character_list(' ') == [' ']
    assert text_as_character_list('') == []
