"""
PB0510 — 숫자 글자 존재 확인하기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
text에 str.isdigit이 참인 글자가 하나라도 있으면 True를 반환한다.

연습 초점
---------
any와 generator 표현식으로 조기 성공 조건을 표현한다.

구현할 함수
-----------
def contains_digit(text: str) -> bool:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- contains_digit('room 101') is True
- contains_digit('python') is False
- contains_digit('') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0510 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def contains_digit(text: str) -> bool:
    raise NotImplementedError("TODO: PB0510")


def self_test() -> None:
    assert contains_digit('room 101') is True
    assert contains_digit('python') is False
    assert contains_digit('') is False
