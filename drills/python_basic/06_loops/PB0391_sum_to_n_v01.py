"""
PB0391 — while 1부터 n 합계

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while 카운터를 사용해 1부터 n까지 합하며 n이 1 미만이면 0을 반환한다.

연습 초점
---------
카운터 증가와 누적값

구현할 함수
-----------
def sum_to_n(n: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- sum_to_n(4) == 10
- sum_to_n(0) == 0
- sum_to_n(1) == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0391 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_to_n(n: int) -> int:
    raise NotImplementedError("TODO: PB0391")


def self_test() -> None:
    assert sum_to_n(4) == 10
    assert sum_to_n(0) == 0
    assert sum_to_n(1) == 1
