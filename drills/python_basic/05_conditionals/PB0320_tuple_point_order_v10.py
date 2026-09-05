"""
PB0320 — 좌표 tuple 비교

Chapter: Conditional Statements
Topic: Comparison Operators
Seed: 32 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
Python의 tuple 사전식 비교로 first가 앞이면 'first', 같으면 'same', 뒤면 'second'를 반환한다.

연습 초점
---------
tuple 비교 규칙 실습

구현할 함수
-----------
def tuple_point_order(first: tuple[int, int], second: tuple[int, int]) -> str:

예시 및 필수 테스트
-------------------
- tuple_point_order((1, 9), (2, 0)) == 'first'
- tuple_point_order((3, 4), (3, 4)) == 'same'
- tuple_point_order((5, 0), (4, 9)) == 'second'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0320 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def tuple_point_order(first: tuple[int, int], second: tuple[int, int]) -> str:
    raise NotImplementedError("TODO: PB0320")


def self_test() -> None:
    assert tuple_point_order((1, 9), (2, 0)) == 'first'
    assert tuple_point_order((3, 4), (3, 4)) == 'same'
    assert tuple_point_order((5, 0), (4, 9)) == 'second'
