"""
PB0390 — 짝수 나눗셈 사슬

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: while

문제
----
0이 아닌 정수가 짝수인 동안 while로 2로 나눈 결과들을 반환한다.

연습 초점
---------
조건이 값 변화로 종료되는 while

구현할 함수
-----------
def halve_even_chain_while(number: int) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- halve_even_chain_while(40) == [20, 10, 5]
- halve_even_chain_while(7) == []
- halve_even_chain_while(-8) == [-4, -2, -1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0390 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def halve_even_chain_while(number: int) -> list[int]:
    raise NotImplementedError("TODO: PB0390")


def self_test() -> None:
    assert halve_even_chain_while(40) == [20, 10, 5]
    assert halve_even_chain_while(7) == []
    assert halve_even_chain_while(-8) == [-4, -2, -1]
