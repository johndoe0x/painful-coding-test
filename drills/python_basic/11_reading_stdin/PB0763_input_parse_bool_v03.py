"""
PB0763 — bool 문자열 해석

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
strip 후 대소문자를 무시해 true면 True, false면 False, 그 밖은 None을 반환한다.

연습 초점
---------
문자열 정규화와 다중 조건 반환

구현할 함수
-----------
def input_parse_bool(text: str) -> bool | None:

예시 및 필수 테스트
-------------------
- input_parse_bool(' TRUE ') is True
- input_parse_bool('false') is False
- input_parse_bool('yes') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0763 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_bool(text: str) -> bool | None:
    raise NotImplementedError("TODO: PB0763")


def self_test() -> None:
    assert input_parse_bool(' TRUE ') is True
    assert input_parse_bool('false') is False
    assert input_parse_bool('yes') is None
