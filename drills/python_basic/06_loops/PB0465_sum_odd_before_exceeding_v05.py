"""
PB0465 — 상한 초과 전 홀수 합

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
limit보다 큰 수에서 break하고 짝수는 continue하며 그전 홀수만 합산한다.

연습 초점
---------
종료 조건과 제외 조건의 우선순위

구현할 함수
-----------
def sum_odd_before_exceeding(numbers: list[int], limit: int) -> int:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- sum_odd_before_exceeding([1, 2, 3, 10, 5], 5) == 4
- sum_odd_before_exceeding([], 5) == 0
- sum_odd_before_exceeding([2, 4, 6], 9) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0465 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_odd_before_exceeding(numbers: list[int], limit: int) -> int:
    raise NotImplementedError("TODO: PB0465")


def self_test() -> None:
    assert sum_odd_before_exceeding([1, 2, 3, 10, 5], 5) == 4
    assert sum_odd_before_exceeding([], 5) == 0
    assert sum_odd_before_exceeding([2, 4, 6], 9) == 0
