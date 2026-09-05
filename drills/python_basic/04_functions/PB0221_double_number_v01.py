"""
PB0221 — 숫자 두 배 함수

Chapter: Functions
Topic: Introduction to Functions
Seed: 23 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
정수 하나를 받아 두 배인 정수를 반환한다.

연습 초점
---------
함수 선언·호출·반환값의 기본 흐름

구현할 함수
-----------
def double(number: int) -> int:

예시 및 필수 테스트
-------------------
- double(7) == 14
- double(0) == 0
- double(-6) == -12

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0221 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def double(number: int) -> int:
    raise NotImplementedError("TODO: PB0221")


def self_test() -> None:
    assert double(7) == 14
    assert double(0) == 0
    assert double(-6) == -12
