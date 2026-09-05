"""
PB0277 — 카운트 사전 합치기

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
같은 키의 값을 더해 두 카운트 딕셔너리를 합친다.

연습 초점
---------
중첩된 key·value 타입 힌트

구현할 함수
-----------
def merge_counts_typed(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- merge_counts_typed({'a': 1}, {'a': 2, 'b': 1}) == {'a': 3, 'b': 1}
- merge_counts_typed({}, {}) == {}
- merge_counts_typed({'x': -1}, {'x': 1}) == {'x': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0277 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def merge_counts_typed(left: dict[str, int], right: dict[str, int]) -> dict[str, int]:
    raise NotImplementedError("TODO: PB0277")


def self_test() -> None:
    assert merge_counts_typed({'a': 1}, {'a': 2, 'b': 1}) == {'a': 3, 'b': 1}
    assert merge_counts_typed({}, {}) == {}
    assert merge_counts_typed({'x': -1}, {'x': 1}) == {'x': 0}
