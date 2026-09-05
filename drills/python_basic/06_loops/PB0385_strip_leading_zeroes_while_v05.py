"""
PB0385 — 앞쪽 0 제거

Chapter: Loops
Topic: While Loops
Seed: 39 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: while

문제
----
while과 인덱스를 사용해 앞의 '0'들을 제거하고, 모두 0이면 빈 문자열을 반환한다.

연습 초점
---------
문자열 경계를 검사하는 while

구현할 함수
-----------
def strip_leading_zeroes_while(text: str) -> str:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- strip_leading_zeroes_while('00042') == '42'
- strip_leading_zeroes_while('000') == ''
- strip_leading_zeroes_while('12') == '12'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0385 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def strip_leading_zeroes_while(text: str) -> str:
    raise NotImplementedError("TODO: PB0385")


def self_test() -> None:
    assert strip_leading_zeroes_while('00042') == '42'
    assert strip_leading_zeroes_while('000') == ''
    assert strip_leading_zeroes_while('12') == '12'
