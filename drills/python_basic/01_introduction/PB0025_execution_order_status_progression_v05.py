"""
PB0025 — 상태 진행 경로

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
['created', 'validated', 'completed'] 중 인덱스 final_stage까지 포함해 반환하세요. final_stage는 0~2입니다.

연습 초점
---------
정해진 단계의 순차 실행

구현할 함수
-----------
def status_progression(final_stage: int) -> list[str]:

예시 및 필수 테스트
-------------------
- status_progression(1) == ['created', 'validated']
- status_progression(0) == ['created']
- status_progression(2) == ['created', 'validated', 'completed']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0025 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def status_progression(final_stage: int) -> list[str]:
    raise NotImplementedError("TODO: PB0025")


def self_test() -> None:
    assert status_progression(1) == ['created', 'validated']
    assert status_progression(0) == ['created']
    assert status_progression(2) == ['created', 'validated', 'completed']
