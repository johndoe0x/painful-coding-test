"""
PB0393 — 0까지 감소 횟수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 number를 while로 1씩 줄여 0이 되는 횟수를 반환하고 0 이하면 0을 반환한다.

연습 초점
---------
종료 조건과 반복 횟수 카운팅

구현할 함수
-----------
def steps_down_to_zero(number: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- steps_down_to_zero(5) == 5
- steps_down_to_zero(0) == 0
- steps_down_to_zero(-3) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0393 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def steps_down_to_zero(number: int) -> int:
    raise NotImplementedError("TODO: PB0393")


def self_test() -> None:
    assert steps_down_to_zero(5) == 5
    assert steps_down_to_zero(0) == 0
    assert steps_down_to_zero(-3) == 0
