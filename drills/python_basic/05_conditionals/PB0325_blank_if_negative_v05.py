"""
PB0325 — 음수만 빈 문자열

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: if

문제
----
기본으로 number의 문자열을 만들고, 음수일 때만 빈 문자열로 바꾼다.

연습 초점
---------
참인 경우에만 결과 덮어쓰기

구현할 함수
-----------
def blank_if_negative(number: int) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- blank_if_negative(7) == '7'
- blank_if_negative(0) == '0'
- blank_if_negative(-3) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0325 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def blank_if_negative(number: int) -> str:
    raise NotImplementedError("TODO: PB0325")


def self_test() -> None:
    assert blank_if_negative(7) == '7'
    assert blank_if_negative(0) == '0'
    assert blank_if_negative(-3) == ''
