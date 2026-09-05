"""
PB0503 — 대문자만 골라내기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
text에서 대문자 글자만 리스트로 반환한다.

연습 초점
---------
리스트 컴프리헨션의 필터 조건을 연습한다.

구현할 함수
-----------
def uppercase_characters(text: str) -> list[str]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- uppercase_characters('PyTHon') == ['P', 'T', 'H']
- uppercase_characters('abc') == []
- uppercase_characters('A1!B') == ['A', 'B']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0503 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_characters(text: str) -> list[str]:
    raise NotImplementedError("TODO: PB0503")


def self_test() -> None:
    assert uppercase_characters('PyTHon') == ['P', 'T', 'H']
    assert uppercase_characters('abc') == []
    assert uppercase_characters('A1!B') == ['A', 'B']
