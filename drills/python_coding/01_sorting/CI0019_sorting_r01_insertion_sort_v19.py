"""
CI0019 — 삽입 정렬 구현 — 반복 세트 1

Chapter: Sorting
Seed: 01 / 40
Variant: 19 / 20
Time cap: 240 seconds
Source checks: for

문제
----
원본을 보존하며 삽입 정렬로 오름차순 새 리스트를 만드세요. 이 파일은 Sorting 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
직접 구현하는 안정 정렬

구현할 함수
-----------
def sorting_r01_insertion_sort(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r01_insertion_sort([3, 1, 2]) == [1, 2, 3]
- sorting_r01_insertion_sort([]) == []
- sorting_r01_insertion_sort([2, 2, -1]) == [-1, 2, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0019 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r01_insertion_sort(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0019")


def self_test() -> None:
    assert sorting_r01_insertion_sort([3, 1, 2]) == [1, 2, 3]
    assert sorting_r01_insertion_sort([]) == []
    assert sorting_r01_insertion_sort([2, 2, -1]) == [-1, 2, 2]
