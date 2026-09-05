"""
PB0170 — 괄호가 있는 계산

Chapter: Math
Topic: Arithmetic Operators
Seed: 17 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
a와 b를 먼저 더한 뒤 multiplier를 곱한 값을 반환하세요.

연습 초점
---------
괄호로 연산 우선순위 명시

구현할 함수
-----------
def grouped_arithmetic(a: int, b: int, multiplier: int) -> int:

예시 및 필수 테스트
-------------------
- grouped_arithmetic(2, 3, 4) == 20
- grouped_arithmetic(0, 0, 9) == 0
- grouped_arithmetic(-1, 1, 5) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0170 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def grouped_arithmetic(a: int, b: int, multiplier: int) -> int:
    raise NotImplementedError("TODO: PB0170")


def self_test() -> None:
    assert grouped_arithmetic(2, 3, 4) == 20
    assert grouped_arithmetic(0, 0, 9) == 0
    assert grouped_arithmetic(-1, 1, 5) == 0
