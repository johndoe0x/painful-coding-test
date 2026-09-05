"""
PB0092 — 상한·하한이 있는 재고 갱신

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
0 <= initial_quantity <= capacity이고 capacity >= 0이라고 가정합니다. 각 transaction을 quantity에 더한 직후 0 미만이면 0, capacity 초과이면 capacity로 재할당해 최종 재고를 반환하세요.

연습 초점
---------
매 단계에서 상태를 갱신하고 범위로 보정

구현할 함수
-----------
def update_inventory(initial_quantity: int, transactions: list[int], capacity: int) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- update_inventory(8, [5, -3], 10) == 7
- update_inventory(2, [-5, 4], 10) == 4
- update_inventory(0, [], 5) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0092 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def update_inventory(initial_quantity: int, transactions: list[int], capacity: int) -> int:
    raise NotImplementedError("TODO: PB0092")


def self_test() -> None:
    assert update_inventory(8, [5, -3], 10) == 7
    assert update_inventory(2, [-5, 4], 10) == 4
    assert update_inventory(0, [], 5) == 0
