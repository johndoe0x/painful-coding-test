"""
PB0632 — 마지막 일치 인덱스 찾기

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
target과 같은 마지막 원소의 인덱스를 반환하고 없으면 -1을 반환한다.

연습 초점
---------
뒤에서 검색하되 원래 리스트의 인덱스를 정확히 반환한다.

구현할 함수
-----------
def find_last_index(values: list[object], target: object) -> int:

예시 및 필수 테스트
-------------------
- find_last_index(['a', 'b', 'a'], 'a') == 2
- find_last_index([1, 2, 3], 2) == 1
- find_last_index([], None) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0632 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def find_last_index(values: list[object], target: object) -> int:
    raise NotImplementedError("TODO: PB0632")


def self_test() -> None:
    assert find_last_index(['a', 'b', 'a'], 'a') == 2
    assert find_last_index([1, 2, 3], 2) == 1
    assert find_last_index([], None) == -1
