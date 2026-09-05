"""
PB0584 — 한 원소만 증가시키기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정해 복사본의 해당 원소에 amount를 더하고 values는 그대로 둔다.

연습 초점
---------
리스트 원소 읽기와 제자리 산술 할당을 복사본에 적용한다.

구현할 함수
-----------
def increment_list_item(values: list[int], index: int, amount: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [10, 20]), increment_list_item(items, 1, 5) == [10, 25] and items == [10, 20])[-1] is True
- increment_list_item([3], 0, -3) == [0]
- increment_list_item([1, 2, 3], -1, 10) == [1, 2, 13]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0584 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def increment_list_item(values: list[int], index: int, amount: int) -> list[int]:
    raise NotImplementedError("TODO: PB0584")


def self_test() -> None:
    assert ((items := [10, 20]), increment_list_item(items, 1, 5) == [10, 25] and items == [10, 20])[-1] is True
    assert increment_list_item([3], 0, -3) == [0]
    assert increment_list_item([1, 2, 3], -1, 10) == [1, 2, 13]
