"""
PB0762 — 실수 입력 변환

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
text를 float로 변환한다.

연습 초점
---------
float 생성자와 부호·소수점

구현할 함수
-----------
def input_parse_float(text: str) -> float:

예시 및 필수 테스트
-------------------
- input_parse_float('3.5') == 3.5
- input_parse_float(' 0 ') == 0.0
- input_parse_float('-2') == -2.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0762 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_float(text: str) -> float:
    raise NotImplementedError("TODO: PB0762")


def self_test() -> None:
    assert input_parse_float('3.5') == 3.5
    assert input_parse_float(' 0 ') == 0.0
    assert input_parse_float('-2') == -2.0
