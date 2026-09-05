"""
CI0424 — zip 별표 인자로 전치

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 04 / 20
Time cap: 150 seconds
Source checks: zip_call

문제
----
직사각형 rows를 zip(*rows)로 전치하고 각 열 tuple을 리스트로 바꾸세요. 빈 격자나 빈 열이면 []이고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
함수 호출의 별표 unpacking

구현할 함수
-----------
def grid_fluency_zip_transpose_rows(rows: list[list[int]]) -> list[list[int]]:

필수 구현 방식
--------------
- zip()을 사용한다.

예시 및 필수 테스트
-------------------
- grid_fluency_zip_transpose_rows([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
- grid_fluency_zip_transpose_rows([]) == [] and grid_fluency_zip_transpose_rows([[]]) == []
- ((_practice_1_0 := [[1], [2]]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_zip_transpose_rows(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [[1, 2]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0424 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_fluency_zip_transpose_rows(rows: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0424")


def self_test() -> None:
    assert grid_fluency_zip_transpose_rows([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert grid_fluency_zip_transpose_rows([]) == [] and grid_fluency_zip_transpose_rows([[]]) == []
    assert ((_practice_1_0 := [[1], [2]]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_zip_transpose_rows(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [[1, 2]]
