"""
CI0510 — Counter 다중집합 교집합 — 반복 세트 3

Chapter: Hashmaps and Hashsets
Seed: 26 / 40
Variant: 10 / 20
Time cap: 240 seconds
Source checks: counter_call, sorted_call

문제
----
Counter 교집합으로 공통 원소를 작은 값부터 중복 횟수만큼 반환하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
Counter multiset 연산

구현할 함수
-----------
def hashing_r03_multiset_intersection(left: list[int], right: list[int]) -> list[int]:

필수 구현 방식
--------------
- collections.Counter를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_r03_multiset_intersection([1, 2, 2, 3], [2, 2, 4]) == [2, 2]
- hashing_r03_multiset_intersection([], [1]) == []
- hashing_r03_multiset_intersection([1, 1], [1]) == [1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0510 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r03_multiset_intersection(left: list[int], right: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0510")


def self_test() -> None:
    assert hashing_r03_multiset_intersection([1, 2, 2, 3], [2, 2, 4]) == [2, 2]
    assert hashing_r03_multiset_intersection([], [1]) == []
    assert hashing_r03_multiset_intersection([1, 1], [1]) == [1]
