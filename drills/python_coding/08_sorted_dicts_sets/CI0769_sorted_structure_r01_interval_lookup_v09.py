"""
CI0769 — 구간 포함 조회 — 반복 세트 1

Chapter: Sorted Dicts and Sorted Sets
Seed: 39 / 40
Variant: 09 / 20
Time cap: 240 seconds
Source checks: bisect_call

문제
----
겹치지 않고 시작점순인 닫힌 구간에서 각 point가 속한 label을 bisect로 찾고 없으면 None을 반환하세요. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
시작점 index와 끝점 확인

구현할 함수
-----------
def sorted_structure_r01_interval_lookup(intervals: list[tuple[int, int, str]], points: list[int]) -> list[str | None]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r01_interval_lookup([(0, 2, 'a'), (5, 7, 'b')], [1, 4, 7]) == ['a', None, 'b']
- sorted_structure_r01_interval_lookup([], [1]) == [None]
- sorted_structure_r01_interval_lookup([(1, 1, 'x')], [1]) == ['x']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0769 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r01_interval_lookup(intervals: list[tuple[int, int, str]], points: list[int]) -> list[str | None]:
    raise NotImplementedError("TODO: CI0769")


def self_test() -> None:
    assert sorted_structure_r01_interval_lookup([(0, 2, 'a'), (5, 7, 'b')], [1, 4, 7]) == ['a', None, 'b']
    assert sorted_structure_r01_interval_lookup([], [1]) == [None]
    assert sorted_structure_r01_interval_lookup([(1, 1, 'x')], [1]) == ['x']
