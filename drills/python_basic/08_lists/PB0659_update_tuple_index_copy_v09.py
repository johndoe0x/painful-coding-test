"""
PB0659 — tuple 한 원소 교체하기

Chapter: Lists
Topic: Tuples
Seed: 66 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정해 해당 위치만 value로 교체한 새 tuple을 반환한다.

연습 초점
---------
tuple은 직접 수정할 수 없으므로 슬라이스와 단일 원소 tuple을 결합한다.

구현할 함수
-----------
def update_tuple_at(values: tuple[int, ...], index: int, value: int) -> tuple[int, ...]:

예시 및 필수 테스트
-------------------
- update_tuple_at((1, 2, 3), 1, 9) == (1, 9, 3)
- update_tuple_at((5,), 0, 7) == (7,)
- update_tuple_at((1, 2, 3), -1, 0) == (1, 2, 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0659 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def update_tuple_at(values: tuple[int, ...], index: int, value: int) -> tuple[int, ...]:
    raise NotImplementedError("TODO: PB0659")


def self_test() -> None:
    assert update_tuple_at((1, 2, 3), 1, 9) == (1, 9, 3)
    assert update_tuple_at((5,), 0, 7) == (7,)
    assert update_tuple_at((1, 2, 3), -1, 0) == (1, 2, 0)
