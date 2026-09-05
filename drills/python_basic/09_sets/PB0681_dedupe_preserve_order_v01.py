"""
PB0681 — 순서 보존 중복 제거

Chapter: Sets
Topic: Set Practice
Seed: 69 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
set으로 등장 여부를 확인하며 최초 등장 순서만 남긴다.

연습 초점
---------
seen set과 순서 보존 리스트

구현할 함수
-----------
def dedupe_preserve_order(values: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- dedupe_preserve_order([2, 1, 2, 3]) == [2, 1, 3]
- dedupe_preserve_order([]) == []
- dedupe_preserve_order([1, 1, 1]) == [1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0681 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dedupe_preserve_order(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0681")


def self_test() -> None:
    assert dedupe_preserve_order([2, 1, 2, 3]) == [2, 1, 3]
    assert dedupe_preserve_order([]) == []
    assert dedupe_preserve_order([1, 1, 1]) == [1]
