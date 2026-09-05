"""
PB0124 — 타입 변경 횟수

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
인접한 두 값의 실제 타입이 달라진 횟수를 반환하세요.

연습 초점
---------
재할당 시 타입 변경 집계

구현할 함수
-----------
def count_type_changes(values: list[object]) -> int:

예시 및 필수 테스트
-------------------
- count_type_changes([1, '1', 2.0, 3.0]) == 2
- count_type_changes([]) == 0
- count_type_changes([False, 0]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0124 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_type_changes(values: list[object]) -> int:
    raise NotImplementedError("TODO: PB0124")


def self_test() -> None:
    assert count_type_changes([1, '1', 2.0, 3.0]) == 2
    assert count_type_changes([]) == 0
    assert count_type_changes([False, 0]) == 1
