"""
PB0406 — 공통 배수 찾기

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: while

문제
----
1부터 limit까지 while로 확인해 양수 first와 second 모두의 배수인 수를 반환한다.

연습 초점
---------
두 배수 조건과 while 탐색

구현할 함수
-----------
def common_multiples_while(limit: int, first: int, second: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- common_multiples_while(20, 4, 6) == [12]
- common_multiples_while(5, 2, 3) == []
- common_multiples_while(12, 3, 4) == [12]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0406 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def common_multiples_while(limit: int, first: int, second: int) -> list[int]:
    raise NotImplementedError("TODO: PB0406")


def self_test() -> None:
    assert common_multiples_while(20, 4, 6) == [12]
    assert common_multiples_while(5, 2, 3) == []
    assert common_multiples_while(12, 3, 4) == [12]
