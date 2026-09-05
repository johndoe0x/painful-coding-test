"""
PB0470 — None 전 유효 정수 개수

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
None을 만나면 break하고 음수는 continue하며 그전 0 이상 정수 개수를 반환한다.

연습 초점
---------
선택적 값 센티널과 조건부 건너뛰기

구현할 함수
-----------
def count_nonnegative_until_none(values: list[int | None]) -> int:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- count_nonnegative_until_none([-1, 0, 2, None, 3]) == 2
- count_nonnegative_until_none([]) == 0
- count_nonnegative_until_none([None, 1]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0470 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_nonnegative_until_none(values: list[int | None]) -> int:
    raise NotImplementedError("TODO: PB0470")


def self_test() -> None:
    assert count_nonnegative_until_none([-1, 0, 2, None, 3]) == 2
    assert count_nonnegative_until_none([]) == 0
    assert count_nonnegative_until_none([None, 1]) == 0
