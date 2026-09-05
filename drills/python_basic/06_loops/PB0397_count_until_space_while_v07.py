"""
PB0397 — 공백 전 문자 수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while로 첫 공백 전까지의 문자 수를 반환하고 공백이 없으면 전체 길이를 반환한다.

연습 초점
---------
문자열 인덱스 경계와 카운터

구현할 함수
-----------
def count_until_space_while(text: str) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_until_space_while('hello world') == 5
- count_until_space_while('') == 0
- count_until_space_while('abc') == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0397 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_until_space_while(text: str) -> int:
    raise NotImplementedError("TODO: PB0397")


def self_test() -> None:
    assert count_until_space_while('hello world') == 5
    assert count_until_space_while('') == 0
    assert count_until_space_while('abc') == 3
