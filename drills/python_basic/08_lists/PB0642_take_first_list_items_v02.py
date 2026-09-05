"""
PB0642 — 앞에서 n개 복사하기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
count가 0 이상이라고 가정해 앞 count개 원소의 새 리스트를 반환한다.

연습 초점
---------
범위를 넘는 끝 인덱스도 안전한 리스트 슬라이싱을 사용한다.

구현할 함수
-----------
def first_list_items(values: list[int], count: int) -> list[int]:

예시 및 필수 테스트
-------------------
- first_list_items([1, 2, 3], 2) == [1, 2]
- first_list_items([1, 2], 5) == [1, 2]
- first_list_items([1], 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0642 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def first_list_items(values: list[int], count: int) -> list[int]:
    raise NotImplementedError("TODO: PB0642")


def self_test() -> None:
    assert first_list_items([1, 2, 3], 2) == [1, 2]
    assert first_list_items([1, 2], 5) == [1, 2]
    assert first_list_items([1], 0) == []
