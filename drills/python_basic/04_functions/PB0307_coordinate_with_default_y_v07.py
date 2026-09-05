"""
PB0307 — 기본 y 좌표

Chapter: Functions
Topic: Default Arguments
Seed: 31 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
x와 y 좌표를 tuple로 반환하며 y 생략 시 0을 사용한다.

연습 초점
---------
필수 인자 뒤의 기본 인자

구현할 함수
-----------
def coordinate_with_default_y(x: int, y: int = 0) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- coordinate_with_default_y(4) == (4, 0)
- coordinate_with_default_y(4, 7) == (4, 7)
- coordinate_with_default_y(-1, -2) == (-1, -2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0307 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def coordinate_with_default_y(x: int, y: int = 0) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0307")


def self_test() -> None:
    assert coordinate_with_default_y(4) == (4, 0)
    assert coordinate_with_default_y(4, 7) == (4, 7)
    assert coordinate_with_default_y(-1, -2) == (-1, -2)
