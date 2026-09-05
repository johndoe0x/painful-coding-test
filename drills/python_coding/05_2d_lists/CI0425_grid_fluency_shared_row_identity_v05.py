"""
CI0425 — 같은 내용과 같은 행 객체

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 05 / 20
Time cap: 180 seconds
Source checks: nested_loop

문제
----
i<j이며 rows[i] is rows[j]인 모든 (i,j)를 인덱스 사전순으로 반환하세요. 값만 같은 독립 행은 제외합니다. 행은 최대 20개이고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
==와 is를 중첩 리스트에서 구분

구현할 함수
-----------
def grid_fluency_shared_row_identity(rows: list[list[int]]) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.

예시 및 필수 테스트
-------------------
- grid_fluency_shared_row_identity([[1], [1]]) == []
- grid_fluency_shared_row_identity([]) == []
- ((r := [1]), ((_practice_1_0 := [r, [], r, r]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_shared_row_identity(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1])[1] == [(0, 2), (0, 3), (2, 3)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0425 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_fluency_shared_row_identity(rows: list[list[int]]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: CI0425")


def self_test() -> None:
    assert grid_fluency_shared_row_identity([[1], [1]]) == []
    assert grid_fluency_shared_row_identity([]) == []
    assert ((r := [1]), ((_practice_1_0 := [r, [], r, r]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := grid_fluency_shared_row_identity(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1])[1] == [(0, 2), (0, 3), (2, 3)]
