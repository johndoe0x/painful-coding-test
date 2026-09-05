"""
PB0091 — 변화 누적

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
하나의 total 변수를 각 change만큼 재할당해 마지막 값을 반환하세요.

연습 초점
---------
같은 변수의 상태 갱신

구현할 함수
-----------
def running_total(start: int, changes: list[int]) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- running_total(10, [3, -2, 5]) == 16
- running_total(0, []) == 0
- running_total(-1, [1]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0091 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def running_total(start: int, changes: list[int]) -> int:
    raise NotImplementedError("TODO: PB0091")


def self_test() -> None:
    assert running_total(10, [3, -2, 5]) == 16
    assert running_total(0, []) == 0
    assert running_total(-1, [1]) == 0
