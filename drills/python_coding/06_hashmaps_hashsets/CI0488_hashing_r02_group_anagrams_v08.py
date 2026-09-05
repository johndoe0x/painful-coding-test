"""
CI0488 — 애너그램 그룹 — 반복 세트 2

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 08 / 20
Time cap: 240 seconds
Source checks: counter_call, defaultdict_call

문제
----
문자의 Counter 빈도를 hashable key로 사용해 애너그램을 입력 그룹 생성 순서와 그룹 내부 입력 순서대로 묶으세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
Counter signature grouping

구현할 함수
-----------
def hashing_r02_group_anagrams(words: list[str]) -> list[list[str]]:

필수 구현 방식
--------------
- collections.Counter를 사용한다.
- collections.defaultdict를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_r02_group_anagrams(['eat', 'tea', 'tan', 'ate']) == [['eat', 'tea', 'ate'], ['tan']]
- hashing_r02_group_anagrams([]) == []
- hashing_r02_group_anagrams(['', '']) == [['', '']]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0488 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r02_group_anagrams(words: list[str]) -> list[list[str]]:
    raise NotImplementedError("TODO: CI0488")


def self_test() -> None:
    assert hashing_r02_group_anagrams(['eat', 'tea', 'tan', 'ate']) == [['eat', 'tea', 'ate'], ['tan']]
    assert hashing_r02_group_anagrams([]) == []
    assert hashing_r02_group_anagrams(['', '']) == [['', '']]
