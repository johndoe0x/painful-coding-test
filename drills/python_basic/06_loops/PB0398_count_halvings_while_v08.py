"""
PB0398 — 1 이하까지 절반 횟수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 value가 1보다 큰 동안 while로 절반을 만들고 반복 횟수를 반환한다.

연습 초점
---------
실수 상태 변화 횟수 측정

구현할 함수
-----------
def count_halvings_while(value: float) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_halvings_while(8.0) == 3
- count_halvings_while(1.0) == 0
- count_halvings_while(0.5) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0398 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_halvings_while(value: float) -> int:
    raise NotImplementedError("TODO: PB0398")


def self_test() -> None:
    assert count_halvings_while(8.0) == 3
    assert count_halvings_while(1.0) == 0
    assert count_halvings_while(0.5) == 0
