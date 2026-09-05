"""
CI0422 — 중첩 enumerate로 좌표 붙이기

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 02 / 20
Time cap: 150 seconds
Source checks: enumerate_call, nested_loop

문제
----
중첩 enumerate로 0이 아닌 셀의 (행, 열, 값)을 행 우선 순서로 반환하세요. 길이가 다른 행과 빈 행을 허용하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
행 번호와 열 번호를 따로 생성

구현할 함수
-----------
def grid_fluency_enumerate_cells(rows: list[list[int]]) -> list[tuple[int, int, int]]:

필수 구현 방식
--------------
- enumerate()를 사용한다.
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- grid_fluency_enumerate_cells([[0, 2], [], [3]]) == [(0, 1, 2), (2, 0, 3)]
- grid_fluency_enumerate_cells([]) == []
- ((_practice_1_0 := [[-1, 0, 4]]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_enumerate_cells(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [(0, 0, -1), (0, 2, 4)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0422 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_fluency_enumerate_cells(rows: list[list[int]]) -> list[tuple[int, int, int]]:
    raise NotImplementedError("TODO: CI0422")


def self_test() -> None:
    assert grid_fluency_enumerate_cells([[0, 2], [], [3]]) == [(0, 1, 2), (2, 0, 3)]
    assert grid_fluency_enumerate_cells([]) == []
    assert ((_practice_1_0 := [[-1, 0, 4]]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_enumerate_cells(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [(0, 0, -1), (0, 2, 4)]
