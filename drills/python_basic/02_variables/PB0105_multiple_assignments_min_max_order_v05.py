"""
PB0105 — 작은 값부터 정렬

Chapter: Variables
Topic: Multiple Assignments
Seed: 11 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: multiple_assignment

문제
----
first가 second보다 크면 다중 할당으로 교환해 오름차순 tuple을 반환하세요.

연습 초점
---------
조건부 다중 할당

구현할 함수
-----------
def order_pair(first: int, second: int) -> tuple[int, int]:

필수 구현 방식
--------------
- tuple/list 다중 할당 또는 swap 형태를 사용한다.

예시 및 필수 테스트
-------------------
- order_pair(5, 2) == (2, 5)
- order_pair(0, 0) == (0, 0)
- order_pair(-1, 3) == (-1, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0105 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def order_pair(first: int, second: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: PB0105")


def self_test() -> None:
    assert order_pair(5, 2) == (2, 5)
    assert order_pair(0, 0) == (0, 0)
    assert order_pair(-1, 3) == (-1, 3)
