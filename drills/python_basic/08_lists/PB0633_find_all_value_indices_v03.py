"""
PB0633 — 모든 일치 위치 찾기

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
target과 같은 모든 원소의 인덱스를 왼쪽부터 반환한다.

연습 초점
---------
enumerate 순회 중 여러 일치 위치를 수집한다.

구현할 함수
-----------
def find_all_indices(values: list[object], target: object) -> list[int]:

예시 및 필수 테스트
-------------------
- find_all_indices(['a', 'b', 'a'], 'a') == [0, 2]
- find_all_indices([1, 2], 9) == []
- find_all_indices([], None) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0633 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def find_all_indices(values: list[object], target: object) -> list[int]:
    raise NotImplementedError("TODO: PB0633")


def self_test() -> None:
    assert find_all_indices(['a', 'b', 'a'], 'a') == [0, 2]
    assert find_all_indices([1, 2], 9) == []
    assert find_all_indices([], None) == []
