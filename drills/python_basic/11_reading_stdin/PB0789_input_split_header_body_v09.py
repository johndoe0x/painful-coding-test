"""
PB0789 — 첫 줄과 나머지 줄

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄을 strip한다. 입력이 비면 (None, []), 아니면 첫 줄과 나머지 줄을 반환한다.

연습 초점
---------
빈 리스트 분기와 sequence head-tail 분리

구현할 함수
-----------
def input_split_header_body(lines: list[str]) -> tuple[str | None, list[str]]:

예시 및 필수 테스트
-------------------
- input_split_header_body([' TITLE ', ' a ', ' b ']) == ('TITLE', ['a', 'b'])
- input_split_header_body([]) == (None, [])
- input_split_header_body([' only ']) == ('only', [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0789 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_split_header_body(lines: list[str]) -> tuple[str | None, list[str]]:
    raise NotImplementedError("TODO: PB0789")


def self_test() -> None:
    assert input_split_header_body([' TITLE ', ' a ', ' b ']) == ('TITLE', ['a', 'b'])
    assert input_split_header_body([]) == (None, [])
    assert input_split_header_body([' only ']) == ('only', [])
