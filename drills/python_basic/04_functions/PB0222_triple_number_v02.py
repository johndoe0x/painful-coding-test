"""
PB0222 — 숫자 세 배 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
숫자 하나를 받아 세 배인 값을 반환한다.

연습 초점
---------
매개변수를 계산식에 사용해 반환하기

구현할 함수
-----------
def triple_number(number: float) -> float:

예시 및 필수 테스트
-------------------
- triple_number(2.5) == 7.5
- triple_number(0.0) == 0.0
- triple_number(-4.0) == -12.0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0222 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def triple_number(number: float) -> float:
    raise NotImplementedError("TODO: PB0222")


def self_test() -> None:
    assert triple_number(2.5) == 7.5
    assert triple_number(0.0) == 0.0
    assert triple_number(-4.0) == -12.0
