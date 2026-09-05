"""
CI0045 — itemgetter 필드 정렬 — 반복 세트 3

Chapter: Sorting
Seed: 03 / 40
Variant: 05 / 20
Time cap: 240 seconds
Source checks: sorted_call, itemgetter_call

문제
----
operator.itemgetter를 key로 사용해 딕셔너리 레코드를 field 값 오름차순으로 정렬하세요. 이 파일은 Sorting 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
operator.itemgetter와 레코드 정렬

구현할 함수
-----------
def sorting_r03_itemgetter_field(records: list[dict[str, object]], field: str) -> list[dict[str, object]]:

필수 구현 방식
--------------
- sorted()를 사용한다.
- operator.itemgetter를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r03_itemgetter_field([{'n': 'b', 's': 2}, {'n': 'a', 's': 1}], 's') == [{'n': 'a', 's': 1}, {'n': 'b', 's': 2}]
- sorting_r03_itemgetter_field([], 'x') == []
- sorting_r03_itemgetter_field([{'x': 2}, {'x': -1}, {'x': 2}], 'x') == [{'x': -1}, {'x': 2}, {'x': 2}]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0045 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r03_itemgetter_field(records: list[dict[str, object]], field: str) -> list[dict[str, object]]:
    raise NotImplementedError("TODO: CI0045")


def self_test() -> None:
    assert sorting_r03_itemgetter_field([{'n': 'b', 's': 2}, {'n': 'a', 's': 1}], 's') == [{'n': 'a', 's': 1}, {'n': 'b', 's': 2}]
    assert sorting_r03_itemgetter_field([], 'x') == []
    assert sorting_r03_itemgetter_field([{'x': 2}, {'x': -1}, {'x': 2}], 'x') == [{'x': -1}, {'x': 2}, {'x': 2}]
