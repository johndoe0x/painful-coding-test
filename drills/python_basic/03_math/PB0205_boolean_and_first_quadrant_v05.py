"""
PB0205 — 제1사분면 좌표

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
x와 y가 모두 양수이면 True를 반환하세요.

연습 초점
---------
두 축 조건의 AND

구현할 함수
-----------
def is_first_quadrant(x: float, y: float) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- is_first_quadrant(1, 2) is True
- is_first_quadrant(0, 2) is False
- is_first_quadrant(-1, -2) is False and is_first_quadrant(1, 0) is False and is_first_quadrant(1, -2) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0205 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_first_quadrant(x: float, y: float) -> bool:
    raise NotImplementedError("TODO: PB0205")


def self_test() -> None:
    assert is_first_quadrant(1, 2) is True
    assert is_first_quadrant(0, 2) is False
    assert is_first_quadrant(-1, -2) is False and is_first_quadrant(1, 0) is False and is_first_quadrant(1, -2) is False
