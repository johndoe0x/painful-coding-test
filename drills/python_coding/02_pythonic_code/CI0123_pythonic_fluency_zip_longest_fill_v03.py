"""
CI0123 — 길이가 다른 열의 zip_longest

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 03 / 20
Time cap: 150 seconds
Source checks: itertools_call

문제
----
itertools.zip_longest(fillvalue=fill)로 두 열을 긴 쪽 길이까지 묶으세요. 부족한 쪽만 fill을 사용하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
zip과 zip_longest의 길이 계약

구현할 함수
-----------
def pythonic_fluency_zip_longest_fill(left: list[int], right: list[int], fill: int) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- itertools API를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_fluency_zip_longest_fill([1, 2], [9], 0) == [(1, 9), (2, 0)]
- pythonic_fluency_zip_longest_fill([], [], -1) == []
- ((_practice_1_0 := []), (_practice_1_1 := [0, 2]), (_practice_1_2 := (-1)), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := pythonic_fluency_zip_longest_fill(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [(-1, 0), (-1, 2)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0123 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_fluency_zip_longest_fill(left: list[int], right: list[int], fill: int) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: CI0123")


def self_test() -> None:
    assert pythonic_fluency_zip_longest_fill([1, 2], [9], 0) == [(1, 9), (2, 0)]
    assert pythonic_fluency_zip_longest_fill([], [], -1) == []
    assert ((_practice_1_0 := []), (_practice_1_1 := [0, 2]), (_practice_1_2 := (-1)), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := pythonic_fluency_zip_longest_fill(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [(-1, 0), (-1, 2)]
