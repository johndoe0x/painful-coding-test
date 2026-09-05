"""
CI0025 — itemgetter로 두 필드 정렬

Chapter: Sorting
Seed: 02 / 40
Variant: 05 / 20
Time cap: 180 seconds
Source checks: sorted_call, itemgetter_call

문제
----
모든 행에 정수 team과 rank 키가 있습니다. operator.itemgetter('team', 'rank')를 sorted의 key로 사용해 두 필드 모두 오름차순 정렬하세요. 동률 순서와 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
다중 필드 itemgetter

구현할 함수
-----------
def sorting_fluency_itemgetter_two_fields(rows: list[dict[str, int]]) -> list[dict[str, int]]:

필수 구현 방식
--------------
- sorted()를 사용한다.
- operator.itemgetter를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_fluency_itemgetter_two_fields([{'team': 2, 'rank': 0}, {'team': 1, 'rank': 2}, {'team': 1, 'rank': 1}]) == [{'team': 1, 'rank': 1}, {'team': 1, 'rank': 2}, {'team': 2, 'rank': 0}]
- sorting_fluency_itemgetter_two_fields([]) == []
- ((_practice_1_0 := [{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_itemgetter_two_fields(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0025 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_fluency_itemgetter_two_fields(rows: list[dict[str, int]]) -> list[dict[str, int]]:
    raise NotImplementedError("TODO: CI0025")


def self_test() -> None:
    assert sorting_fluency_itemgetter_two_fields([{'team': 2, 'rank': 0}, {'team': 1, 'rank': 2}, {'team': 1, 'rank': 1}]) == [{'team': 1, 'rank': 1}, {'team': 1, 'rank': 2}, {'team': 2, 'rank': 0}]
    assert sorting_fluency_itemgetter_two_fields([]) == []
    assert ((_practice_1_0 := [{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_itemgetter_two_fields(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [{'team': 0, 'rank': 1, 'id': 2}, {'team': 0, 'rank': 1, 'id': 1}]
