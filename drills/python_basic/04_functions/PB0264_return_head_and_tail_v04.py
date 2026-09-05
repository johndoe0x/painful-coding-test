"""
PB0264 — 머리와 꼬리 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
빈 리스트면 (None, []), 아니면 첫 원소와 나머지 리스트를 반환한다.

연습 초점
---------
분기마다 명확한 반환값 제공

구현할 함수
-----------
def return_head_and_tail(values: list[int]) -> tuple[int | None, list[int]]:

예시 및 필수 테스트
-------------------
- return_head_and_tail([1, 2, 3]) == (1, [2, 3])
- return_head_and_tail([]) == (None, [])
- return_head_and_tail([-4]) == (-4, [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0264 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def return_head_and_tail(values: list[int]) -> tuple[int | None, list[int]]:
    raise NotImplementedError("TODO: PB0264")


def self_test() -> None:
    assert return_head_and_tail([1, 2, 3]) == (1, [2, 3])
    assert return_head_and_tail([]) == (None, [])
    assert return_head_and_tail([-4]) == (-4, [])
