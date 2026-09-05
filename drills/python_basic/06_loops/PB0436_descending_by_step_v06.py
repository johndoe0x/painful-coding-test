"""
PB0436 — 고정 폭 감소

Chapter: Loops
Topic: For Loops Step
Seed: 44 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
양수 step을 음수 간격으로 사용해 start부터 stop 초과까지 감소하는 값을 반환한다.

연습 초점
---------
음수 step으로 역방향 range

구현할 함수
-----------
def descending_by_step(start: int, stop: int, step: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- descending_by_step(10, 3, 2) == [10, 8, 6, 4]
- descending_by_step(3, 3, 1) == []
- descending_by_step(2, -3, 2) == [2, 0, -2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0436 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def descending_by_step(start: int, stop: int, step: int) -> list[int]:
    raise NotImplementedError("TODO: PB0436")


def self_test() -> None:
    assert descending_by_step(10, 3, 2) == [10, 8, 6, 4]
    assert descending_by_step(3, 3, 1) == []
    assert descending_by_step(2, -3, 2) == [2, 0, -2]
