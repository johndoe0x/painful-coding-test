"""
CI0020 — 분수 comparator 정렬 — 반복 세트 1

Chapter: Sorting
Seed: 01 / 40
Variant: 20 / 20
Time cap: 300 seconds
Source checks: cmp_to_key_call, sorted_call

문제
----
functools.cmp_to_key와 교차 곱 comparator로 양의 분모를 가진 분수를 값 오름차순 정렬하세요. 이 파일은 Sorting 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
부동소수점 변환 없는 comparator

구현할 함수
-----------
def sorting_r01_fraction_cmp(fractions: list[tuple[int, int]]) -> list[tuple[int, int]]:

필수 구현 방식
--------------
- functools.cmp_to_key를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r01_fraction_cmp([(1, 2), (1, 3), (3, 4)]) == [(1, 3), (1, 2), (3, 4)]
- sorting_r01_fraction_cmp([]) == []
- sorting_r01_fraction_cmp([(2, 4), (1, 2)]) == [(2, 4), (1, 2)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0020 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r01_fraction_cmp(fractions: list[tuple[int, int]]) -> list[tuple[int, int]]:
    raise NotImplementedError("TODO: CI0020")


def self_test() -> None:
    assert sorting_r01_fraction_cmp([(1, 2), (1, 3), (3, 4)]) == [(1, 3), (1, 2), (3, 4)]
    assert sorting_r01_fraction_cmp([]) == []
    assert sorting_r01_fraction_cmp([(2, 4), (1, 2)]) == [(2, 4), (1, 2)]
