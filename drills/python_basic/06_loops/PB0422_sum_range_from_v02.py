"""
PB0422 — 시작 구간 합계

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
for와 range(start, stop)으로 정수 합계를 반환한다.

연습 초점
---------
0이 아닌 시작값의 range 순회

구현할 함수
-----------
def sum_range_from(start: int, stop: int) -> int:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- sum_range_from(3, 6) == 12
- sum_range_from(5, 5) == 0
- sum_range_from(-2, 2) == -2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0422 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_range_from(start: int, stop: int) -> int:
    raise NotImplementedError("TODO: PB0422")


def self_test() -> None:
    assert sum_range_from(3, 6) == 12
    assert sum_range_from(5, 5) == 0
    assert sum_range_from(-2, 2) == -2
