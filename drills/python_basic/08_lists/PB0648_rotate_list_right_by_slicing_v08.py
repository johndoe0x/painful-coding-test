"""
PB0648 — 리스트 오른쪽 회전하기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
빈 리스트는 []를 반환하고, 아니면 amount를 길이로 나눈 나머지만큼 오른쪽으로 회전한 새 리스트를 반환한다.

연습 초점
---------
뒤쪽과 앞쪽 슬라이스의 결합 순서를 바꿔 회전한다.

구현할 함수
-----------
def rotate_list_right(values: list[int], amount: int) -> list[int]:

예시 및 필수 테스트
-------------------
- rotate_list_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
- rotate_list_right([1, 2, 3], 4) == [3, 1, 2]
- rotate_list_right([], 2) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0648 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def rotate_list_right(values: list[int], amount: int) -> list[int]:
    raise NotImplementedError("TODO: PB0648")


def self_test() -> None:
    assert rotate_list_right([1, 2, 3, 4], 1) == [4, 1, 2, 3]
    assert rotate_list_right([1, 2, 3], 4) == [3, 1, 2]
    assert rotate_list_right([], 2) == []
