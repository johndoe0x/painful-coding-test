"""
PB0127 — 타입별 마지막 값

Chapter: Variables
Topic: Dynamic Typing
Seed: 13 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 실제 타입 이름별로 마지막에 등장한 값을 저장해 반환하세요.

연습 초점
---------
동적 타입 키의 값 갱신

구현할 함수
-----------
def latest_value_by_type(values: list[object]) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- latest_value_by_type([1, 'a', 2]) == {'int': 2, 'str': 'a'}
- latest_value_by_type([]) == {}
- latest_value_by_type([False, True]) == {'bool': True}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0127 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def latest_value_by_type(values: list[object]) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0127")


def self_test() -> None:
    assert latest_value_by_type([1, 'a', 2]) == {'int': 2, 'str': 'a'}
    assert latest_value_by_type([]) == {}
    assert latest_value_by_type([False, True]) == {'bool': True}
