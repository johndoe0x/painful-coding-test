"""
PB0405 — 음수 배수 나열

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 base에 대해 -base부터 시작하는 음수 배수 count개를 while로 반환한다.

연습 초점
---------
음의 방향 배수 진행

구현할 함수
-----------
def negative_multiples_while(base: int, count: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- negative_multiples_while(3, 3) == [-3, -6, -9]
- negative_multiples_while(5, 0) == []
- negative_multiples_while(1, 2) == [-1, -2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0405 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def negative_multiples_while(base: int, count: int) -> list[int]:
    raise NotImplementedError("TODO: PB0405")


def self_test() -> None:
    assert negative_multiples_while(3, 3) == [-3, -6, -9]
    assert negative_multiples_while(5, 0) == []
    assert negative_multiples_while(1, 2) == [-1, -2]
