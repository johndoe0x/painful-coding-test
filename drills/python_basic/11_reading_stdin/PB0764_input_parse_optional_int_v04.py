"""
PB0764 — 선택 정수 입력

Chapter: Reading Stdin
Topic: Type Conversion with Input
Seed: 77 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
strip 결과가 비면 None, 아니면 int 변환 결과를 반환한다. 비어 있지 않은 입력은 유효한 정수라고 가정한다.

연습 초점
---------
빈 입력 분기와 int 변환

구현할 함수
-----------
def input_parse_optional_int(text: str) -> int | None:

예시 및 필수 테스트
-------------------
- input_parse_optional_int('42') == 42
- input_parse_optional_int('   ') is None
- input_parse_optional_int('-3') == -3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0764 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def input_parse_optional_int(text: str) -> int | None:
    raise NotImplementedError("TODO: PB0764")


def self_test() -> None:
    assert input_parse_optional_int('42') == 42
    assert input_parse_optional_int('   ') is None
    assert input_parse_optional_int('-3') == -3
