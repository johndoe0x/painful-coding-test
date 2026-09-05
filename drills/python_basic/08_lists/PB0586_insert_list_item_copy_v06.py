"""
PB0586 — 지정 위치에 원소 삽입하기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
Python list.insert와 같은 인덱스 규칙으로 values의 복사본에 value를 삽입해 반환한다.

연습 초점
---------
복사본의 insert 연산이 원본 길이에 영향을 주지 않도록 한다.

구현할 함수
-----------
def insert_list_item(values: list[int], index: int, value: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 3]), insert_list_item(items, 1, 2) == [1, 2, 3] and items == [1, 3])[-1] is True
- insert_list_item([2, 3], 0, 1) == [1, 2, 3]
- insert_list_item([1], 99, 2) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0586 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def insert_list_item(values: list[int], index: int, value: int) -> list[int]:
    raise NotImplementedError("TODO: PB0586")


def self_test() -> None:
    assert ((items := [1, 3]), insert_list_item(items, 1, 2) == [1, 2, 3] and items == [1, 3])[-1] is True
    assert insert_list_item([2, 3], 0, 1) == [1, 2, 3]
    assert insert_list_item([1], 99, 2) == [1, 2]
