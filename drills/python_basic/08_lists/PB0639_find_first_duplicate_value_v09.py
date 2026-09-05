"""
PB0639 — 처음 중복이 확인되는 값

Chapter: Lists
Topic: List Find
Seed: 64 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
왼쪽부터 읽을 때 이전에 이미 등장한 첫 값을 반환하고 끝까지 중복이 없으면 None을 반환한다.

연습 초점
---------
검색 과정에서 이미 본 값들을 별도로 추적한다.

구현할 함수
-----------
def first_duplicate_value(values: list[int]) -> int | None:

예시 및 필수 테스트
-------------------
- first_duplicate_value([2, 1, 3, 1, 2]) == 1
- first_duplicate_value([1, 2, 3]) is None
- first_duplicate_value([5, 5]) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0639 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_duplicate_value(values: list[int]) -> int | None:
    raise NotImplementedError("TODO: PB0639")


def self_test() -> None:
    assert first_duplicate_value([2, 1, 3, 1, 2]) == 1
    assert first_duplicate_value([1, 2, 3]) is None
    assert first_duplicate_value([5, 5]) == 5
