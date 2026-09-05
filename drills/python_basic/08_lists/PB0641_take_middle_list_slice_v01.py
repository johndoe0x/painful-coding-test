"""
PB0641 — 양 끝을 제외한 리스트

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
첫 원소와 마지막 원소를 제외한 새 리스트를 반환하며 길이가 2 이하면 []를 반환한다.

연습 초점
---------
리스트의 반열린 슬라이스와 짧은 입력 결과를 익힌다.

구현할 함수
-----------
def middle_slice(values: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- middle_slice([1, 2, 3, 4]) == [2, 3]
- middle_slice([1, 2]) == []
- middle_slice([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0641 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def middle_slice(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0641")


def self_test() -> None:
    assert middle_slice([1, 2, 3, 4]) == [2, 3]
    assert middle_slice([1, 2]) == []
    assert middle_slice([]) == []
