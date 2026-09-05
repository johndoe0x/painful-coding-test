"""
PB0120 — 등장한 타입 종류

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
처음 등장한 순서대로 중복 없는 실제 타입 이름 리스트를 반환하세요.

연습 초점
---------
타입 다양성과 순서 보존

구현할 함수
-----------
def distinct_type_names(values: list[object]) -> list[str]:

예시 및 필수 테스트
-------------------
- distinct_type_names([1, 'a', 2, True, 'b']) == ['int', 'str', 'bool']
- distinct_type_names([]) == []
- distinct_type_names([None, None]) == ['NoneType']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0120 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def distinct_type_names(values: list[object]) -> list[str]:
    raise NotImplementedError("TODO: PB0120")


def self_test() -> None:
    assert distinct_type_names([1, 'a', 2, True, 'b']) == ['int', 'str', 'bool']
    assert distinct_type_names([]) == []
    assert distinct_type_names([None, None]) == ['NoneType']
