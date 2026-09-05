"""
PB0591 — 반복문으로 리스트 합계

Chapter: Lists
Topic: List Looping
Seed: 60 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: for

문제
----
for loop로 values의 모든 정수를 더해 반환한다.

연습 초점
---------
누적 변수의 초기값을 0으로 두고 원소마다 갱신한다.

구현할 함수
-----------
def sum_list(values: list[int]) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- sum_list([2, 3, 4]) == 9
- sum_list([-2, 2]) == 0
- sum_list([]) == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0591 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_list(values: list[int]) -> int:
    raise NotImplementedError("TODO: PB0591")


def self_test() -> None:
    assert sum_list([2, 3, 4]) == 9
    assert sum_list([-2, 2]) == 0
    assert sum_list([]) == 0
