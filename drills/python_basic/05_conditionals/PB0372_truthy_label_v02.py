"""
PB0372 — Truthiness 라벨

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: if

문제
----
value가 truthy면 'present', falsy면 'empty'를 반환한다.

연습 초점
---------
여러 타입의 truthy·falsy 판정

구현할 함수
-----------
def truthy_label(value: object) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- truthy_label([]) == 'empty'
- truthy_label([0]) == 'present'
- truthy_label(None) == 'empty'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0372 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def truthy_label(value: object) -> str:
    raise NotImplementedError("TODO: PB0372")


def self_test() -> None:
    assert truthy_label([]) == 'empty'
    assert truthy_label([0]) == 'present'
    assert truthy_label(None) == 'empty'
