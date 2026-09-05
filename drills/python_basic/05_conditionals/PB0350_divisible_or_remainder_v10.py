"""
PB0350 — 나누어떨어짐 구분

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
0이 아닌 divisor로 나누어떨어지면 'divisible', 아니면 'remainder'를 반환한다.

연습 초점
---------
나머지 비교를 if-else로 완결

구현할 함수
-----------
def divisible_or_remainder(number: int, divisor: int) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- divisible_or_remainder(12, 3) == 'divisible'
- divisible_or_remainder(10, 3) == 'remainder'
- divisible_or_remainder(-8, 2) == 'divisible'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0350 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def divisible_or_remainder(number: int, divisor: int) -> str:
    raise NotImplementedError("TODO: PB0350")


def self_test() -> None:
    assert divisible_or_remainder(12, 3) == 'divisible'
    assert divisible_or_remainder(10, 3) == 'remainder'
    assert divisible_or_remainder(-8, 2) == 'divisible'
