"""
PB0027 — 문자열 변환 단계

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
원문, strip 결과, strip 결과의 소문자화를 이 순서로 리스트에 담으세요.

연습 초점
---------
중간 결과가 다음 단계 입력이 되는 흐름

구현할 함수
-----------
def text_transform_trace(text: str) -> list[str]:

예시 및 필수 테스트
-------------------
- text_transform_trace(' Hi ') == [' Hi ', 'Hi', 'hi']
- text_transform_trace('') == ['', '', '']
- text_transform_trace('ABC') == ['ABC', 'ABC', 'abc']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0027 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def text_transform_trace(text: str) -> list[str]:
    raise NotImplementedError("TODO: PB0027")


def self_test() -> None:
    assert text_transform_trace(' Hi ') == [' Hi ', 'Hi', 'hi']
    assert text_transform_trace('') == ['', '', '']
    assert text_transform_trace('ABC') == ['ABC', 'ABC', 'abc']
