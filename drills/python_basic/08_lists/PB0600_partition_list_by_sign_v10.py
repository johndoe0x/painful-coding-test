"""
PB0600 — 음수·0·양수로 나누기

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: for

문제
----
values를 순회해 음수, 0, 양수를 각각 원래 순서의 리스트로 나누어 tuple로 반환한다.

연습 초점
---------
한 번의 순회에서 세 결과 리스트 중 알맞은 곳에 append한다.

구현할 함수
-----------
def partition_by_sign(values: list[int]) -> tuple[list[int], list[int], list[int]]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- partition_by_sign([-2, 0, 3, -1, 0]) == ([-2, -1], [0, 0], [3])
- partition_by_sign([1, 2]) == ([], [], [1, 2])
- partition_by_sign([]) == ([], [], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0600 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def partition_by_sign(values: list[int]) -> tuple[list[int], list[int], list[int]]:
    raise NotImplementedError("TODO: PB0600")


def self_test() -> None:
    assert partition_by_sign([-2, 0, 3, -1, 0]) == ([-2, -1], [0, 0], [3])
    assert partition_by_sign([1, 2]) == ([], [], [1, 2])
    assert partition_by_sign([]) == ([], [], [])
