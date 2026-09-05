"""
CI0246 — step 슬라이스 대입의 길이

Chapter: Lists
Seed: 13 / 40
Variant: 06 / 20
Time cap: 180 seconds
Source checks: slice

문제
----
step>0입니다. replacement 길이가 values[::step] 길이와 다르면 None, 같으면 사본의 [::step]에 대입한 새 리스트를 반환하세요. 두 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
확장 슬라이스 대입은 길이를 바꾸지 않음

구현할 함수
-----------
def lists_fluency_extended_slice_assignment(values: list[int], step: int, replacement: list[int]) -> list[int] | None:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- lists_fluency_extended_slice_assignment([0, 1, 2, 3, 4], 2, [8, 9, 10]) == [8, 1, 9, 3, 10]
- lists_fluency_extended_slice_assignment([], 2, []) == []
- ((_practice_1_0 := [1, 2, 3]), (_practice_1_1 := 2), (_practice_1_2 := [9]), (_practice_1_before := repr((_practice_1_0, _practice_1_2))), (_practice_1_result := lists_fluency_extended_slice_assignment(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_2)) == _practice_1_before else object())[-1] is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0246 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_extended_slice_assignment(values: list[int], step: int, replacement: list[int]) -> list[int] | None:
    raise NotImplementedError("TODO: CI0246")


def self_test() -> None:
    assert lists_fluency_extended_slice_assignment([0, 1, 2, 3, 4], 2, [8, 9, 10]) == [8, 1, 9, 3, 10]
    assert lists_fluency_extended_slice_assignment([], 2, []) == []
    assert ((_practice_1_0 := [1, 2, 3]), (_practice_1_1 := 2), (_practice_1_2 := [9]), (_practice_1_before := repr((_practice_1_0, _practice_1_2))), (_practice_1_result := lists_fluency_extended_slice_assignment(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_2)) == _practice_1_before else object())[-1] is None
