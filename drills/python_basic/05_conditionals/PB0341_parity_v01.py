"""
PB0341 — 짝수와 홀수

Chapter: Conditional Statements
Topic: If-Else Statements
Seed: 35 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: if_else

문제
----
짝수면 'even', 홀수면 'odd'를 반환한다.

연습 초점
---------
상호 배타적인 if-else 경로

구현할 함수
-----------
def parity(number: int) -> str:

필수 구현 방식
--------------
- else 경로가 있는 if문을 사용한다.

예시 및 필수 테스트
-------------------
- parity(7) == 'odd'
- parity(0) == 'even'
- parity(-4) == 'even'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0341 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def parity(number: int) -> str:
    raise NotImplementedError("TODO: PB0341")


def self_test() -> None:
    assert parity(7) == 'odd'
    assert parity(0) == 'even'
    assert parity(-4) == 'even'
