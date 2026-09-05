"""
PB0536 — 범위와 간격을 함께 지정하기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
Python의 text[start:stop:step]과 같은 결과를 반환하며 step은 0이 아니다.

연습 초점
---------
세 요소를 모두 가진 슬라이스 문법을 연습한다.

구현할 함수
-----------
def bounded_stride(text: str, start: int, stop: int, step: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- bounded_stride('abcdefgh', 1, 7, 2) == 'bdf'
- bounded_stride('abcdefgh', 6, 0, -2) == 'gec'
- bounded_stride('abc', 0, 0, 1) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0536 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def bounded_stride(text: str, start: int, stop: int, step: int) -> str:
    raise NotImplementedError("TODO: PB0536")


def self_test() -> None:
    assert bounded_stride('abcdefgh', 1, 7, 2) == 'bdf'
    assert bounded_stride('abcdefgh', 6, 0, -2) == 'gec'
    assert bounded_stride('abc', 0, 0, 1) == ''
