"""
PB0115 — 컬렉션 타입 구분

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
list, tuple, set, dict를 타입 이름으로 반환하고 나머지는 'scalar'로 반환하세요.

연습 초점
---------
기본 컬렉션 타입 식별

구현할 함수
-----------
def collection_kind(value: object) -> str:

예시 및 필수 테스트
-------------------
- collection_kind([1]) == 'list'
- collection_kind({}) == 'dict'
- collection_kind('') == 'scalar'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0115 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def collection_kind(value: object) -> str:
    raise NotImplementedError("TODO: PB0115")


def self_test() -> None:
    assert collection_kind([1]) == 'list'
    assert collection_kind({}) == 'dict'
    assert collection_kind('') == 'scalar'
