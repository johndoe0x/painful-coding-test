"""
CI0325 — 독립적인 빈 행 초기화 — 반복 세트 6

Chapter: Lists
Seed: 17 / 40
Variant: 05 / 20
Time cap: 240 seconds
Source checks: comprehension

문제
----
서로 같은 객체를 공유하지 않는 빈 리스트 count개를 만드세요. 이 파일은 Lists 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
중첩 리스트 곱셈의 aliasing 회피

구현할 함수
-----------
def lists_r06_independent_rows(count: int) -> list[list[int]]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- ((rows := lists_r06_independent_rows(3)), rows == [[], [], []] and len({id(row) for row in rows}) == 3) == ([[], [], []], True)
- lists_r06_independent_rows(0) == []
- ((rows := lists_r06_independent_rows(1)), rows == [[]]) == ([[]], True)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0325 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r06_independent_rows(count: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0325")


def self_test() -> None:
    assert ((rows := lists_r06_independent_rows(3)), rows == [[], [], []] and len({id(row) for row in rows}) == 3) == ([[], [], []], True)
    assert lists_r06_independent_rows(0) == []
    assert ((rows := lists_r06_independent_rows(1)), rows == [[]]) == ([[]], True)
