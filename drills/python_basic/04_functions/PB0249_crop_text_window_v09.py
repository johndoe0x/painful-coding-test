"""
PB0249 — 문자열 구간 추출

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
text에서 start 이상 stop 미만 구간을 반환한다.

연습 초점
---------
슬라이스 경계를 매개변수로 받기

구현할 함수
-----------
def crop_text_window(text: str, start: int, stop: int) -> str:

예시 및 필수 테스트
-------------------
- crop_text_window('abcdef', 1, 4) == 'bcd'
- crop_text_window('abc', 0, 0) == ''
- crop_text_window('abc', 1, 9) == 'bc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0249 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def crop_text_window(text: str, start: int, stop: int) -> str:
    raise NotImplementedError("TODO: PB0249")


def self_test() -> None:
    assert crop_text_window('abcdef', 1, 4) == 'bcd'
    assert crop_text_window('abc', 0, 0) == ''
    assert crop_text_window('abc', 1, 9) == 'bc'
