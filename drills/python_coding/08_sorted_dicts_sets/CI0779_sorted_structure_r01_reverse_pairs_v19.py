"""
CI0779 — 중요 역순 쌍 — 반복 세트 1

Chapter: Sorted Dicts and Sorted Sets
Seed: 39 / 40
Variant: 19 / 20
Time cap: 300 seconds
Source checks: bisect_call

문제
----
i < j이고 values[i] > 2*values[j]인 쌍의 수를 정렬된 오른쪽 값과 bisect로 세세요. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
ordered threshold counting

구현할 함수
-----------
def sorted_structure_r01_reverse_pairs(values: list[int]) -> int:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r01_reverse_pairs([1, 3, 2, 3, 1]) == 2
- sorted_structure_r01_reverse_pairs([]) == 0
- sorted_structure_r01_reverse_pairs([2, 4, 3, 5, 1]) == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0779 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r01_reverse_pairs(values: list[int]) -> int:
    raise NotImplementedError("TODO: CI0779")


def self_test() -> None:
    assert sorted_structure_r01_reverse_pairs([1, 3, 2, 3, 1]) == 2
    assert sorted_structure_r01_reverse_pairs([]) == 0
    assert sorted_structure_r01_reverse_pairs([2, 4, 3, 5, 1]) == 3
