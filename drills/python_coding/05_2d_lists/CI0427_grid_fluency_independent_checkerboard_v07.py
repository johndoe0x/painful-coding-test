"""
CI0427 — 중첩 comprehension 격자 생성

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 07 / 20
Time cap: 150 seconds
Source checks: comprehension

문제
----
0<=rows,cols<=20, first는 0 또는 1입니다. cell=(행+열+first)%2인 격자를 중첩 comprehension으로 반환하세요. 행 객체는 서로 독립적이어야 합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
행마다 새 리스트 생성

구현할 함수
-----------
def grid_fluency_independent_checkerboard(rows: int, cols: int, first: int) -> list[list[int]]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- grid_fluency_independent_checkerboard(2, 3, 0) == [[0, 1, 0], [1, 0, 1]]
- grid_fluency_independent_checkerboard(0, 3, 1) == [] and grid_fluency_independent_checkerboard(2, 0, 1) == [[], []]
- ((r := grid_fluency_independent_checkerboard(3, 1, 1)), r == [[1], [0], [1]] and r[0] is not r[2])[-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0427 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_fluency_independent_checkerboard(rows: int, cols: int, first: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0427")


def self_test() -> None:
    assert grid_fluency_independent_checkerboard(2, 3, 0) == [[0, 1, 0], [1, 0, 1]]
    assert grid_fluency_independent_checkerboard(0, 3, 1) == [] and grid_fluency_independent_checkerboard(2, 0, 1) == [[], []]
    assert ((r := grid_fluency_independent_checkerboard(3, 1, 1)), r == [[1], [0], [1]] and r[0] is not r[2])[-1]
