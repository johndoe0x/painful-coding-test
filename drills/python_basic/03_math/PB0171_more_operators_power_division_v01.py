"""
PB0171 — 거듭제곱과 실수 나눗셈

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
b는 양의 정수라고 가정하고 a**b와 a/b를 반환하세요. 양의 지수이므로 첫 결과는 int이고 b가 0인 나눗셈도 발생하지 않습니다.

연습 초점
---------
**와 / 연산자

구현할 함수
-----------
def power_and_division(a: int, b: int) -> tuple[int, float]:

예시 및 필수 테스트
-------------------
- power_and_division(8, 2) == (64, 4.0)
- power_and_division(0, 2) == (0, 0.0)
- power_and_division(-4, 2) == (16, -2.0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0171 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def power_and_division(a: int, b: int) -> tuple[int, float]:
    raise NotImplementedError("TODO: PB0171")


def self_test() -> None:
    assert power_and_division(8, 2) == (64, 4.0)
    assert power_and_division(0, 2) == (0, 0.0)
    assert power_and_division(-4, 2) == (16, -2.0)
