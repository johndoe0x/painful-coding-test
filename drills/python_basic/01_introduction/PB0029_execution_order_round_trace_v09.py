"""
PB0029 — 라운드별 앞뒤 표시

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 라운드 1..rounds에 대해 'before:n', 'after:n'을 바로 이어 붙여 반환하세요.

연습 초점
---------
반복 본문 안의 세부 실행 순서

구현할 함수
-----------
def round_trace(rounds: int) -> list[str]:

예시 및 필수 테스트
-------------------
- round_trace(2) == ['before:1', 'after:1', 'before:2', 'after:2']
- round_trace(0) == []
- round_trace(1) == ['before:1', 'after:1']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0029 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def round_trace(rounds: int) -> list[str]:
    raise NotImplementedError("TODO: PB0029")


def self_test() -> None:
    assert round_trace(2) == ['before:1', 'after:1', 'before:2', 'after:2']
    assert round_trace(0) == []
    assert round_trace(1) == ['before:1', 'after:1']
