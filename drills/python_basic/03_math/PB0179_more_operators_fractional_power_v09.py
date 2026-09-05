"""
PB0179 — 제곱 후 나누기

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
left와 right를 각각 exponent제곱한 뒤 둘의 합을 2로 나누세요.

연습 초점
---------
거듭제곱 결과의 실수 나눗셈

구현할 함수
-----------
def powered_average(left: float, right: float, exponent: int) -> float:

예시 및 필수 테스트
-------------------
- powered_average(2, 4, 2) == 10.0
- powered_average(0, 0, 3) == 0.0
- powered_average(-1, 1, 2) == 1.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0179 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def powered_average(left: float, right: float, exponent: int) -> float:
    raise NotImplementedError("TODO: PB0179")


def self_test() -> None:
    assert powered_average(2, 4, 2) == 10.0
    assert powered_average(0, 0, 3) == 0.0
    assert powered_average(-1, 1, 2) == 1.0
