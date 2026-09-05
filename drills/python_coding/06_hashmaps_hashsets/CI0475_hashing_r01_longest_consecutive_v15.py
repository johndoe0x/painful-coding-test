"""
CI0475 — 최장 연속 수열 — 반복 세트 1

Chapter: Hashmaps and Hashsets
Seed: 24 / 40
Variant: 15 / 20
Time cap: 240 seconds
Source checks:

문제
----
set을 사용해 정렬 없이 연속한 정수의 가장 긴 길이를 O(n)에 반환하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
수열 시작점만 확장

구현할 함수
-----------
def hashing_r01_longest_consecutive(values: list[int]) -> int:

예시 및 필수 테스트
-------------------
- hashing_r01_longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
- hashing_r01_longest_consecutive([]) == 0
- hashing_r01_longest_consecutive([1, 1, 2]) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0475 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r01_longest_consecutive(values: list[int]) -> int:
    raise NotImplementedError("TODO: CI0475")


def self_test() -> None:
    assert hashing_r01_longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert hashing_r01_longest_consecutive([]) == 0
    assert hashing_r01_longest_consecutive([1, 1, 2]) == 2
