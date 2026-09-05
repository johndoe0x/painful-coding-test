"""
CI0787 — 작은·같은·큰 값 슬라이스

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 07 / 20
Time cap: 180 seconds
Source checks: bisect_call, slice

문제
----
오름차순 values에서 bisect_left/right와 슬라이스로 (target 미만, 같은 값, 초과) 세 새 리스트를 반환하세요. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
경계 인덱스를 출력 구간으로 변환

구현할 함수
-----------
def sorted_structure_fluency_bisect_three_slices(values: list[int], target: int) -> tuple[list[int], list[int], list[int]]:

필수 구현 방식
--------------
- bisect API를 사용한다.
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_fluency_bisect_three_slices([1, 2, 2, 4], 2) == ([1], [2, 2], [4])
- sorted_structure_fluency_bisect_three_slices([], 1) == ([], [], [])
- ((_practice_1_0 := [1, 3]), (_practice_1_1 := 2), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_three_slices(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ([1], [], [3])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0787 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_fluency_bisect_three_slices(values: list[int], target: int) -> tuple[list[int], list[int], list[int]]:
    raise NotImplementedError("TODO: CI0787")


def self_test() -> None:
    assert sorted_structure_fluency_bisect_three_slices([1, 2, 2, 4], 2) == ([1], [2, 2], [4])
    assert sorted_structure_fluency_bisect_three_slices([], 1) == ([], [], [])
    assert ((_practice_1_0 := [1, 3]), (_practice_1_1 := 2), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_three_slices(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ([1], [], [3])
