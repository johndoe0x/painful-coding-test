"""
PB0493 — 글자와 위치 짝짓기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: for

문제
----
각 문자를 0부터 시작하는 인덱스와 묶어 순서대로 반환한다.

연습 초점
---------
enumerate 또는 인덱스 누적으로 문자열 순회 위치를 기록한다.

구현할 함수
-----------
def indexed_characters(text: str) -> list[tuple[int, str]]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- indexed_characters('cat') == [(0, 'c'), (1, 'a'), (2, 't')]
- indexed_characters('Z') == [(0, 'Z')]
- indexed_characters('') == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0493 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def indexed_characters(text: str) -> list[tuple[int, str]]:
    raise NotImplementedError("TODO: PB0493")


def self_test() -> None:
    assert indexed_characters('cat') == [(0, 'c'), (1, 'a'), (2, 't')]
    assert indexed_characters('Z') == [(0, 'Z')]
    assert indexed_characters('') == []
