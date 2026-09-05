"""
CI0793 — 시각별 이전 값 조회 — 반복 세트 2

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 13 / 20
Time cap: 240 seconds
Source checks: bisect_call

문제
----
입력 순서와 무관하게 key별 기록을 timestamp로 정렬하고 query 시각 이하의 가장 최근 값을 bisect로 반환하세요. 같은 key와 timestamp는 입력의 마지막 값을 사용하며 이전 기록이 없으면 None입니다. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
per-key sorted history와 동일 시각 갱신

구현할 함수
-----------
def sorted_structure_r02_time_map(records: list[tuple[str, int, str]], queries: list[tuple[str, int]]) -> list[str | None]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r02_time_map([('a', 1, 'x'), ('a', 3, 'y')], [('a', 2), ('a', 3), ('b', 1)]) == ['x', 'y', None]
- sorted_structure_r02_time_map([], []) == []
- sorted_structure_r02_time_map([('a', 3, 'late'), ('a', 2, 'z'), ('a', 2, 'a')], [('a', 1), ('a', 2), ('a', 3)]) == [None, 'a', 'late']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0793 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r02_time_map(records: list[tuple[str, int, str]], queries: list[tuple[str, int]]) -> list[str | None]:
    raise NotImplementedError("TODO: CI0793")


def self_test() -> None:
    assert sorted_structure_r02_time_map([('a', 1, 'x'), ('a', 3, 'y')], [('a', 2), ('a', 3), ('b', 1)]) == ['x', 'y', None]
    assert sorted_structure_r02_time_map([], []) == []
    assert sorted_structure_r02_time_map([('a', 3, 'late'), ('a', 2, 'z'), ('a', 2, 'a')], [('a', 1), ('a', 2), ('a', 3)]) == [None, 'a', 'late']
