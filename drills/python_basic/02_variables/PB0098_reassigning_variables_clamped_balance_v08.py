"""
PB0098 — 잔액을 0 아래로 막기

Chapter: Variables
Topic: Reassigning Variables
Seed: 10 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: reassignment

문제
----
각 expense를 뺀 뒤 balance가 음수가 되면 즉시 0으로 재할당해 계속 처리하세요.

연습 초점
---------
갱신 후 경계값으로 보정

구현할 함수
-----------
def spend_with_floor(balance: int, expenses: list[int]) -> int:

필수 구현 방식
--------------
- 같은 지역 상태를 다시 할당하거나 복합 할당으로 갱신한다.

예시 및 필수 테스트
-------------------
- spend_with_floor(10, [3, 20, 1]) == 0
- spend_with_floor(0, []) == 0
- spend_with_floor(5, [5]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0098 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def spend_with_floor(balance: int, expenses: list[int]) -> int:
    raise NotImplementedError("TODO: PB0098")


def self_test() -> None:
    assert spend_with_floor(10, [3, 20, 1]) == 0
    assert spend_with_floor(0, []) == 0
    assert spend_with_floor(5, [5]) == 0
