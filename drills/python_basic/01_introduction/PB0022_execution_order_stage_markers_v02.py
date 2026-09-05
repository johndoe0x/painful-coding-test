"""
PB0022 — 단계 번호 붙이기

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 단계에 1부터 시작하는 번호를 붙여 '1:단계' 형식으로 반환하세요.

연습 초점
---------
입력 순서 보존과 단계 번호

구현할 함수
-----------
def mark_stages(stages: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- mark_stages(['load', 'run']) == ['1:load', '2:run']
- mark_stages([]) == []
- mark_stages(['done']) == ['1:done']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0022 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def mark_stages(stages: list[str]) -> list[str]:
    raise NotImplementedError("TODO: PB0022")


def self_test() -> None:
    assert mark_stages(['load', 'run']) == ['1:load', '2:run']
    assert mark_stages([]) == []
    assert mark_stages(['done']) == ['1:done']
