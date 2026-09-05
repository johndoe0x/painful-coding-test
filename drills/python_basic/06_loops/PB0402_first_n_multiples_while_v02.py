"""
PB0402 — 처음 n개 배수

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while을 사용해 양수 base의 처음 count개 배수를 반환하며 count가 0 이하면 빈 리스트를 반환한다.

연습 초점
---------
배수 인덱스 카운터

구현할 함수
-----------
def first_n_multiples_while(base: int, count: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- first_n_multiples_while(4, 3) == [4, 8, 12]
- first_n_multiples_while(5, 0) == []
- first_n_multiples_while(1, 1) == [1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0402 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_n_multiples_while(base: int, count: int) -> list[int]:
    raise NotImplementedError("TODO: PB0402")


def self_test() -> None:
    assert first_n_multiples_while(4, 3) == [4, 8, 12]
    assert first_n_multiples_while(5, 0) == []
    assert first_n_multiples_while(1, 1) == [1]
