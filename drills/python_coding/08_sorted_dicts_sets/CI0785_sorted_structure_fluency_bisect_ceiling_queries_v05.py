"""
CI0785 — bisect_left로 이상 값 조회

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 05 / 20
Time cap: 180 seconds
Source checks: bisect_call

문제
----
values는 오름차순입니다. 각 query에 bisect_left를 적용해 query 이상인 첫 값을 반환하고 없으면 None을 넣으세요. 질의 순서와 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
삽입 위치와 len 경계

구현할 함수
-----------
def sorted_structure_fluency_bisect_ceiling_queries(values: list[int], queries: list[int]) -> list[int | None]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_fluency_bisect_ceiling_queries([1, 3, 3, 7], [0, 3, 4, 8]) == [1, 3, 7, None]
- sorted_structure_fluency_bisect_ceiling_queries([], [1]) == [None]
- ((_practice_1_0 := [0]), (_practice_1_1 := [0, -1]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := sorted_structure_fluency_bisect_ceiling_queries(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [0, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0785 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_fluency_bisect_ceiling_queries(values: list[int], queries: list[int]) -> list[int | None]:
    raise NotImplementedError("TODO: CI0785")


def self_test() -> None:
    assert sorted_structure_fluency_bisect_ceiling_queries([1, 3, 3, 7], [0, 3, 4, 8]) == [1, 3, 7, None]
    assert sorted_structure_fluency_bisect_ceiling_queries([], [1]) == [None]
    assert ((_practice_1_0 := [0]), (_practice_1_1 := [0, -1]), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := sorted_structure_fluency_bisect_ceiling_queries(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [0, 0]
