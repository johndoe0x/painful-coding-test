"""
PB0495 — 글자마다 반복하기

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for

문제
----
count는 0 이상이라고 가정한다. 각 문자를 count번 연속으로 붙인 문자열을 반환하며 count가 0이면 빈 문자열을 반환한다.

연습 초점
---------
문자열을 순회하면서 문자별 반복 결과를 누적한다.

구현할 함수
-----------
def repeat_characters(text: str, count: int) -> str:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- repeat_characters('abc', 2) == 'aabbcc'
- repeat_characters('Hi', 1) == 'Hi'
- repeat_characters('abc', 0) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0495 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_characters(text: str, count: int) -> str:
    raise NotImplementedError("TODO: PB0495")


def self_test() -> None:
    assert repeat_characters('abc', 2) == 'aabbcc'
    assert repeat_characters('Hi', 1) == 'Hi'
    assert repeat_characters('abc', 0) == ''
