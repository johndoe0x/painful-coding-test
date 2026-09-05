"""
PB0608 — 모두 0 이상인지 확인하기

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
모든 원소가 0 이상이면 True를 반환하며 빈 리스트도 True로 본다.

연습 초점
---------
all에 원소별 비교 generator를 전달한다.

구현할 함수
-----------
def all_nonnegative(values: list[int]) -> bool:

예시 및 필수 테스트
-------------------
- all_nonnegative([0, 2, 5]) is True
- all_nonnegative([1, -1, 3]) is False
- all_nonnegative([]) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0608 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def all_nonnegative(values: list[int]) -> bool:
    raise NotImplementedError("TODO: PB0608")


def self_test() -> None:
    assert all_nonnegative([0, 2, 5]) is True
    assert all_nonnegative([1, -1, 3]) is False
    assert all_nonnegative([]) is True
