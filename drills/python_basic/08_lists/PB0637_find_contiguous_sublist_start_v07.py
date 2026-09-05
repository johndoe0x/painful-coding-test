"""
PB0637 — 연속 부분 리스트 시작 위치

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
pattern이 values에 연속으로 처음 등장하는 시작 인덱스를 반환하며, 빈 pattern은 0, 없으면 -1을 반환한다.

연습 초점
---------
가능한 시작 위치마다 같은 길이의 슬라이스를 비교한다.

구현할 함수
-----------
def find_sublist_start(values: list[int], pattern: list[int]) -> int:

예시 및 필수 테스트
-------------------
- find_sublist_start([1, 2, 3, 2, 3], [2, 3]) == 1
- find_sublist_start([1, 2], [3]) == -1
- find_sublist_start([1, 2], []) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0637 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def find_sublist_start(values: list[int], pattern: list[int]) -> int:
    raise NotImplementedError("TODO: PB0637")


def self_test() -> None:
    assert find_sublist_start([1, 2, 3, 2, 3], [2, 3]) == 1
    assert find_sublist_start([1, 2], [3]) == -1
    assert find_sublist_start([1, 2], []) == 0
