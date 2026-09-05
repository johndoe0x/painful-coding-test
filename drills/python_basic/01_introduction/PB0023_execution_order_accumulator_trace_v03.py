"""
PB0023 — 누적값 변화 기록

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
start를 첫 원소로 기록하고 각 change를 차례로 더한 직후의 값을 이어서 반환하세요.

연습 초점
---------
문장 실행 순서와 상태 변화

구현할 함수
-----------
def trace_accumulator(start: int, changes: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- trace_accumulator(10, [3, -2]) == [10, 13, 11]
- trace_accumulator(5, []) == [5]
- trace_accumulator(0, [0]) == [0, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0023 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def trace_accumulator(start: int, changes: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0023")


def self_test() -> None:
    assert trace_accumulator(10, [3, -2]) == [10, 13, 11]
    assert trace_accumulator(5, []) == [5]
    assert trace_accumulator(0, [0]) == [0, 0]
