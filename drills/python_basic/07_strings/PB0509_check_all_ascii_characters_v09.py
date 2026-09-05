"""
PB0509 — 모두 ASCII인지 확인하기

Chapter: Strings
Topic: String Looping Shorthand
Seed: 51 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: comprehension

문제
----
모든 문자의 ord 값이 128보다 작으면 True를 반환하며 빈 문자열도 True로 본다.

연습 초점
---------
all과 generator 표현식의 빈 입력 동작을 익힌다.

구현할 함수
-----------
def all_ascii(text: str) -> bool:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- all_ascii('Python 3!') is True
- all_ascii('한글') is False
- all_ascii('') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0509 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def all_ascii(text: str) -> bool:
    raise NotImplementedError("TODO: PB0509")


def self_test() -> None:
    assert all_ascii('Python 3!') is True
    assert all_ascii('한글') is False
    assert all_ascii('') is True
