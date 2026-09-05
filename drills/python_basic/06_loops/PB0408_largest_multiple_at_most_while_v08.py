"""
PB0408 — 가장 큰 제한 내 배수

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks: while

문제
----
양수 base의 배수를 while로 증가시켜 limit 이하에서 가장 큰 값을 반환하고 하나도 없으면 None을 반환한다.

연습 초점
---------
다음 배수를 보기 전 마지막 값 보존

구현할 함수
-----------
def largest_multiple_at_most_while(limit: int, base: int) -> int | None:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- largest_multiple_at_most_while(10, 3) == 9
- largest_multiple_at_most_while(2, 3) is None
- largest_multiple_at_most_while(6, 2) == 6

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0408 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def largest_multiple_at_most_while(limit: int, base: int) -> int | None:
    raise NotImplementedError("TODO: PB0408")


def self_test() -> None:
    assert largest_multiple_at_most_while(10, 3) == 9
    assert largest_multiple_at_most_while(2, 3) is None
    assert largest_multiple_at_most_while(6, 2) == 6
