"""
CI0780 — floor·ceil 다중 조회 — 반복 세트 1

Chapter: Sorted Dicts and Sorted Sets
Seed: 39 / 40
Variant: 20 / 20
Time cap: 240 seconds
Source checks: bisect_call

문제
----
오름차순 values에서 각 query 이하 최댓값 floor와 이상 최솟값 ceil을 bisect로 반환하세요. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
lower bound 양옆 query

구현할 함수
-----------
def sorted_structure_r01_floor_ceil_queries(values: list[int], queries: list[int]) -> list[tuple[int | None, int | None]]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r01_floor_ceil_queries([1, 3, 5], [0, 3, 4, 6]) == [(None, 1), (3, 3), (3, 5), (5, None)]
- sorted_structure_r01_floor_ceil_queries([], [1]) == [(None, None)]
- sorted_structure_r01_floor_ceil_queries([2], []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0780 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r01_floor_ceil_queries(values: list[int], queries: list[int]) -> list[tuple[int | None, int | None]]:
    raise NotImplementedError("TODO: CI0780")


def self_test() -> None:
    assert sorted_structure_r01_floor_ceil_queries([1, 3, 5], [0, 3, 4, 6]) == [(None, 1), (3, 3), (3, 5), (5, None)]
    assert sorted_structure_r01_floor_ceil_queries([], [1]) == [(None, None)]
    assert sorted_structure_r01_floor_ceil_queries([2], []) == []
