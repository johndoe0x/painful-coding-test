"""
CI0414 — 나선 순회 — 반복 세트 1

Chapter: 2-D Lists
Seed: 21 / 40
Variant: 14 / 20
Time cap: 240 seconds
Source checks: while

문제
----
직사각형 matrix를 바깥쪽부터 시계 방향 나선 순서로 반환하세요. 이 파일은 2-D Lists 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
네 경계 수축

구현할 함수
-----------
def grid_r01_spiral_order(matrix: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- grid_r01_spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
- grid_r01_spiral_order([]) == []
- grid_r01_spiral_order([[1, 2]]) == [1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0414 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r01_spiral_order(matrix: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: CI0414")


def self_test() -> None:
    assert grid_r01_spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert grid_r01_spiral_order([]) == []
    assert grid_r01_spiral_order([[1, 2]]) == [1, 2]
