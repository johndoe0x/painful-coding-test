"""
PB0581 — 복사본의 한 위치 수정하기

Chapter: Lists
Topic: List Operations
Seed: 59 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하다고 가정하고 values는 변경하지 않은 채 복사본의 index 위치만 value로 바꾸어 반환한다.

연습 초점
---------
얕은 복사 뒤 인덱스 할당을 수행해 원본과 결과를 분리한다.

구현할 함수
-----------
def update_at(values: list[int], index: int, value: int) -> list[int]:

예시 및 필수 테스트
-------------------
- ((items := [1, 2, 3]), update_at(items, 1, 9) == [1, 9, 3] and items == [1, 2, 3])[-1] is True
- update_at([5], 0, -1) == [-1]
- update_at([1, 2], -1, 7) == [1, 7]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0581 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def update_at(values: list[int], index: int, value: int) -> list[int]:
    raise NotImplementedError("TODO: PB0581")


def self_test() -> None:
    assert ((items := [1, 2, 3]), update_at(items, 1, 9) == [1, 9, 3] and items == [1, 2, 3])[-1] is True
    assert update_at([5], 0, -1) == [-1]
    assert update_at([1, 2], -1, 7) == [1, 7]
