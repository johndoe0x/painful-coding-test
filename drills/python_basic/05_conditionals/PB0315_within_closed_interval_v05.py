"""
PB0315 — 닫힌 구간 판정

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
정수 value가 양쪽 끝점을 포함하는 [low, high] 구간 안에 놓이는지 판정한다.

연습 초점
---------
이상·이하 경계 비교

구현할 함수
-----------
def within_closed_interval(value: int, low: int, high: int) -> bool:

예시 및 필수 테스트
-------------------
- within_closed_interval(5, 1, 9) is True
- within_closed_interval(1, 1, 9) is True
- within_closed_interval(10, 1, 9) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0315 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def within_closed_interval(value: int, low: int, high: int) -> bool:
    raise NotImplementedError("TODO: PB0315")


def self_test() -> None:
    assert within_closed_interval(5, 1, 9) is True
    assert within_closed_interval(1, 1, 9) is True
    assert within_closed_interval(10, 1, 9) is False
