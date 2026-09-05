"""
PB0650 — 슬라이스를 다른 값들로 바꾸기

Chapter: Lists
Topic: List Slicing
Seed: 65 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
0 <= start <= stop <= len(values)라고 가정해 해당 구간 대신 replacement가 들어간 새 리스트를 반환한다.

연습 초점
---------
앞 슬라이스, replacement, 뒤 슬라이스를 결합해 길이 변화도 처리한다.

구현할 함수
-----------
def splice_list(values: list[int], start: int, stop: int, replacement: list[int]) -> list[int]:

예시 및 필수 테스트
-------------------
- splice_list([1, 2, 3, 4], 1, 3, [8, 9]) == [1, 8, 9, 4]
- splice_list([1, 2], 1, 1, [7]) == [1, 7, 2]
- splice_list([1, 2, 3], 0, 3, []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0650 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def splice_list(values: list[int], start: int, stop: int, replacement: list[int]) -> list[int]:
    raise NotImplementedError("TODO: PB0650")


def self_test() -> None:
    assert splice_list([1, 2, 3, 4], 1, 3, [8, 9]) == [1, 8, 9, 4]
    assert splice_list([1, 2], 1, 1, [7]) == [1, 7, 2]
    assert splice_list([1, 2, 3], 0, 3, []) == []
