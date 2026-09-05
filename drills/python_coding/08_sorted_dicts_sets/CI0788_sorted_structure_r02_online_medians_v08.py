"""
CI0788 — 정렬 리스트 실시간 중앙값 — 반복 세트 2

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 08 / 20
Time cap: 240 seconds
Source checks: bisect_call

문제
----
각 값을 insort로 정렬 상태에 넣고 prefix별 중앙값을 반환하세요. 이 파일은 Sorted Dicts and Sorted Sets 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
bisect 기반 online median

구현할 함수
-----------
def sorted_structure_r02_online_medians(values: list[int]) -> list[float]:

필수 구현 방식
--------------
- bisect API를 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_r02_online_medians([2, 1, 5]) == [2.0, 1.5, 2.0]
- sorted_structure_r02_online_medians([]) == []
- sorted_structure_r02_online_medians([1, 3]) == [1.0, 2.0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0788 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_r02_online_medians(values: list[int]) -> list[float]:
    raise NotImplementedError("TODO: CI0788")


def self_test() -> None:
    assert sorted_structure_r02_online_medians([2, 1, 5]) == [2.0, 1.5, 2.0]
    assert sorted_structure_r02_online_medians([]) == []
    assert sorted_structure_r02_online_medians([1, 3]) == [1.0, 2.0]
