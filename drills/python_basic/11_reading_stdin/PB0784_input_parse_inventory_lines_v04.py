"""
PB0784 — 여러 재고 줄 합산

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 04 / 10
Time cap: 150 seconds
Source checks:

문제
----
각 'item quantity' 줄을 파싱해 item별 quantity를 합산한다.

연습 초점
---------
여러 줄 파싱과 딕셔너리 누적

구현할 함수
-----------
def input_parse_inventory_lines(lines: list[str]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- input_parse_inventory_lines(['pen 2', 'book 1', 'pen 3']) == {'pen': 5, 'book': 1}
- input_parse_inventory_lines([]) == {}
- input_parse_inventory_lines(['x -1']) == {'x': -1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0784 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_inventory_lines(lines: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0784")


def self_test() -> None:
    assert input_parse_inventory_lines(['pen 2', 'book 1', 'pen 3']) == {'pen': 5, 'book': 1}
    assert input_parse_inventory_lines([]) == {}
    assert input_parse_inventory_lines(['x -1']) == {'x': -1}
