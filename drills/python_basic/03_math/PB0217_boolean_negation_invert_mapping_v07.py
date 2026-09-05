"""
PB0217 — 상태 딕셔너리 반전

Chapter: Math
Topic: Boolean Negation
Seed: 22 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks: bool_not

문제
----
모든 값을 not으로 반전하되 키는 그대로인 새 딕셔너리를 반환하세요.

연습 초점
---------
딕셔너리 값의 논리 부정

구현할 함수
-----------
def invert_statuses(statuses: dict[str, bool]) -> dict[str, bool]:

필수 구현 방식
--------------
- 논리 연산자 not을 사용한다.

예시 및 필수 테스트
-------------------
- invert_statuses({'a': True, 'b': False}) == {'a': False, 'b': True}
- invert_statuses({}) == {}
- invert_statuses({'x': False}) == {'x': True}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0217 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def invert_statuses(statuses: dict[str, bool]) -> dict[str, bool]:
    raise NotImplementedError("TODO: PB0217")


def self_test() -> None:
    assert invert_statuses({'a': True, 'b': False}) == {'a': False, 'b': True}
    assert invert_statuses({}) == {}
    assert invert_statuses({'x': False}) == {'x': True}
