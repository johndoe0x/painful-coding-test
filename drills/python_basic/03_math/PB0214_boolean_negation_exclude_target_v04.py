"""
PB0214 — 대상이 아닌 값

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
value와 target이 같지 않으면 True를 반환하세요.

연습 초점
---------
동등 조건의 부정

구현할 함수
-----------
def is_not_target(value: object, target: object) -> bool:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- is_not_target(1, 2) is True
- is_not_target('', '') is False
- is_not_target(False, 0) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0214 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_not_target(value: object, target: object) -> bool:
    raise NotImplementedError("TODO: PB0214")


def self_test() -> None:
    assert is_not_target(1, 2) is True
    assert is_not_target('', '') is False
    assert is_not_target(False, 0) is False
