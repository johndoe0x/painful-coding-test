"""
CI0243 — 중첩 리스트의 얕은 복사

Chapter: Lists
Seed: 13 / 40
Variant: 03 / 20
Time cap: 150 seconds
Source checks:

문제
----
rows.copy()로 바깥 리스트만 새로 만들고 내부 행 객체는 공유하세요. 호출 중 입력을 변경하지 않습니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
값 동등성과 객체 정체성

구현할 함수
-----------
def lists_fluency_shallow_outer_copy(rows: list[list[int]]) -> list[list[int]]:

예시 및 필수 테스트
-------------------
- lists_fluency_shallow_outer_copy([[1], [2]]) == [[1], [2]]
- lists_fluency_shallow_outer_copy([]) == []
- ((v := [[1], [2]]), (r := lists_fluency_shallow_outer_copy(v)), r is not v and r[0] is v[0] and (r[1] is v[1]))[-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0243 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_shallow_outer_copy(rows: list[list[int]]) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0243")


def self_test() -> None:
    assert lists_fluency_shallow_outer_copy([[1], [2]]) == [[1], [2]]
    assert lists_fluency_shallow_outer_copy([]) == []
    assert ((v := [[1], [2]]), (r := lists_fluency_shallow_outer_copy(v)), r is not v and r[0] is v[0] and (r[1] is v[1]))[-1]
