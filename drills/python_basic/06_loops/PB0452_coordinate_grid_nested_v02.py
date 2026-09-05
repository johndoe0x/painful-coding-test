"""
PB0452 — 좌표 격자

Chapter: Loops
Topic: Nested Loops
Seed: 46 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: nested_loop

문제
----
중첩 for로 모든 (행 인덱스, 열 인덱스)를 행 우선 순서로 반환한다.

연습 초점
---------
직교하는 두 인덱스 순회

구현할 함수
-----------
def coordinate_grid_nested(rows: int, columns: int) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- coordinate_grid_nested(2, 3) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
- coordinate_grid_nested(0, 3) == []
- coordinate_grid_nested(1, 1) == [(0, 0)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0452 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def coordinate_grid_nested(rows: int, columns: int) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: PB0452")


def self_test() -> None:
    assert coordinate_grid_nested(2, 3) == [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)]
    assert coordinate_grid_nested(0, 3) == []
    assert coordinate_grid_nested(1, 1) == [(0, 0)]
