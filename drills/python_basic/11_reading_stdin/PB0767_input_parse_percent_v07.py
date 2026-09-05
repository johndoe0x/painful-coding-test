"""
PB0767 — 퍼센트 문자열을 비율로

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
strip 후 마지막의 % 한 글자를 제거하고 숫자를 100으로 나눈다.

연습 초점
---------
문자열 suffix 제거와 float 계산

구현할 함수
-----------
def input_parse_percent(text: str) -> float:

예시 및 필수 테스트
-------------------
- input_parse_percent('25%') == 0.25
- input_parse_percent(' 100% ') == 1.0
- input_parse_percent('0%') == 0.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0767 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_percent(text: str) -> float:
    raise NotImplementedError("TODO: PB0767")


def self_test() -> None:
    assert input_parse_percent('25%') == 0.25
    assert input_parse_percent(' 100% ') == 1.0
    assert input_parse_percent('0%') == 0.0
