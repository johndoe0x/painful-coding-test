"""
PB0204 — 비밀번호 기본 조건

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
길이가 8 이상이고 숫자를 하나 이상 포함하면 True를 반환하세요.

연습 초점
---------
길이와 내용 조건 동시 충족

구현할 함수
-----------
def has_password_shape(password: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- has_password_shape('python123') is True and has_password_shape('abcdefg1') is True
- has_password_shape('') is False
- has_password_shape('abcdefgh') is False and has_password_shape('x1') is False and has_password_shape('abcdef1') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0204 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_password_shape(password: str) -> bool:
    raise NotImplementedError("TODO: PB0204")


def self_test() -> None:
    assert has_password_shape('python123') is True and has_password_shape('abcdefg1') is True
    assert has_password_shape('') is False
    assert has_password_shape('abcdefgh') is False and has_password_shape('x1') is False and has_password_shape('abcdef1') is False
