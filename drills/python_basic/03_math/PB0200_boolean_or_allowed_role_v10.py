"""
PB0200 — 허용 역할

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
role이 'editor' 또는 'viewer'이면 True를 반환하세요.

연습 초점
---------
열거된 선택지의 OR

구현할 함수
-----------
def has_allowed_role(role: str) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- has_allowed_role('editor') is True
- has_allowed_role('') is False
- has_allowed_role('admin') is False and has_allowed_role('viewer') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0200 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_allowed_role(role: str) -> bool:
    raise NotImplementedError("TODO: PB0200")


def self_test() -> None:
    assert has_allowed_role('editor') is True
    assert has_allowed_role('') is False
    assert has_allowed_role('admin') is False and has_allowed_role('viewer') is True
