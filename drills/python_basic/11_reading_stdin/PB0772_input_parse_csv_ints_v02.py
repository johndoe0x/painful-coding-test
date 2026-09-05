"""
PB0772 — CSV 정수 목록

Chapter: Reading Stdin
Topic: Parse Input
Seed: 78 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
쉼표로 나눈 조각을 strip해 int로 바꾼다. strip한 전체 line이 비면 빈 리스트를 반환한다.

연습 초점
---------
빈 입력 처리와 구분자 기반 파싱

구현할 함수
-----------
def input_parse_csv_ints(line: str) -> list[int]:

예시 및 필수 테스트
-------------------
- input_parse_csv_ints('1, 2,-3') == [1, 2, -3]
- input_parse_csv_ints('   ') == []
- input_parse_csv_ints('0') == [0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0772 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_csv_ints(line: str) -> list[int]:
    raise NotImplementedError("TODO: PB0772")


def self_test() -> None:
    assert input_parse_csv_ints('1, 2,-3') == [1, 2, -3]
    assert input_parse_csv_ints('   ') == []
    assert input_parse_csv_ints('0') == [0]
