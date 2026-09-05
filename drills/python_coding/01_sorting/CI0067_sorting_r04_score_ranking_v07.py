"""
CI0067 — 점수 순위 정렬 — 반복 세트 4

Chapter: Sorting
Seed: 04 / 40
Variant: 07 / 20
Time cap: 240 seconds
Source checks: sorted_call

문제
----
(이름, 점수)를 점수 내림차순, 동률이면 이름 오름차순으로 정렬하세요. 이 파일은 Sorting 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
내림차순 숫자와 오름차순 문자열의 복합 key

구현할 함수
-----------
def sorting_r04_score_ranking(records: list[tuple[str, int]]) -> list[tuple[str, int]]:

필수 구현 방식
--------------
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r04_score_ranking([('B', 90), ('A', 90), ('C', 80)]) == [('A', 90), ('B', 90), ('C', 80)]
- sorting_r04_score_ranking([]) == []
- sorting_r04_score_ranking([('x', -1), ('y', 0)]) == [('y', 0), ('x', -1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0067 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r04_score_ranking(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: CI0067")


def self_test() -> None:
    assert sorting_r04_score_ranking([('B', 90), ('A', 90), ('C', 80)]) == [('A', 90), ('B', 90), ('C', 80)]
    assert sorting_r04_score_ranking([]) == []
    assert sorting_r04_score_ranking([('x', -1), ('y', 0)]) == [('y', 0), ('x', -1)]
