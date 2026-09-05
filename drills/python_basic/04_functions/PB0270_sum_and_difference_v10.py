"""
PB0270 — 합과 차 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 수의 합과 left-right를 tuple로 반환한다.

연습 초점
---------
여러 계산 결과를 단일 return에 담기

구현할 함수
-----------
def sum_and_difference(left: int, right: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- sum_and_difference(7, 2) == (9, 5)
- sum_and_difference(0, 0) == (0, 0)
- sum_and_difference(-3, 5) == (2, -8)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0270 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sum_and_difference(left: int, right: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0270")


def self_test() -> None:
    assert sum_and_difference(7, 2) == (9, 5)
    assert sum_and_difference(0, 0) == (0, 0)
    assert sum_and_difference(-3, 5) == (2, -8)
