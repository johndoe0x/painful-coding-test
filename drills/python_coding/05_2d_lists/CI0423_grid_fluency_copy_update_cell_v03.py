"""
CI0423 — 셀 수정 전 행별 복사

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 03 / 20
Time cap: 180 seconds
Source checks: comprehension

문제
----
각 행을 copy한 새 격자를 만들고 유효한 row,col 한 칸만 value로 바꾸세요. rows는 비어 있지 않고 좌표는 0 이상입니다. 원래 격자는 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
바깥 리스트만 복사할 때의 alias 오류

구현할 함수
-----------
def grid_fluency_copy_update_cell(rows: list[list[int]], row: int, col: int, value: int) -> list[list[int]]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- grid_fluency_copy_update_cell([[1, 2], [3, 4]], 0, 1, 9) == [[1, 9], [3, 4]]
- grid_fluency_copy_update_cell([[1]], 0, 0, 0) == [[0]]
- ((_practice_1_0 := [[1], [], [2]]), (_practice_1_1 := 2), (_practice_1_2 := 0), (_practice_1_3 := 7), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_copy_update_cell(_practice_1_0, _practice_1_1, _practice_1_2, _practice_1_3)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [[1], [], [7]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0423 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_fluency_copy_update_cell(rows: list[list[int]], row: int, col: int, value: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0423")


def self_test() -> None:
    assert grid_fluency_copy_update_cell([[1, 2], [3, 4]], 0, 1, 9) == [[1, 9], [3, 4]]
    assert grid_fluency_copy_update_cell([[1]], 0, 0, 0) == [[0]]
    assert ((_practice_1_0 := [[1], [], [2]]), (_practice_1_1 := 2), (_practice_1_2 := 0), (_practice_1_3 := 7), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_copy_update_cell(_practice_1_0, _practice_1_1, _practice_1_2, _practice_1_3)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [[1], [], [7]]
