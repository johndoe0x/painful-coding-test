"""
PB0396 — 짝수 인덱스 개수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while로 유효한 인덱스를 순회해 0,2,4처럼 짝수 인덱스의 개수를 반환한다.

연습 초점
---------
인덱스 조건을 카운트

구현할 함수
-----------
def count_even_indices_while(values: list[object]) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_even_indices_while(['a', 'b', 'c', 'd']) == 2
- count_even_indices_while([]) == 0
- count_even_indices_while([None]) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0396 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_even_indices_while(values: list[object]) -> int:
    raise NotImplementedError("TODO: PB0396")


def self_test() -> None:
    assert count_even_indices_while(['a', 'b', 'c', 'd']) == 2
    assert count_even_indices_while([]) == 0
    assert count_even_indices_while([None]) == 1
