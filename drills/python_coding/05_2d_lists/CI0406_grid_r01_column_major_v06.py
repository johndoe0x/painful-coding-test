"""
CI0406 — 열 우선 순회 — 반복 세트 1

Chapter: 2-D Lists
Seed: 21 / 40
Variant: 06 / 20
Time cap: 240 seconds
Source checks: nested_loop

문제
----
직사각형 matrix를 열별로 위에서 아래로 읽어 반환하세요. 이 파일은 2-D Lists 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
열 index 바깥 loop

구현할 함수
-----------
def grid_r01_column_major(matrix: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- grid_r01_column_major([[1, 2], [3, 4]]) == [1, 3, 2, 4]
- grid_r01_column_major([]) == []
- grid_r01_column_major([[1, 2, 3]]) == [1, 2, 3]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0406 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r01_column_major(matrix: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: CI0406")


def self_test() -> None:
    assert grid_r01_column_major([[1, 2], [3, 4]]) == [1, 3, 2, 4]
    assert grid_r01_column_major([]) == []
    assert grid_r01_column_major([[1, 2, 3]]) == [1, 2, 3]
