"""
PB0038 — 표의 한 행

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
cells를 ' | '로 연결하고 양끝에도 '| '와 ' |'를 붙이세요.

연습 초점
---------
구분자가 있는 표 형식

구현할 함수
-----------
def format_table_row(cells: list[str]) -> str:

예시 및 필수 테스트
-------------------
- format_table_row(['A', 'B']) == '| A | B |'
- format_table_row([]) == '|  |'
- format_table_row(['']) == '|  |'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0038 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_table_row(cells: list[str]) -> str:
    raise NotImplementedError("TODO: PB0038")


def self_test() -> None:
    assert format_table_row(['A', 'B']) == '| A | B |'
    assert format_table_row([]) == '|  |'
    assert format_table_row(['']) == '|  |'
