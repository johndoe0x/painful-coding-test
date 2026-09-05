"""
CI0507 — 문자열 key 정규화 — 반복 세트 3

Chapter: Hashmaps and Hashsets
Seed: 26 / 40
Variant: 07 / 20
Time cap: 240 seconds
Source checks:

문제
----
key의 앞뒤 공백을 제거하고 소문자로 바꿔 값을 합산하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
정규화된 hash key

구현할 함수
-----------
def hashing_r03_normalize_keys(records: list[tuple[str, int]]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- hashing_r03_normalize_keys([(' A ', 1), ('a', 2)]) == {'a': 3}
- hashing_r03_normalize_keys([]) == {}
- hashing_r03_normalize_keys([('', 1), (' ', 2)]) == {'': 3}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0507 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r03_normalize_keys(records: list[tuple[str, int]]) -> dict[str, int]:
    raise NotImplementedError("TODO: CI0507")


def self_test() -> None:
    assert hashing_r03_normalize_keys([(' A ', 1), ('a', 2)]) == {'a': 3}
    assert hashing_r03_normalize_keys([]) == {}
    assert hashing_r03_normalize_keys([('', 1), (' ', 2)]) == {'': 3}
