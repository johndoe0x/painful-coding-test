"""
PB0366 — 비밀번호 복합 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
길이가 8 이상이고 숫자와 기호가 모두 있다고 전달되면 True를 반환한다.

연습 초점
---------
문자열 경계와 두 불리언의 and

구현할 함수
-----------
def strong_password_conditions(password: str, has_digit: bool, has_symbol: bool) -> bool:

예시 및 필수 테스트
-------------------
- strong_password_conditions('abcdefgh', True, True) is True
- strong_password_conditions('short', True, True) is False
- strong_password_conditions('abcdefgh', True, False) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0366 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def strong_password_conditions(password: str, has_digit: bool, has_symbol: bool) -> bool:
    raise NotImplementedError("TODO: PB0366")


def self_test() -> None:
    assert strong_password_conditions('abcdefgh', True, True) is True
    assert strong_password_conditions('short', True, True) is False
    assert strong_password_conditions('abcdefgh', True, False) is False
