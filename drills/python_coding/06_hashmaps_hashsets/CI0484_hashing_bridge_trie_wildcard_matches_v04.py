"""
CI0484 — 해시맵 → 단일 문자 와일드카드

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 04 / 20
Time cap: 720 seconds
Source checks:

문제
----
최대 200개의 길이 0~20 소문자 단어와 길이 0~20 패턴이 주어집니다. 패턴은 소문자와 '.'로 구성되고 '.'은 정확히 한 문자와 일치합니다. 전체 패턴에 맞는 단어를 중복 제거한 사전순 리스트로 반환하세요. 빈 패턴은 빈 단어만 일치, 입력은 보존합니다.

연습 초점
---------
트라이의 분기 탐색과 완전 일치

구현할 함수
-----------
def hashing_bridge_trie_wildcard_matches(words: list[str], pattern: str) -> list[str]:

예시 및 필수 테스트
-------------------
- hashing_bridge_trie_wildcard_matches([], '.') == [] and hashing_bridge_trie_wildcard_matches(['', 'a'], '') == ['']
- hashing_bridge_trie_wildcard_matches(['bad', 'dad', 'mad', 'bad', 'bade'], '.ad') == ['bad', 'dad', 'mad']
- ((_bridge_1_arg_0 := ['ab', 'ac', 'a', 'ba']), (_bridge_1_arg_1 := 'a.'), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := hashing_bridge_trie_wildcard_matches(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == ['ab', 'ac'] and ((_bridge_2_arg_0 := ['abc']), (_bridge_2_arg_1 := '..'), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := hashing_bridge_trie_wildcard_matches(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0484 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_bridge_trie_wildcard_matches(words: list[str], pattern: str) -> list[str]:
    raise NotImplementedError("TODO: CI0484")


def self_test() -> None:
    assert hashing_bridge_trie_wildcard_matches([], '.') == [] and hashing_bridge_trie_wildcard_matches(['', 'a'], '') == ['']
    assert hashing_bridge_trie_wildcard_matches(['bad', 'dad', 'mad', 'bad', 'bade'], '.ad') == ['bad', 'dad', 'mad']
    assert ((_bridge_1_arg_0 := ['ab', 'ac', 'a', 'ba']), (_bridge_1_arg_1 := 'a.'), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := hashing_bridge_trie_wildcard_matches(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == ['ab', 'ac'] and ((_bridge_2_arg_0 := ['abc']), (_bridge_2_arg_1 := '..'), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := hashing_bridge_trie_wildcard_matches(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == []
