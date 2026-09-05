"""
CI0512 — 두 레코드 hash join — 반복 세트 3

Chapter: Hashmaps and Hashsets
Seed: 26 / 40
Variant: 12 / 20
Time cap: 240 seconds
Source checks:

문제
----
right를 key로 index하되 중복 key는 마지막 값을 사용하세요. left 입력 순서와 중복 레코드를 유지하여 공통 key만 결합합니다. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
hash join과 중복 key 정책

구현할 함수
-----------
def hashing_r03_hash_join(left: list[tuple[str, int]], right: list[tuple[str, str]]) -> list[tuple[str, int, str]]:

예시 및 필수 테스트
-------------------
- hashing_r03_hash_join([('a', 1), ('b', 2)], [('b', 'B'), ('a', 'A')]) == [('a', 1, 'A'), ('b', 2, 'B')]
- hashing_r03_hash_join([('a', 1), ('a', 2)], [('a', 'old'), ('a', 'new')]) == [('a', 1, 'new'), ('a', 2, 'new')]
- (hashing_r03_hash_join([], [('a', 'A')]), hashing_r03_hash_join([('x', 1)], [])) == ([], [])

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0512 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r03_hash_join(left: list[tuple[str, int]], right: list[tuple[str, str]]) -> list[tuple[str, int, str]]:
    raise NotImplementedError("TODO: CI0512")


def self_test() -> None:
    assert hashing_r03_hash_join([('a', 1), ('b', 2)], [('b', 'B'), ('a', 'A')]) == [('a', 1, 'A'), ('b', 2, 'B')]
    assert hashing_r03_hash_join([('a', 1), ('a', 2)], [('a', 'old'), ('a', 'new')]) == [('a', 1, 'new'), ('a', 2, 'new')]
    assert (hashing_r03_hash_join([], [('a', 'A')]), hashing_r03_hash_join([('x', 1)], [])) == ([], [])
