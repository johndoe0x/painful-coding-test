"""
PB0021 — 값 처리 순서

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
'start', 각 값의 'value=<값>', 'end'를 실제 실행 순서대로 반환하세요.

연습 초점
---------
위에서 아래로 실행되는 순서 추적

구현할 함수
-----------
def execution_trace(values: list[int]) -> list[str]:

예시 및 필수 테스트
-------------------
- execution_trace([2, 4]) == ['start', 'value=2', 'value=4', 'end']
- execution_trace([]) == ['start', 'end']
- execution_trace([0]) == ['start', 'value=0', 'end']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0021 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def execution_trace(values: list[int]) -> list[str]:
    raise NotImplementedError("TODO: PB0021")


def self_test() -> None:
    assert execution_trace([2, 4]) == ['start', 'value=2', 'value=4', 'end']
    assert execution_trace([]) == ['start', 'end']
    assert execution_trace([0]) == ['start', 'value=0', 'end']
