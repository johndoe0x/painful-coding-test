"""
PB0180 — 거듭제곱 차이

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
base**high - base**low를 반환하세요.

연습 초점
---------
여러 지수식 조합

구현할 함수
-----------
def power_difference(base: int, high: int, low: int) -> int:

예시 및 필수 테스트
-------------------
- power_difference(2, 4, 2) == 12
- power_difference(1, 10, 0) == 0
- power_difference(3, 1, 1) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0180 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def power_difference(base: int, high: int, low: int) -> int:
    raise NotImplementedError("TODO: PB0180")


def self_test() -> None:
    assert power_difference(2, 4, 2) == 12
    assert power_difference(1, 10, 0) == 0
    assert power_difference(3, 1, 1) == 0
