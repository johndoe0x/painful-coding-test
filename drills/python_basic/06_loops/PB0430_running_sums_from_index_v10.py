"""
PB0430 — 시작 위치부터 누적 합

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(values)라고 가정하고 for와 range(start, len(values))로 start부터 누적한 중간 합계를 반환한다.

연습 초점
---------
유효한 시작 지점의 누적 순회

구현할 함수
-----------
def running_sums_from_index(values: list[int], start: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- running_sums_from_index([5, 1, 2, 3], 1) == [1, 3, 6]
- running_sums_from_index([], 0) == []
- running_sums_from_index([7], 1) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0430 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def running_sums_from_index(values: list[int], start: int) -> list[int]:
    raise NotImplementedError("TODO: PB0430")


def self_test() -> None:
    assert running_sums_from_index([5, 1, 2, 3], 1) == [1, 3, 6]
    assert running_sums_from_index([], 0) == []
    assert running_sums_from_index([7], 1) == []
