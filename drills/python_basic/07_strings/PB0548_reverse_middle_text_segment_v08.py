"""
PB0548 — 지정 구간만 뒤집기

Chapter: Strings
Topic: Reversing a String
Seed: 55 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: reverse_slice

문제
----
0 <= start <= stop <= len(text)라고 가정해 text[start:stop]만 뒤집은 문자열을 반환한다.

연습 초점
---------
앞·선택 구간·뒤의 세 슬라이스를 올바른 순서로 재조립한다.

구현할 함수
-----------
def reverse_segment(text: str, start: int, stop: int) -> str:

필수 구현 방식
--------------
- step이 -1인 역방향 슬라이스를 사용한다.

예시 및 필수 테스트
-------------------
- reverse_segment('abcdef', 1, 5) == 'aedcbf'
- reverse_segment('abc', 0, 3) == 'cba'
- reverse_segment('abc', 1, 1) == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0548 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_segment(text: str, start: int, stop: int) -> str:
    raise NotImplementedError("TODO: PB0548")


def self_test() -> None:
    assert reverse_segment('abcdef', 1, 5) == 'aedcbf'
    assert reverse_segment('abc', 0, 3) == 'cba'
    assert reverse_segment('abc', 1, 1) == 'abc'
