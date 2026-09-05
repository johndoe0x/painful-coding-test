"""
CI0071 — 두 정렬열 병합 — 반복 세트 4

Chapter: Sorting
Seed: 04 / 40
Variant: 11 / 20
Time cap: 240 seconds
Source checks: while

문제
----
이미 오름차순인 두 리스트를 다시 전체 정렬하지 말고 두 포인터로 병합하세요. 이 파일은 Sorting 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
merge 단계와 선형 시간

구현할 함수
-----------
def sorting_r04_merge_sorted(left: list[int], right: list[int]) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r04_merge_sorted([1, 4], [2, 3]) == [1, 2, 3, 4]
- sorting_r04_merge_sorted([], [1]) == [1]
- sorting_r04_merge_sorted([-2, 2], [-1, 2]) == [-2, -1, 2, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0071 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r04_merge_sorted(left: list[int], right: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0071")


def self_test() -> None:
    assert sorting_r04_merge_sorted([1, 4], [2, 3]) == [1, 2, 3, 4]
    assert sorting_r04_merge_sorted([], [1]) == [1]
    assert sorting_r04_merge_sorted([-2, 2], [-1, 2]) == [-2, -1, 2, 2]
