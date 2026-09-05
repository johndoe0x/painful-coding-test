"""
PB0446 — 마지막 대상 인덱스

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
마지막 인덱스부터 역순으로 찾아 첫 target 인덱스를 반환하고 없으면 -1을 반환한다.

연습 초점
---------
역순 탐색으로 마지막 등장 찾기

구현할 함수
-----------
def last_target_index_reverse(values: list[int], target: int) -> int:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- last_target_index_reverse([1, 2, 1], 1) == 2
- last_target_index_reverse([], 1) == -1
- last_target_index_reverse([3, 4], 9) == -1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0446 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def last_target_index_reverse(values: list[int], target: int) -> int:
    raise NotImplementedError("TODO: PB0446")


def self_test() -> None:
    assert last_target_index_reverse([1, 2, 1], 1) == 2
    assert last_target_index_reverse([], 1) == -1
    assert last_target_index_reverse([3, 4], 9) == -1
