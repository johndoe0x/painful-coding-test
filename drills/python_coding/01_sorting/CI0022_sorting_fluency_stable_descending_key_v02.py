"""
CI0022 — 점수 내림차순과 동률 순서

Chapter: Sorting
Seed: 02 / 40
Variant: 02 / 20
Time cap: 150 seconds
Source checks: sorted_call

문제
----
sorted의 key와 reverse로 (이름, 점수)를 점수 내림차순 정렬하세요. 동률은 입력 순서이며 원본은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
reverse=True의 안정성

구현할 함수
-----------
def sorting_fluency_stable_descending_key(records: list[tuple[str, int]]) -> list[tuple[str, int]]:

필수 구현 방식
--------------
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_fluency_stable_descending_key([('b', 2), ('a', 2), ('z', 3)]) == [('z', 3), ('b', 2), ('a', 2)]
- sorting_fluency_stable_descending_key([]) == []
- ((_practice_1_0 := [('b', -1), ('a', -1), ('c', 0)]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_stable_descending_key(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [('c', 0), ('b', -1), ('a', -1)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0022 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_fluency_stable_descending_key(records: list[tuple[str, int]]) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: CI0022")


def self_test() -> None:
    assert sorting_fluency_stable_descending_key([('b', 2), ('a', 2), ('z', 3)]) == [('z', 3), ('b', 2), ('a', 2)]
    assert sorting_fluency_stable_descending_key([]) == []
    assert ((_practice_1_0 := [('b', -1), ('a', -1), ('c', 0)]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_stable_descending_key(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [('c', 0), ('b', -1), ('a', -1)]
