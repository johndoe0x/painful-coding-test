"""
PB0395 — 대상 전 원소 수

Chapter: Loops
Topic: While Loops Counting
Seed: 40 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: while

문제
----
인덱스 while로 첫 target 전까지의 원소 수를 반환하고 target이 없으면 전체 길이를 반환한다.

연습 초점
---------
탐색 종료 조건과 카운터

구현할 함수
-----------
def count_before_target_while(values: list[int], target: int) -> int:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- count_before_target_while([4, 7, 9], 7) == 1
- count_before_target_while([], 1) == 0
- count_before_target_while([1, 2], 9) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0395 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def count_before_target_while(values: list[int], target: int) -> int:
    raise NotImplementedError("TODO: PB0395")


def self_test() -> None:
    assert count_before_target_while([4, 7, 9], 7) == 1
    assert count_before_target_while([], 1) == 0
    assert count_before_target_while([1, 2], 9) == 2
