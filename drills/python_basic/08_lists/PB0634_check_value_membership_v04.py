"""
PB0634 — 목표값 포함 여부

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
target과 같은 원소가 values에 하나라도 있으면 True를 반환한다.

연습 초점
---------
리스트 membership 연산으로 존재 여부를 표현한다.

구현할 함수
-----------
def list_contains(values: list[object], target: object) -> bool:

예시 및 필수 테스트
-------------------
- list_contains(['a', 'b'], 'b') is True
- list_contains([1, 2], 3) is False
- list_contains([], None) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0634 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def list_contains(values: list[object], target: object) -> bool:
    raise NotImplementedError("TODO: PB0634")


def self_test() -> None:
    assert list_contains(['a', 'b'], 'b') is True
    assert list_contains([1, 2], 3) is False
    assert list_contains([], None) is False
