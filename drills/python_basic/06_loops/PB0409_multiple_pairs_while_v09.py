"""
PB0409 — 배수와 순번 쌍

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while로 순번 1부터 count까지 (순번, base의 배수) tuple을 만들어 반환한다.

연습 초점
---------
배수 값과 카운터를 함께 활용

구현할 함수
-----------
def multiple_pairs_while(base: int, count: int) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- multiple_pairs_while(3, 3) == [(1, 3), (2, 6), (3, 9)]
- multiple_pairs_while(4, 0) == []
- multiple_pairs_while(-2, 2) == [(1, -2), (2, -4)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0409 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiple_pairs_while(base: int, count: int) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: PB0409")


def self_test() -> None:
    assert multiple_pairs_while(3, 3) == [(1, 3), (2, 6), (3, 9)]
    assert multiple_pairs_while(4, 0) == []
    assert multiple_pairs_while(-2, 2) == [(1, -2), (2, -4)]
