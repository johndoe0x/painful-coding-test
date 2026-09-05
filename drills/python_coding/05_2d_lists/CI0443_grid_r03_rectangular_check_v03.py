"""
CI0443 — 직사각형 판정 — 반복 세트 3

Chapter: 2-D Lists
Seed: 23 / 40
Variant: 03 / 20
Time cap: 240 seconds
Source checks:

문제
----
모든 행 길이가 같으면 True를 반환하세요. 빈 행렬도 직사각형으로 봅니다. 이 파일은 2-D Lists 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
jagged row 검증

구현할 함수
-----------
def grid_r03_rectangular_check(matrix: list[list[object]]) -> bool:

예시 및 필수 테스트
-------------------
- grid_r03_rectangular_check([[1, 2], [3, 4]]) is True
- grid_r03_rectangular_check([[1], [2, 3]]) is False
- grid_r03_rectangular_check([]) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0443 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_r03_rectangular_check(matrix: list[list[object]]) -> bool:
    raise NotImplementedError("TODO: CI0443")


def self_test() -> None:
    assert grid_r03_rectangular_check([[1, 2], [3, 4]]) is True
    assert grid_r03_rectangular_check([[1], [2, 3]]) is False
    assert grid_r03_rectangular_check([]) is True
