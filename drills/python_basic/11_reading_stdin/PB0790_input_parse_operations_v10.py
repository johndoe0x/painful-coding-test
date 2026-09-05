"""
PB0790 — 연산명과 피연산자 목록

Chapter: Reading Stdin
Topic: Read Input Practice
Seed: 79 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄의 operation과 정수 operand를 tuple로 변환한다.

연습 초점
---------
여러 명령 줄의 반복 파싱

구현할 함수
-----------
def input_parse_operations(lines: list[str]) -> list[tuple[str, int]]:

예시 및 필수 테스트
-------------------
- input_parse_operations(['add 3', 'sub 1']) == [('add', 3), ('sub', 1)]
- input_parse_operations([]) == []
- input_parse_operations(['move -2']) == [('move', -2)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0790 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_operations(lines: list[str]) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: PB0790")


def self_test() -> None:
    assert input_parse_operations(['add 3', 'sub 1']) == [('add', 3), ('sub', 1)]
    assert input_parse_operations([]) == []
    assert input_parse_operations(['move -2']) == [('move', -2)]
