"""
PB0166 — 거스름돈

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
paid가 price 이상일 때 지불액에서 가격을 뺀 거스름돈을 반환하세요.

연습 초점
---------
금액의 올바른 뺄셈 방향

구현할 함수
-----------
def calculate_change(price: int, paid: int) -> int:

예시 및 필수 테스트
-------------------
- calculate_change(70, 100) == 30
- calculate_change(0, 0) == 0
- calculate_change(50, 50) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0166 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def calculate_change(price: int, paid: int) -> int:
    raise NotImplementedError("TODO: PB0166")


def self_test() -> None:
    assert calculate_change(70, 100) == 30
    assert calculate_change(0, 0) == 0
    assert calculate_change(50, 50) == 0
