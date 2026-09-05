"""
PB0177 — 거듭제곱 표

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
지수 0부터 max_exponent까지 base**지수를 리스트로 반환하세요.

연습 초점
---------
0제곱 경계와 연속 지수

구현할 함수
-----------
def power_table(base: int, max_exponent: int) -> list[int]:

예시 및 필수 테스트
-------------------
- power_table(2, 3) == [1, 2, 4, 8]
- power_table(5, 0) == [1]
- power_table(0, 2) == [1, 0, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0177 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def power_table(base: int, max_exponent: int) -> list[int]:
    raise NotImplementedError("TODO: PB0177")


def self_test() -> None:
    assert power_table(2, 3) == [1, 2, 4, 8]
    assert power_table(5, 0) == [1]
    assert power_table(0, 2) == [1, 0, 0]
