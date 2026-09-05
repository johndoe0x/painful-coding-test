"""
PB0191 — 둘 중 하나의 권한

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
관리자이거나 소유자이면 True를 반환하세요.

연습 초점
---------
논리 OR의 기본 진리표

구현할 함수
-----------
def any_permission(is_admin: bool, is_owner: bool) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- any_permission(False, True) is True
- any_permission(False, False) is False
- any_permission(True, True) is True and any_permission(True, False) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0191 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def any_permission(is_admin: bool, is_owner: bool) -> bool:
    raise NotImplementedError("TODO: PB0191")


def self_test() -> None:
    assert any_permission(False, True) is True
    assert any_permission(False, False) is False
    assert any_permission(True, True) is True and any_permission(True, False) is True
