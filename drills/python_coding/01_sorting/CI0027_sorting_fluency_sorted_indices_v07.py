"""
CI0027 — 값 순서대로 원래 인덱스 정렬

Chapter: Sorting
Seed: 02 / 40
Variant: 07 / 20
Time cap: 180 seconds
Source checks: sorted_call, range

문제
----
sorted(range(len(values)), key=...)로 값 오름차순에 해당하는 원래 인덱스를 반환하세요. 동률이면 작은 인덱스가 먼저이며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
값을 key로 쓰는 인덱스 정렬

구현할 함수
-----------
def sorting_fluency_sorted_indices(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- sorted()를 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_fluency_sorted_indices([5, 2, 5, 1]) == [3, 1, 0, 2]
- sorting_fluency_sorted_indices([]) == []
- ((_practice_1_0 := [0, -1, -1]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_sorted_indices(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [1, 2, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0027 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_fluency_sorted_indices(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0027")


def self_test() -> None:
    assert sorting_fluency_sorted_indices([5, 2, 5, 1]) == [3, 1, 0, 2]
    assert sorting_fluency_sorted_indices([]) == []
    assert ((_practice_1_0 := [0, -1, -1]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_sorted_indices(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == [1, 2, 0]
