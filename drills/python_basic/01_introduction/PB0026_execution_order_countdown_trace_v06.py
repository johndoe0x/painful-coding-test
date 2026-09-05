"""
PB0026 — 카운트다운 실행 흔적

Chapter: Introduction
Topic: Execution Order
Seed: 03 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
start부터 1까지 'tick:<n>'을 기록하고 마지막에 'go'를 붙이세요. start가 0이면 ['go']입니다.

연습 초점
---------
반복 종료 전후의 실행 위치

구현할 함수
-----------
def countdown_trace(start: int) -> list[str]:

예시 및 필수 테스트
-------------------
- countdown_trace(3) == ['tick:3', 'tick:2', 'tick:1', 'go']
- countdown_trace(0) == ['go']
- countdown_trace(1) == ['tick:1', 'go']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0026 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def countdown_trace(start: int) -> list[str]:
    raise NotImplementedError("TODO: PB0026")


def self_test() -> None:
    assert countdown_trace(3) == ['tick:3', 'tick:2', 'tick:1', 'go']
    assert countdown_trace(0) == ['go']
    assert countdown_trace(1) == ['tick:1', 'go']
