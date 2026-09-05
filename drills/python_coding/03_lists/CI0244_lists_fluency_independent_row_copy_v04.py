"""
CI0244 — 행별 복사로 공유 끊기

Chapter: Lists
Seed: 13 / 40
Variant: 04 / 20
Time cap: 150 seconds
Source checks: comprehension

문제
----
list comprehension에서 각 행을 copy해 바깥 리스트와 모든 행이 새 객체인 복사본을 만드세요. 입력에서 두 행이 같은 객체여도 결과 행은 각각 독립적이어야 합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
shallow copy 한 단계 더 적용

구현할 함수
-----------
def lists_fluency_independent_row_copy(rows: list[list[int]]) -> list[list[int]]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- lists_fluency_independent_row_copy([[1], [], [2]]) == [[1], [], [2]]
- lists_fluency_independent_row_copy([]) == []
- ((row := [1]), (v := [row, row]), (r := lists_fluency_independent_row_copy(v)), r[0] is not row and r[1] is not row and (r[0] is not r[1]) and (r == [[1], [1]]))[-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0244 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_independent_row_copy(rows: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0244")


def self_test() -> None:
    assert lists_fluency_independent_row_copy([[1], [], [2]]) == [[1], [], [2]]
    assert lists_fluency_independent_row_copy([]) == []
    assert ((row := [1]), (v := [row, row]), (r := lists_fluency_independent_row_copy(v)), r[0] is not row and r[1] is not row and (r[0] is not r[1]) and (r == [[1], [1]]))[-1]
