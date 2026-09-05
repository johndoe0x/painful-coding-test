"""
PB0606 — 역순 복사 리스트

Chapter: Lists
Topic: List Functions
Seed: 61 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
values의 원소 순서를 뒤집은 새 리스트를 반환하고 원본은 변경하지 않는다.

연습 초점
---------
reversed 결과를 list로 변환하거나 역순 슬라이스를 사용한다.

구현할 함수
-----------
def reversed_list_copy(values: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), reversed_list_copy(items) == [3, 2, 1] and items == [1, 2, 3])[-1] is True
- reversed_list_copy([7]) == [7]
- reversed_list_copy([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0606 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def reversed_list_copy(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0606")


def self_test() -> None:
    assert ((items := [1, 2, 3]), reversed_list_copy(items) == [3, 2, 1] and items == [1, 2, 3])[-1] is True
    assert reversed_list_copy([7]) == [7]
    assert reversed_list_copy([]) == []
