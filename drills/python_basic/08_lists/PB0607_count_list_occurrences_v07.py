"""
PB0607 — 리스트에서 값 개수 세기

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
values에서 target과 같은 원소의 개수를 반환한다.

연습 초점
---------
list.count의 동등성 비교 동작을 사용한다.

구현할 함수
-----------
def occurrence_count(values: list[object], target: object) -> int:

예시 및 필수 테스트
-------------------
- occurrence_count(['a', 'b', 'a'], 'a') == 2
- occurrence_count([1, 2, 3], 9) == 0
- occurrence_count([], None) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0607 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def occurrence_count(values: list[object], target: object) -> int:
    raise NotImplementedError("TODO: PB0607")


def self_test() -> None:
    assert occurrence_count(['a', 'b', 'a'], 'a') == 2
    assert occurrence_count([1, 2, 3], 9) == 0
    assert occurrence_count([], None) == 0
