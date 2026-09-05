"""
PB0359 — 비밀번호 길이 단계

Chapter: Conditional Statements
Topic: Else-If Statements
Seed: 36 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: elif

문제
----
길이 0은 empty, 6 미만 weak, 10 미만 medium, 그 이상 strong을 반환한다.

연습 초점
---------
문자열 길이를 여러 단계로 분류

구현할 함수
-----------
def password_length_level(password: str) -> str:

필수 구현 방식
--------------
- elif 경로를 사용한다.

예시 및 필수 테스트
-------------------
- password_length_level('') == 'empty'
- password_length_level('abcde') == 'weak'
- password_length_level('abcdefghij') == 'strong'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0359 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def password_length_level(password: str) -> str:
    raise NotImplementedError("TODO: PB0359")


def self_test() -> None:
    assert password_length_level('') == 'empty'
    assert password_length_level('abcde') == 'weak'
    assert password_length_level('abcdefghij') == 'strong'
