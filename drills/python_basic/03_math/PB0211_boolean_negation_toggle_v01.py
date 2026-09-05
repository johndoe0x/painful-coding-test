"""
PB0211 — 불리언 반전

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
논리 부정 not으로 flag를 반전하세요.

연습 초점
---------
not 연산자의 기본 동작

구현할 함수
-----------
def toggle(flag: bool) -> bool:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- toggle(True) is False
- toggle(False) is True
- toggle(bool(0)) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0211 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def toggle(flag: bool) -> bool:
    raise NotImplementedError("TODO: PB0211")


def self_test() -> None:
    assert toggle(True) is False
    assert toggle(False) is True
    assert toggle(bool(0)) is True
