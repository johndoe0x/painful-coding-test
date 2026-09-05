"""
PB0754 — 줄바꿈 문자만 제거

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열 끝의 연속된 CR과 LF만 제거하고 다른 공백은 유지한다.

연습 초점
---------
rstrip에 제거할 문자 집합 지정

구현할 함수
-----------
def line_strip_line_ending(line: str) -> str:

예시 및 필수 테스트
-------------------
- line_strip_line_ending('hello' + chr(10)) == 'hello'
- line_strip_line_ending('x ' + chr(13) + chr(10)) == 'x '
- line_strip_line_ending('plain') == 'plain'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0754 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_strip_line_ending(line: str) -> str:
    raise NotImplementedError("TODO: PB0754")


def self_test() -> None:
    assert line_strip_line_ending('hello' + chr(10)) == 'hello'
    assert line_strip_line_ending('x ' + chr(13) + chr(10)) == 'x '
    assert line_strip_line_ending('plain') == 'plain'
