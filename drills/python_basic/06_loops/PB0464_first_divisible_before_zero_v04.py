"""
PB0464 — 0 전 첫 배수

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
0이 아닌 divisor에 대해 0을 만나면 break하고 그전에 처음 나누어떨어지는 수를 반환하며 없으면 None을 반환한다.

연습 초점
---------
탐색 성공 또는 센티널 break

구현할 함수
-----------
def first_divisible_before_zero(numbers: list[int], divisor: int) -> int | None:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- first_divisible_before_zero([5, 8, 0, 12], 4) == 8
- first_divisible_before_zero([5, 0, 8], 4) is None
- first_divisible_before_zero([], 3) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0464 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_divisible_before_zero(numbers: list[int], divisor: int) -> int | None:
    raise NotImplementedError("TODO: PB0464")


def self_test() -> None:
    assert first_divisible_before_zero([5, 8, 0, 12], 4) == 8
    assert first_divisible_before_zero([5, 0, 8], 4) is None
    assert first_divisible_before_zero([], 3) is None
