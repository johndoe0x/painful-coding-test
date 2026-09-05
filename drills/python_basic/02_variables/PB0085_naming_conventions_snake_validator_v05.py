"""
PB0085 — snake_case 검사

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
빈 문자열은 False입니다. 모든 문자가 소문자·숫자·밑줄이고 첫 문자는 소문자여야 True를 반환하세요.

연습 초점
---------
유효한 snake_case 식별자 조건

구현할 함수
-----------
def is_snake_case(identifier: str) -> bool:

예시 및 필수 테스트
-------------------
- is_snake_case('user_name2') is True
- is_snake_case('') is False
- is_snake_case('User_Name') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0085 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_snake_case(identifier: str) -> bool:
    raise NotImplementedError("TODO: PB0085")


def self_test() -> None:
    assert is_snake_case('user_name2') is True
    assert is_snake_case('') is False
    assert is_snake_case('User_Name') is False
