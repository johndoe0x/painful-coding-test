"""
PB0215 — 범위 밖 판별

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
minimum <= value <= maximum 조건 전체를 not으로 부정해 반환하세요.

연습 초점
---------
복합 조건 전체의 논리 부정

구현할 함수
-----------
def is_outside_closed_range(value: int, minimum: int, maximum: int) -> bool:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- is_outside_closed_range(0, 1, 3) is True
- is_outside_closed_range(1, 1, 3) is False
- is_outside_closed_range(4, 1, 3) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0215 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_outside_closed_range(value: int, minimum: int, maximum: int) -> bool:
    raise NotImplementedError("TODO: PB0215")


def self_test() -> None:
    assert is_outside_closed_range(0, 1, 3) is True
    assert is_outside_closed_range(1, 1, 3) is False
    assert is_outside_closed_range(4, 1, 3) is True
