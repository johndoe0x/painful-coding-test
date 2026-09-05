"""
PB0404 — 구간 배수 개수

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: while

문제
----
start 이상 stop 이하 정수 중 양수 base의 배수 개수를 while로 센다.

연습 초점
---------
임의 시작 구간에서 배수 판정

구현할 함수
-----------
def count_multiples_interval_while(start: int, stop: int, base: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_multiples_interval_while(3, 10, 3) == 3
- count_multiples_interval_while(5, 4, 2) == 0
- count_multiples_interval_while(-3, 3, 3) == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0404 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_multiples_interval_while(start: int, stop: int, base: int) -> int:
    raise NotImplementedError("TODO: PB0404")


def self_test() -> None:
    assert count_multiples_interval_while(3, 10, 3) == 3
    assert count_multiples_interval_while(5, 4, 2) == 0
    assert count_multiples_interval_while(-3, 3, 3) == 3
