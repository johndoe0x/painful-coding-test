"""
CI0482 — 해시맵 → 접두사 빈도 질의

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 02 / 20
Time cap: 600 seconds
Source checks:

문제
----
words와 prefixes는 각각 최대 200개의 길이 0~30 소문자 문자열입니다. 각 prefix로 시작하는 words 원소 수를 질의 순서대로 반환하세요. words의 중복을 각각 세며 빈 접두사는 모든 원소와 일치합니다. 입력은 보존합니다.

연습 초점
---------
트라이 노드별 통과 빈도와 빈 접두사

구현할 함수
-----------
def hashing_bridge_trie_prefix_counts(words: list[str], prefixes: list[str]) -> list[int]:

예시 및 필수 테스트
-------------------
- hashing_bridge_trie_prefix_counts([], ['', 'a']) == [0, 0] and hashing_bridge_trie_prefix_counts(['a'], []) == []
- hashing_bridge_trie_prefix_counts(['app', 'apple', 'app', 'bat'], ['app', 'ap', 'b', 'z', '']) == [3, 3, 1, 0, 4]
- ((_bridge_1_arg_0 := ['', 'a', 'ab']), (_bridge_1_arg_1 := ['', 'a', 'ab', 'abc']), (_bridge_1_before := repr((_bridge_1_arg_0, _bridge_1_arg_1))), (_bridge_1_result := hashing_bridge_trie_prefix_counts(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0, _bridge_1_arg_1)) == _bridge_1_before else object())[-1] == [3, 2, 1, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0482 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_bridge_trie_prefix_counts(words: list[str], prefixes: list[str]) -> list[int]:
    raise NotImplementedError("TODO: CI0482")


def self_test() -> None:
    assert hashing_bridge_trie_prefix_counts([], ['', 'a']) == [0, 0] and hashing_bridge_trie_prefix_counts(['a'], []) == []
    assert hashing_bridge_trie_prefix_counts(['app', 'apple', 'app', 'bat'], ['app', 'ap', 'b', 'z', '']) == [3, 3, 1, 0, 4]
    assert ((_bridge_1_arg_0 := ['', 'a', 'ab']), (_bridge_1_arg_1 := ['', 'a', 'ab', 'abc']), (_bridge_1_before := repr((_bridge_1_arg_0, _bridge_1_arg_1))), (_bridge_1_result := hashing_bridge_trie_prefix_counts(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0, _bridge_1_arg_1)) == _bridge_1_before else object())[-1] == [3, 2, 1, 0]
