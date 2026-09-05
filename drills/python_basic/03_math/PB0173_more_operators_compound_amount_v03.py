"""
PB0173 — 복리 성장

Chapter: Math
Topic: More Operators
Seed: 18 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
principal * (1 + rate) ** years를 반환하세요.

연습 초점
---------
거듭제곱으로 반복 성장 표현

구현할 함수
-----------
def compound_amount(principal: float, rate: float, years: int) -> float:

예시 및 필수 테스트
-------------------
- compound_amount(100, 0.25, 2) == 156.25
- compound_amount(0, 0.5, 3) == 0.0
- compound_amount(50, 0, 10) == 50

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0173 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def compound_amount(principal: float, rate: float, years: int) -> float:
    raise NotImplementedError("TODO: PB0173")


def self_test() -> None:
    assert compound_amount(100, 0.25, 2) == 156.25
    assert compound_amount(0, 0.5, 3) == 0.0
    assert compound_amount(50, 0, 10) == 50
