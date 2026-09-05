"""
PB0386 — while 숫자 뒤집기

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while과 나눗셈을 사용해 정수 자릿수를 뒤집고 원래 부호를 유지한다.

연습 초점
---------
몫이 0이 될 때까지 자릿수 소비

구현할 함수
-----------
def reverse_digits_while(number: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- reverse_digits_while(120) == 21
- reverse_digits_while(0) == 0
- reverse_digits_while(-305) == -503

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0386 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reverse_digits_while(number: int) -> int:
    raise NotImplementedError("TODO: PB0386")


def self_test() -> None:
    assert reverse_digits_while(120) == 21
    assert reverse_digits_while(0) == 0
    assert reverse_digits_while(-305) == -503
