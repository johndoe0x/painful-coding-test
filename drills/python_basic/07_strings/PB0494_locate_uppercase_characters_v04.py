"""
PB0494 — 대문자 위치 찾기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: for

문제
----
text를 순회해 대문자인 문자의 인덱스만 반환한다.

연습 초점
---------
인덱스가 있는 반복과 str.isupper 조건을 함께 사용한다.

구현할 함수
-----------
def uppercase_positions(text: str) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- uppercase_positions('PyTHon') == [0, 2, 3]
- uppercase_positions('abc') == []
- uppercase_positions('A1B!') == [0, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0494 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def uppercase_positions(text: str) -> list[int]:
    raise NotImplementedError("TODO: PB0494")


def self_test() -> None:
    assert uppercase_positions('PyTHon') == [0, 2, 3]
    assert uppercase_positions('abc') == []
    assert uppercase_positions('A1B!') == [0, 2]
