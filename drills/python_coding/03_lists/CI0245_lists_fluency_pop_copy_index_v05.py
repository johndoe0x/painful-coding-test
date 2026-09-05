"""
CI0245 — 음수 인덱스로 복사본 pop

Chapter: Lists
Seed: 13 / 40
Variant: 05 / 20
Time cap: 180 seconds
Source checks: pop_call

문제
----
복사본에서 list.pop(index)한 값과 남은 복사본을 반환하세요. 유효 범위 -len<=index<len 밖이면 (None, 원본 사본)을 반환합니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
pop 반환값과 음수 인덱스 경계

구현할 함수
-----------
def lists_fluency_pop_copy_index(values: list[int], index: int) -> tuple[int | None, list[int]]:

필수 구현 방식
--------------
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- lists_fluency_pop_copy_index([1, 2, 3], -2) == (2, [1, 3])
- lists_fluency_pop_copy_index([], 0) == (None, [])
- ((_practice_1_0 := [5]), (_practice_1_1 := (-2)), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := lists_fluency_pop_copy_index(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (None, [5]) and ((_practice_2_0 := [5]), (_practice_2_1 := 0), (_practice_2_before := repr((_practice_2_0,))), (_practice_2_result := lists_fluency_pop_copy_index(_practice_2_0, _practice_2_1)), _practice_2_result if repr((_practice_2_0,)) == _practice_2_before else object())[-1] == (5, [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0245 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_pop_copy_index(values: list[int], index: int) -> tuple[int | None, list[int]]:
    raise NotImplementedError("TODO: CI0245")


def self_test() -> None:
    assert lists_fluency_pop_copy_index([1, 2, 3], -2) == (2, [1, 3])
    assert lists_fluency_pop_copy_index([], 0) == (None, [])
    assert ((_practice_1_0 := [5]), (_practice_1_1 := (-2)), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := lists_fluency_pop_copy_index(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (None, [5]) and ((_practice_2_0 := [5]), (_practice_2_1 := 0), (_practice_2_before := repr((_practice_2_0,))), (_practice_2_result := lists_fluency_pop_copy_index(_practice_2_0, _practice_2_1)), _practice_2_result if repr((_practice_2_0,)) == _practice_2_before else object())[-1] == (5, [])
