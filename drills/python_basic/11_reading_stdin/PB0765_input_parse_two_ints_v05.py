"""
PB0765 — 두 정수 token

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
공백으로 구분된 정확히 두 token을 int로 변환해 tuple로 반환한다.

연습 초점
---------
다중 할당과 두 번의 타입 변환

구현할 함수
-----------
def input_parse_two_ints(line: str) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- input_parse_two_ints('10 20') == (10, 20)
- input_parse_two_ints(' -1   0 ') == (-1, 0)
- input_parse_two_ints('3 3') == (3, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0765 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_two_ints(line: str) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0765")


def self_test() -> None:
    assert input_parse_two_ints('10 20') == (10, 20)
    assert input_parse_two_ints(' -1   0 ') == (-1, 0)
    assert input_parse_two_ints('3 3') == (3, 3)
