"""
PB0389 — 목표 증가 횟수

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: while

문제
----
start가 target보다 작은 동안 while로 1씩 증가시켜 필요한 횟수를 반환하며 start가 크거나 같으면 0을 반환한다.

연습 초점
---------
단조 증가 while와 횟수 상태

구현할 함수
-----------
def increment_steps_while(start: int, target: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- increment_steps_while(2, 5) == 3
- increment_steps_while(5, 5) == 0
- increment_steps_while(7, 3) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0389 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def increment_steps_while(start: int, target: int) -> int:
    raise NotImplementedError("TODO: PB0389")


def self_test() -> None:
    assert increment_steps_while(2, 5) == 3
    assert increment_steps_while(5, 5) == 0
    assert increment_steps_while(7, 3) == 0
