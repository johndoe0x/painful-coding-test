"""
PB0392 — while 자릿수 개수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: while

문제
----
절댓값을 10으로 나누는 while로 십진 자릿수를 세며 0은 한 자리로 센다.

연습 초점
---------
값 축소와 카운터 증가

구현할 함수
-----------
def count_digits_while(number: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_digits_while(1205) == 4
- count_digits_while(0) == 1
- count_digits_while(-99) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0392 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_digits_while(number: int) -> int:
    raise NotImplementedError("TODO: PB0392")


def self_test() -> None:
    assert count_digits_while(1205) == 4
    assert count_digits_while(0) == 1
    assert count_digits_while(-99) == 2
