"""
PB0118 — 정확한 타입만 고르기

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
sample과 실제 타입이 정확히 같은 값만 순서를 유지해 반환하세요.

연습 초점
---------
isinstance가 아닌 정확한 타입 비교

구현할 함수
-----------
def filter_exact_type(values: list[object], sample: object) -> list[object]:

예시 및 필수 테스트
-------------------
- filter_exact_type([1, True, 2], 0) == [1, 2]
- filter_exact_type([], '') == []
- filter_exact_type([False, 0], True) == [False]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0118 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def filter_exact_type(values: list[object], sample: object) -> list[object]:
    raise NotImplementedError("TODO: PB0118")


def self_test() -> None:
    assert filter_exact_type([1, True, 2], 0) == [1, 2]
    assert filter_exact_type([], '') == []
    assert filter_exact_type([False, 0], True) == [False]
