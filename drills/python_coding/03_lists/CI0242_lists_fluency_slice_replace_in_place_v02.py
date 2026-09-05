"""
CI0242 — 슬라이스 대입으로 길이 변경

Chapter: Lists
Seed: 13 / 40
Variant: 02 / 20
Time cap: 180 seconds
Source checks: slice

문제
----
values[start:stop] = replacement를 수행하고 None을 반환하세요. values 객체를 직접 바꾸고 replacement는 보존합니다. 음수와 범위 밖 경계는 Python 슬라이스 규칙을 따릅니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
슬라이스 조회와 대입

구현할 함수
-----------
def lists_fluency_slice_replace_in_place(values: list[int], start: int, stop: int, replacement: list[int]) -> None:

필수 구현 방식
--------------
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- ((v := [1, 2, 3]), lists_fluency_slice_replace_in_place(v, 1, 2, [8, 9]), v) == ([1, 8, 9, 3], None, [1, 8, 9, 3])
- ((v := []), lists_fluency_slice_replace_in_place(v, 0, 0, [1]), v) == ([1], None, [1])
- ((v := [1, 2, 3]), (r := [7]), lists_fluency_slice_replace_in_place(v, -2, 99, r), v, r)[2:] == (None, [1, 7], [7])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0242 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_slice_replace_in_place(values: list[int], start: int, stop: int, replacement: list[int]) -> None:
    raise NotImplementedError("TODO: CI0242")


def self_test() -> None:
    assert ((v := [1, 2, 3]), lists_fluency_slice_replace_in_place(v, 1, 2, [8, 9]), v) == ([1, 8, 9, 3], None, [1, 8, 9, 3])
    assert ((v := []), lists_fluency_slice_replace_in_place(v, 0, 0, [1]), v) == ([1], None, [1])
    assert ((v := [1, 2, 3]), (r := [7]), lists_fluency_slice_replace_in_place(v, -2, 99, r), v, r)[2:] == (None, [1, 7], [7])
