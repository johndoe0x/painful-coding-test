"""
PB0265 — 몫과 나머지 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
0이 아닌 divisor로 나눈 몫과 나머지를 tuple로 반환한다.

연습 초점
---------
계산한 두 값을 return으로 묶기

구현할 함수
-----------
def quotient_remainder(number: int, divisor: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- quotient_remainder(17, 5) == (3, 2)
- quotient_remainder(0, 3) == (0, 0)
- quotient_remainder(-7, 3) == (-3, 2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0265 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def quotient_remainder(number: int, divisor: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0265")


def self_test() -> None:
    assert quotient_remainder(17, 5) == (3, 2)
    assert quotient_remainder(0, 3) == (0, 0)
    assert quotient_remainder(-7, 3) == (-3, 2)
