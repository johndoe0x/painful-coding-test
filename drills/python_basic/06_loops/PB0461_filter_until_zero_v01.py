"""
PB0461 — 0 전 양수 수집

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
for에서 0을 만나면 break하고 음수는 continue해 그전 양수만 반환한다.

연습 초점
---------
break와 continue를 한 반복에서 구분

구현할 함수
-----------
def filter_until_zero(numbers: list[int]) -> list[int]:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- filter_until_zero([-1, 2, 3, 0, 4]) == [2, 3]
- filter_until_zero([]) == []
- filter_until_zero([0, 1]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0461 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def filter_until_zero(numbers: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0461")


def self_test() -> None:
    assert filter_until_zero([-1, 2, 3, 0, 4]) == [2, 3]
    assert filter_until_zero([]) == []
    assert filter_until_zero([0, 1]) == []
