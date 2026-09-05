"""
PB0774 — 여러 줄 정수 행렬

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 줄의 공백 구분 정수를 하나의 행으로 변환한다. 빈 줄은 빈 행이 된다.

연습 초점
---------
중첩 list comprehension과 행 단위 파싱

구현할 함수
-----------
def input_parse_matrix(lines: list[str]) -> list[list[int]]:

예시 및 필수 테스트
-------------------
- input_parse_matrix(['1 2', '3 4']) == [[1, 2], [3, 4]]
- input_parse_matrix([]) == []
- input_parse_matrix(['']) == [[]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0774 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_matrix(lines: list[str]) -> list[list[int]]:
    raise NotImplementedError("TODO: PB0774")


def self_test() -> None:
    assert input_parse_matrix(['1 2', '3 4']) == [[1, 2], [3, 4]]
    assert input_parse_matrix([]) == []
    assert input_parse_matrix(['']) == [[]]
