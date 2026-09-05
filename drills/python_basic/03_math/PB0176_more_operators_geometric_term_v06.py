"""
PB0176 — 등비수열 항

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
position이 1 이상일 때 first * ratio ** (position - 1)을 반환하세요.

연습 초점
---------
지수로 등비 반복 표현

구현할 함수
-----------
def geometric_term(first: int, ratio: int, position: int) -> int:

예시 및 필수 테스트
-------------------
- geometric_term(2, 3, 4) == 54
- geometric_term(0, 5, 3) == 0
- geometric_term(7, 2, 1) == 7

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0176 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def geometric_term(first: int, ratio: int, position: int) -> int:
    raise NotImplementedError("TODO: PB0176")


def self_test() -> None:
    assert geometric_term(2, 3, 4) == 54
    assert geometric_term(0, 5, 3) == 0
    assert geometric_term(7, 2, 1) == 7
