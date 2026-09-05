"""
PB0533 — 사용자가 정한 간격으로 자르기

Chapter: Strings
Topic: String Slicing Part 2
Seed: 54 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: slice

문제
----
step이 양수라고 가정하고 start부터 끝까지 step 간격의 글자를 반환한다.

연습 초점
---------
슬라이스의 시작점과 보폭을 매개변수로 적용한다.

구현할 함수
-----------
def stepped_text(text: str, start: int, step: int) -> str:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- stepped_text('abcdefgh', 1, 3) == 'beh'
- stepped_text('abcdef', 0, 2) == 'ace'
- stepped_text('abc', 5, 2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0533 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def stepped_text(text: str, start: int, step: int) -> str:
    raise NotImplementedError("TODO: PB0533")


def self_test() -> None:
    assert stepped_text('abcdefgh', 1, 3) == 'beh'
    assert stepped_text('abcdef', 0, 2) == 'ace'
    assert stepped_text('abc', 5, 2) == ''
