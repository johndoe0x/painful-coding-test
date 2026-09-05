"""
PB0445 — 뒤에서 누적 합

Chapter: Loops
Topic: For Loops Reverse
Seed: 45 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
마지막 원소부터 역순으로 더할 때마다 누적 합을 반환한다.

연습 초점
---------
역순 for의 상태 누적

구현할 함수
-----------
def cumulative_sums_from_end(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- cumulative_sums_from_end([1, 2, 3]) == [3, 5, 6]
- cumulative_sums_from_end([]) == []
- cumulative_sums_from_end([-2, 2]) == [2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0445 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cumulative_sums_from_end(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0445")


def self_test() -> None:
    assert cumulative_sums_from_end([1, 2, 3]) == [3, 5, 6]
    assert cumulative_sums_from_end([]) == []
    assert cumulative_sums_from_end([-2, 2]) == [2, 0]
