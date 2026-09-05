"""
PB0410 — while 곱셈표 한 행

Chapter: Loops
Topic: While Loops Multiples
Seed: 41 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while로 number*1부터 number*width까지 반환하며 width가 0 이하면 빈 리스트를 반환한다.

연습 초점
---------
순번을 곱해 배수 행 생성

구현할 함수
-----------
def multiplication_row_while(number: int, width: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- multiplication_row_while(7, 3) == [7, 14, 21]
- multiplication_row_while(5, 0) == []
- multiplication_row_while(-2, 2) == [-2, -4]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0410 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def multiplication_row_while(number: int, width: int) -> list[int]:
    raise NotImplementedError("TODO: PB0410")


def self_test() -> None:
    assert multiplication_row_while(7, 3) == [7, 14, 21]
    assert multiplication_row_while(5, 0) == []
    assert multiplication_row_while(-2, 2) == [-2, -4]
