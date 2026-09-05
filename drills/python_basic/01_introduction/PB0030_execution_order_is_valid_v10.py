"""
PB0030 — 단계 순서 검증

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
stages가 ['start', 'process', 'end']의 순서를 지키는 부분수열이면 True를 반환하세요. 중복·역순·알 수 없는 단계는 False입니다.

연습 초점
---------
실행 단계의 상대적 순서 검증

구현할 함수
-----------
def is_valid_stage_order(stages: list[str]) -> bool:

예시 및 필수 테스트
-------------------
- is_valid_stage_order(['start', 'end']) is True
- is_valid_stage_order([]) is True
- is_valid_stage_order(['process', 'start']) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0030 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_valid_stage_order(stages: list[str]) -> bool:
    raise NotImplementedError("TODO: PB0030")


def self_test() -> None:
    assert is_valid_stage_order(['start', 'end']) is True
    assert is_valid_stage_order([]) is True
    assert is_valid_stage_order(['process', 'start']) is False
