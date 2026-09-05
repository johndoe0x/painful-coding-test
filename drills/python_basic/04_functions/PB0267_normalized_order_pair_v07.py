"""
PB0267 — 정렬된 두 값 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
작은 값을 먼저, 큰 값을 나중에 둔 tuple을 반환한다.

연습 초점
---------
모든 실행 경로의 return 확인

구현할 함수
-----------
def normalized_order_pair(left: int, right: int) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- normalized_order_pair(8, 3) == (3, 8)
- normalized_order_pair(2, 2) == (2, 2)
- normalized_order_pair(-1, -5) == (-5, -1)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0267 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def normalized_order_pair(left: int, right: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0267")


def self_test() -> None:
    assert normalized_order_pair(8, 3) == (3, 8)
    assert normalized_order_pair(2, 2) == (2, 2)
    assert normalized_order_pair(-1, -5) == (-5, -1)
