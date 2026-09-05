"""
PB0771 — 공백 정수 목록

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백으로 구분된 모든 token을 int로 변환한다.

연습 초점
---------
split 결과를 list comprehension으로 변환

구현할 함수
-----------
def parse_int_list(line: str) -> list[int]:

예시 및 필수 테스트
-------------------
- parse_int_list('1 2 3') == [1, 2, 3]
- parse_int_list('') == []
- parse_int_list('-1 0 1') == [-1, 0, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0771 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def parse_int_list(line: str) -> list[int]:
    raise NotImplementedError("TODO: PB0771")


def self_test() -> None:
    assert parse_int_list('1 2 3') == [1, 2, 3]
    assert parse_int_list('') == []
    assert parse_int_list('-1 0 1') == [-1, 0, 1]
