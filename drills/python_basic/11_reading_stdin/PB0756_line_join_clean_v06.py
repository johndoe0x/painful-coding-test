"""
PB0756 — 정리한 줄 다시 합치기

Chapter: Reading Stdin
Topic: Reading Input
Seed: 76 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄을 strip하고 빈 줄은 버린 뒤 LF 한 글자로 연결한다.

연습 초점
---------
strip, 필터링, join

구현할 함수
-----------
def line_join_clean(lines: list[str]) -> str:

예시 및 필수 테스트
-------------------
- line_join_clean([' a ', '', ' b']) == 'a' + chr(10) + 'b'
- line_join_clean([]) == ''
- line_join_clean([' x ']) == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0756 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def line_join_clean(lines: list[str]) -> str:
    raise NotImplementedError("TODO: PB0756")


def self_test() -> None:
    assert line_join_clean([' a ', '', ' b']) == 'a' + chr(10) + 'b'
    assert line_join_clean([]) == ''
    assert line_join_clean([' x ']) == 'x'
