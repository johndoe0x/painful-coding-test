"""
CI0124 — 별표 unpacking으로 가운데 분리

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 04 / 20
Time cap: 150 seconds
Source checks: tuple_unpack

문제
----
길이 2 이상인 values를 first, *middle, last로 unpack해 tuple로 반환하세요. middle은 새 리스트이고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
가변 길이 unpacking과 빈 가운데

구현할 함수
-----------
def pythonic_fluency_starred_unpack(values: list[int]) -> tuple[int, list[int], int]:

필수 구현 방식
--------------
- 대입이나 for 문에서 tuple unpacking을 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_fluency_starred_unpack([1, 2, 3, 4]) == (1, [2, 3], 4)
- pythonic_fluency_starred_unpack([5, 6]) == (5, [], 6)
- ((_practice_1_0 := [0, -1, 0]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := pythonic_fluency_starred_unpack(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (0, [-1], 0)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0124 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_fluency_starred_unpack(values: list[int]) -> tuple[int, list[int], int]:
    raise NotImplementedError("TODO: CI0124")


def self_test() -> None:
    assert pythonic_fluency_starred_unpack([1, 2, 3, 4]) == (1, [2, 3], 4)
    assert pythonic_fluency_starred_unpack([5, 6]) == (5, [], 6)
    assert ((_practice_1_0 := [0, -1, 0]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := pythonic_fluency_starred_unpack(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == (0, [-1], 0)
