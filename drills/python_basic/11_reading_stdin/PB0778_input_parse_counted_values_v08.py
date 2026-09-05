"""
PB0778 — 개수가 앞에 있는 입력

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
첫 정수 n 뒤에 정확히 n개의 정수가 온다고 가정하고 뒤의 n개 정수만 반환한다.

연습 초점
---------
첫 token과 나머지 token 분리

구현할 함수
-----------
def input_parse_counted_values(line: str) -> list[int]:

예시 및 필수 테스트
-------------------
- input_parse_counted_values('3 10 20 30') == [10, 20, 30]
- input_parse_counted_values('0') == []
- input_parse_counted_values('1 -5') == [-5]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0778 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_counted_values(line: str) -> list[int]:
    raise NotImplementedError("TODO: PB0778")


def self_test() -> None:
    assert input_parse_counted_values('3 10 20 30') == [10, 20, 30]
    assert input_parse_counted_values('0') == []
    assert input_parse_counted_values('1 -5') == [-5]
