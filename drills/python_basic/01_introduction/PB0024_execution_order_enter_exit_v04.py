"""
PB0024 — 진입과 종료 기록

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 name에 대해 'enter:<name>'을 입력 순서로 기록한 뒤 'exit:<name>'을 역순으로 기록하세요.

연습 초점
---------
순방향 실행과 역방향 정리 순서

구현할 함수
-----------
def enter_exit_trace(names: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- enter_exit_trace(['a', 'b']) == ['enter:a', 'enter:b', 'exit:b', 'exit:a']
- enter_exit_trace([]) == []
- enter_exit_trace(['x']) == ['enter:x', 'exit:x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0024 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def enter_exit_trace(names: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0024")


def self_test() -> None:
    assert enter_exit_trace(['a', 'b']) == ['enter:a', 'enter:b', 'exit:b', 'exit:a']
    assert enter_exit_trace([]) == []
    assert enter_exit_trace(['x']) == ['enter:x', 'exit:x']
