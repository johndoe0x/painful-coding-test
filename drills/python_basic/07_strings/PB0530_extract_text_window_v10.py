"""
PB0530 — 고정 길이 창 자르기

Chapter: Strings
Topic: String Slicing Part 1
Seed: 53 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
start가 0 이상이고 size가 0 이상이라고 가정해 start부터 최대 size글자를 반환한다.

연습 초점
---------
시작 위치와 길이를 끝 위치로 변환해 슬라이스한다.

구현할 함수
-----------
def text_window(text: str, start: int, size: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- text_window('abcdefgh', 2, 3) == 'cde'
- text_window('abc', 1, 5) == 'bc'
- text_window('abc', 3, 2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0530 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def text_window(text: str, start: int, size: int) -> str:
    raise NotImplementedError("TODO: PB0530")


def self_test() -> None:
    assert text_window('abcdefgh', 2, 3) == 'cde'
    assert text_window('abc', 1, 5) == 'bc'
    assert text_window('abc', 3, 2) == ''
