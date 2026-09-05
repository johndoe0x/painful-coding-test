"""
CI0283 — 삽입 후 음수 제거 — 반복 세트 4

Chapter: Lists
Seed: 15 / 40
Variant: 03 / 20
Time cap: 240 seconds
Source checks:

문제
----
사본의 index에 new_value를 삽입한 뒤 처음 등장하는 음수 하나만 제거하세요. 이 파일은 Lists 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
insert와 remove의 순서

구현할 함수
-----------
def lists_r04_insert_remove_negative(values: list[int], index: int, new_value: int) -> list[int]:

예시 및 필수 테스트
-------------------
- lists_r04_insert_remove_negative([1, -1, 3], 1, 2) == [1, 2, 3]
- lists_r04_insert_remove_negative([], 0, 5) == [5]
- lists_r04_insert_remove_negative([-1, -2], 0, 0) == [0, -2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0283 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r04_insert_remove_negative(values: list[int], index: int, new_value: int) -> list[int]:
    raise NotImplementedError("TODO: CI0283")


def self_test() -> None:
    assert lists_r04_insert_remove_negative([1, -1, 3], 1, 2) == [1, 2, 3]
    assert lists_r04_insert_remove_negative([], 0, 5) == [5]
    assert lists_r04_insert_remove_negative([-1, -2], 0, 0) == [0, -2]
