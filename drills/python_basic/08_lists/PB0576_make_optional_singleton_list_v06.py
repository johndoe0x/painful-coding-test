"""
PB0576 — 값이 있을 때만 한 칸 리스트

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
value가 None이면 빈 리스트를, 아니면 value 하나만 든 리스트를 반환한다.

연습 초점
---------
빈 리스트와 단일 원소 리스트를 조건에 따라 생성한다.

구현할 함수
-----------
def optional_singleton(value: object | None) -> list[object]:

예시 및 필수 테스트
-------------------
- optional_singleton('x') == ['x']
- optional_singleton(0) == [0]
- optional_singleton(None) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0576 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_singleton(value: object | None) -> list[object]:
    raise NotImplementedError("TODO: PB0576")


def self_test() -> None:
    assert optional_singleton('x') == ['x']
    assert optional_singleton(0) == [0]
    assert optional_singleton(None) == []
