"""
PB0469 — 정원까지 고유값 수집

Chapter: Loops
Topic: Control Flow
Seed: 47 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: break_or_continue

문제
----
중복 값은 continue하고 고유값 수가 capacity에 도달하면 break해 최초 등장 순서로 반환한다.

연습 초점
---------
continue로 중복 제외 후 조건부 break

구현할 함수
-----------
def unique_until_capacity(values: list[int], capacity: int) -> list[int]:

필수 구현 방식
--------------
- break 또는 continue를 사용한다.

예시 및 필수 테스트
-------------------
- unique_until_capacity([1, 1, 2, 3], 2) == [1, 2]
- unique_until_capacity([], 3) == []
- unique_until_capacity([1, 2], 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0469 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def unique_until_capacity(values: list[int], capacity: int) -> list[int]:
    raise NotImplementedError("TODO: PB0469")


def self_test() -> None:
    assert unique_until_capacity([1, 1, 2, 3], 2) == [1, 2]
    assert unique_until_capacity([], 3) == []
    assert unique_until_capacity([1, 2], 0) == []
