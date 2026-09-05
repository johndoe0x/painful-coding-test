"""
CI0260 — 두 구간 목록 교집합 — 반복 세트 2

Chapter: Lists
Seed: 13 / 40
Variant: 20 / 20
Time cap: 240 seconds
Source checks: while

문제
----
각 목록이 서로 겹치지 않는 정렬된 닫힌 구간일 때 두 포인터로 교집합을 반환하세요. 이 파일은 Lists 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
구간 두 포인터

구현할 함수
-----------
def lists_r02_interval_intersections(left: list[tuple[int, int]], right: list[tuple[int, int]]) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- lists_r02_interval_intersections([(0, 2), (5, 10)], [(1, 5), (8, 12)]) == [(1, 2), (5, 5), (8, 10)]
- lists_r02_interval_intersections([], [(1, 2)]) == []
- lists_r02_interval_intersections([(1, 2)], [(3, 4)]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0260 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r02_interval_intersections(left: list[tuple[int, int]], right: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: CI0260")


def self_test() -> None:
    assert lists_r02_interval_intersections([(0, 2), (5, 10)], [(1, 5), (8, 12)]) == [(1, 2), (5, 5), (8, 10)]
    assert lists_r02_interval_intersections([], [(1, 2)]) == []
    assert lists_r02_interval_intersections([(1, 2)], [(3, 4)]) == []
