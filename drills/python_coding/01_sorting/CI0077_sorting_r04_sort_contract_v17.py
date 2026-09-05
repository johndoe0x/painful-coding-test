"""
CI0077 — sort 반환 계약 — 반복 세트 4

Chapter: Sorting
Seed: 04 / 40
Variant: 17 / 20
Time cap: 240 seconds
Source checks: list_sort_call

문제
----
입력의 사본에 list.sort()를 호출하고 {'values': 정렬된 사본, 'returned_none': 반환값이 None인지}를 반환하세요. 이 파일은 Sorting 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
in-place sort의 반환값

구현할 함수
-----------
def sorting_r04_sort_contract(values: list[int]) -> dict[str, object]:

필수 구현 방식
--------------
- list.sort()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r04_sort_contract([3, 1]) == {'values': [1, 3], 'returned_none': True}
- sorting_r04_sort_contract([]) == {'values': [], 'returned_none': True}
- ((data := [2, 1]), sorting_r04_sort_contract(data), data) == ([2, 1], {'values': [1, 2], 'returned_none': True}, [2, 1])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0077 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r04_sort_contract(values: list[int]) -> dict[str, object]:
    raise NotImplementedError("TODO: CI0077")


def self_test() -> None:
    assert sorting_r04_sort_contract([3, 1]) == {'values': [1, 3], 'returned_none': True}
    assert sorting_r04_sort_contract([]) == {'values': [], 'returned_none': True}
    assert ((data := [2, 1]), sorting_r04_sort_contract(data), data) == ([2, 1], {'values': [1, 2], 'returned_none': True}, [2, 1])
