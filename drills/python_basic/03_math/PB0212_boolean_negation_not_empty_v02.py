"""
PB0212 — 비어 있지 않은 문자열

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
text가 빈 문자열이 아닐 때 True를 반환하되 not을 사용하세요.

연습 초점
---------
falsy 문자열의 논리 부정

구현할 함수
-----------
def is_not_empty(text: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- is_not_empty('x') is True
- is_not_empty('') is False
- is_not_empty(' ') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0212 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_not_empty(text: str) -> bool:
    raise NotImplementedError("TODO: PB0212")


def self_test() -> None:
    assert is_not_empty('x') is True
    assert is_not_empty('') is False
    assert is_not_empty(' ') is True
