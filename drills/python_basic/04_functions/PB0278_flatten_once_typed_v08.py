"""
PB0278 — 이차원 정수 펼치기

Chapter: Functions
Topic: Type Hints
Seed: 28 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
행 순서를 유지하며 이차원 정수 리스트를 한 리스트로 펼친다.

연습 초점
---------
중첩 list 타입 힌트 읽기

구현할 함수
-----------
def flatten_once_typed(rows: list[list[int]]) -> list[int]:

예시 및 필수 테스트
-------------------
- flatten_once_typed([[1, 2], [3]]) == [1, 2, 3]
- flatten_once_typed([]) == []
- flatten_once_typed([[], [-1]]) == [-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0278 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def flatten_once_typed(rows: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: PB0278")


def self_test() -> None:
    assert flatten_once_typed([[1, 2], [3]]) == [1, 2, 3]
    assert flatten_once_typed([]) == []
    assert flatten_once_typed([[], [-1]]) == [-1]
