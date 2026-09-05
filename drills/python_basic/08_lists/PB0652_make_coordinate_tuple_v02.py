"""
PB0652 — 좌표 tuple 만들기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
x와 y를 그 순서로 담은 2차원 좌표 tuple을 반환한다.

연습 초점
---------
쉼표로 고정된 구조의 불변 tuple을 생성한다.

구현할 함수
-----------
def make_coordinate(x: float, y: float) -> tuple[float, float]:

예시 및 필수 테스트
-------------------
- make_coordinate(1.5, 2.0) == (1.5, 2.0)
- make_coordinate(-1, 0) == (-1, 0)
- make_coordinate(0.0, 0.0) == (0.0, 0.0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0652 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_coordinate(x: float, y: float) -> tuple[float, float]:
    raise NotImplementedError("TODO: PB0652")


def self_test() -> None:
    assert make_coordinate(1.5, 2.0) == (1.5, 2.0)
    assert make_coordinate(-1, 0) == (-1, 0)
    assert make_coordinate(0.0, 0.0) == (0.0, 0.0)
