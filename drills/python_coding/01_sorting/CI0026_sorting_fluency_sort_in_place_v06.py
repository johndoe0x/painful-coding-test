"""
CI0026 — list.sort의 변경과 반환값

Chapter: Sorting
Seed: 02 / 40
Variant: 06 / 20
Time cap: 150 seconds
Source checks: list_sort_call

문제
----
values 자체를 list.sort(reverse=True)로 내림차순 정렬하고 None을 반환하세요. 새 리스트를 반환하면 안 됩니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
원본 객체 변경과 None 반환

구현할 함수
-----------
def sorting_fluency_sort_in_place(values: list[int]) -> None:

필수 구현 방식
--------------
- list.sort()를 사용한다.

예시 및 필수 테스트
-------------------
- ((v := [2, 1, 3]), sorting_fluency_sort_in_place(v), v) == ([3, 2, 1], None, [3, 2, 1])
- ((v := []), sorting_fluency_sort_in_place(v), v) == ([], None, [])
- ((v := [-1, 0, -1]), sorting_fluency_sort_in_place(v), v) == ([0, -1, -1], None, [0, -1, -1])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0026 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_fluency_sort_in_place(values: list[int]) -> None:
    raise NotImplementedError("TODO: CI0026")


def self_test() -> None:
    assert ((v := [2, 1, 3]), sorting_fluency_sort_in_place(v), v) == ([3, 2, 1], None, [3, 2, 1])
    assert ((v := []), sorting_fluency_sort_in_place(v), v) == ([], None, [])
    assert ((v := [-1, 0, -1]), sorting_fluency_sort_in_place(v), v) == ([0, -1, -1], None, [0, -1, -1])
