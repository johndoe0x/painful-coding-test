"""
PB0585 — 지정 위치를 제외한 복사본

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정해 values는 바꾸지 않고 해당 위치를 삭제한 새 리스트를 반환한다.

연습 초점
---------
복사본에 del을 적용하거나 양쪽 슬라이스를 결합한다.

구현할 함수
-----------
def delete_list_item(values: list[int], index: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), delete_list_item(items, 1) == [1, 3] and items == [1, 2, 3])[-1] is True
- delete_list_item([5], 0) == []
- delete_list_item([1, 2, 3], -1) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0585 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def delete_list_item(values: list[int], index: int) -> list[int]:
    raise NotImplementedError("TODO: PB0585")


def self_test() -> None:
    assert ((items := [1, 2, 3]), delete_list_item(items, 1) == [1, 3] and items == [1, 2, 3])[-1] is True
    assert delete_list_item([5], 0) == []
    assert delete_list_item([1, 2, 3], -1) == [1, 2]
