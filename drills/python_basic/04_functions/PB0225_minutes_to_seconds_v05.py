"""
PB0225 — 분을 초로 바꾸는 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
분을 초 단위 정수로 변환해 반환한다.

연습 초점
---------
단위 변환 로직을 함수로 캡슐화

구현할 함수
-----------
def minutes_to_seconds(minutes: int) -> int:

예시 및 필수 테스트
-------------------
- minutes_to_seconds(3) == 180
- minutes_to_seconds(0) == 0
- minutes_to_seconds(60) == 3600

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0225 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def minutes_to_seconds(minutes: int) -> int:
    raise NotImplementedError("TODO: PB0225")


def self_test() -> None:
    assert minutes_to_seconds(3) == 180
    assert minutes_to_seconds(0) == 0
    assert minutes_to_seconds(60) == 3600
