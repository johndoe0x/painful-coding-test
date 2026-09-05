"""
PB0201 — 두 요구사항

Chapter: Math
Topic: Boolean AND
Seed: 21 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: bool_and

문제
----
두 조건이 모두 참일 때만 True를 반환하세요.

연습 초점
---------
논리 AND의 기본 진리표

구현할 함수
-----------
def all_requirements(age_ok: bool, consent_ok: bool) -> bool:

필수 구현 방식
--------------
- 논리 연산자 and를 사용한다.

예시 및 필수 테스트
-------------------
- all_requirements(True, False) is False
- all_requirements(False, False) is False and all_requirements(False, True) is False
- all_requirements(True, True) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0201 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def all_requirements(age_ok: bool, consent_ok: bool) -> bool:
    raise NotImplementedError("TODO: PB0201")


def self_test() -> None:
    assert all_requirements(True, False) is False
    assert all_requirements(False, False) is False and all_requirements(False, True) is False
    assert all_requirements(True, True) is True
