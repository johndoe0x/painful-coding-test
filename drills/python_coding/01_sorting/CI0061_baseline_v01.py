"""
CI0061 — Sort Lambda — 기본 계약

Chapter: Sorting
Seed: 04 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks: sorted_call, lambda

문제
----
사람을 나이 오름차순, 이름 오름차순으로 lambda key를 사용해 정렬한다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def sort_people(people: list[tuple[str, int]]) -> list[tuple[str, int]]:

필수 구현 방식
--------------
- sorted()를 사용한다.
- lambda 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- sort_people([]) == []
- sort_people([('B', 20), ('A', 20), ('C', 18)]) == [('C', 18), ('A', 20), ('B', 20)]
- sort_people([('Z', 1)]) == [('Z', 1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0061 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sort_people(people: list[tuple[str, int]]) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: CI0061")


def self_test() -> None:
    assert sort_people([]) == []
    assert sort_people([('B', 20), ('A', 20), ('C', 18)]) == [('C', 18), ('A', 20), ('B', 20)]
    assert sort_people([('Z', 1)]) == [('Z', 1)]
