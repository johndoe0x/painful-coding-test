"""
PB0096 — 최솟값 갱신

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
현재 minimum보다 작은 candidate를 만날 때만 변수를 재할당하세요.

연습 초점
---------
조건에 따른 상태 갱신

구현할 함수
-----------
def update_running_minimum(start: int, candidates: list[int]) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- update_running_minimum(10, [8, 12, 3]) == 3
- update_running_minimum(5, []) == 5
- update_running_minimum(0, [0]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0096 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def update_running_minimum(start: int, candidates: list[int]) -> int:
    raise NotImplementedError("TODO: PB0096")


def self_test() -> None:
    assert update_running_minimum(10, [8, 12, 3]) == 3
    assert update_running_minimum(5, []) == 5
    assert update_running_minimum(0, [0]) == 0
