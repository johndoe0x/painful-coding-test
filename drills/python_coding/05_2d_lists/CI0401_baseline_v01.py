"""
CI0401 — Multi-Dimensional List — 기본 계약

Chapter: 2-D Lists
Seed: 21 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks:

문제
----
직사각형 행렬의 행과 열 수를 반환하고 빈 행렬은 (0,0)으로 처리한다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def matrix_shape(matrix: list[list[object]]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- matrix_shape([]) == (0, 0)
- matrix_shape([[]]) == (1, 0)
- matrix_shape([[1, 2], [3, 4]]) == (2, 2)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0401 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def matrix_shape(matrix: list[list[object]]) -> tuple[int, int]:
    raise NotImplementedError("TODO: CI0401")


def self_test() -> None:
    assert matrix_shape([]) == (0, 0)
    assert matrix_shape([[]]) == (1, 0)
    assert matrix_shape([[1, 2], [3, 4]]) == (2, 2)
