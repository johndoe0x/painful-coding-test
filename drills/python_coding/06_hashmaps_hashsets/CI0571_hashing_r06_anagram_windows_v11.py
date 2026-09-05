"""
CI0571 — 애너그램 시작 index — 반복 세트 6

Chapter: Hashmaps and Hashsets
Seed: 29 / 40
Variant: 11 / 20
Time cap: 240 seconds
Source checks: counter_call

문제
----
고정 길이 sliding Counter로 text에서 pattern의 애너그램이 시작하는 모든 index를 반환하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
증감 Counter window

구현할 함수
-----------
def hashing_r06_anagram_windows(text: str, pattern: str) -> list[int]:

필수 구현 방식
--------------
- collections.Counter를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_r06_anagram_windows('cbaebabacd', 'abc') == [0, 6]
- hashing_r06_anagram_windows('', 'a') == []
- hashing_r06_anagram_windows('aaaa', 'aa') == [0, 1, 2]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0571 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r06_anagram_windows(text: str, pattern: str) -> list[int]:
    raise NotImplementedError("TODO: CI0571")


def self_test() -> None:
    assert hashing_r06_anagram_windows('cbaebabacd', 'abc') == [0, 6]
    assert hashing_r06_anagram_windows('', 'a') == []
    assert hashing_r06_anagram_windows('aaaa', 'aa') == [0, 1, 2]
