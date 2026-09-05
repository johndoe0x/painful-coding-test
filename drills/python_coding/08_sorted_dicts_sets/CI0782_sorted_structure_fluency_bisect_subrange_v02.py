"""
CI0782 — bisect의 lo·hi 경계

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 02 / 20
Time cap: 180 seconds
Source checks: bisect_call

문제
----
values는 오름차순이며 0<=low<=high<=len(values)입니다. bisect_left/right의 lo=low, hi=high를 사용한 두 삽입 인덱스를 반환하세요. 결과는 원본 기준 절대 인덱스입니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
반열린 검색 구간과 절대 인덱스

구현할 함수
-----------
def sorted_structure_fluency_bisect_subrange(values: list[int], target: int, low: int, high: int) -> tuple[int, int]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_fluency_bisect_subrange([1, 2, 2, 2, 5], 2, 2, 4) == (2, 4)
- sorted_structure_fluency_bisect_subrange([], 0, 0, 0) == (0, 0)
- ((_practice_1_0 := [1, 3, 5]), (_practice_1_1 := 0), (_practice_1_2 := 1), (_practice_1_3 := 3), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_subrange(_practice_1_0, _practice_1_1, _practice_1_2, _practice_1_3)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (1, 1)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0782 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_fluency_bisect_subrange(values: list[int], target: int, low: int, high: int) -> tuple[int, int]:
    raise NotImplementedError("TODO: CI0782")


def self_test() -> None:
    assert sorted_structure_fluency_bisect_subrange([1, 2, 2, 2, 5], 2, 2, 4) == (2, 4)
    assert sorted_structure_fluency_bisect_subrange([], 0, 0, 0) == (0, 0)
    assert ((_practice_1_0 := [1, 3, 5]), (_practice_1_1 := 0), (_practice_1_2 := 1), (_practice_1_3 := 3), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_subrange(_practice_1_0, _practice_1_1, _practice_1_2, _practice_1_3)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (1, 1)
