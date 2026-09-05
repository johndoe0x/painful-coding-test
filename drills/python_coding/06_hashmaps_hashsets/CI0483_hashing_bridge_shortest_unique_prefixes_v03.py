"""
CI0483 — 해시맵 → 최소 고유 접두사

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 03 / 20
Time cap: 720 seconds
Source checks:

문제
----
최대 200개의 길이 0~30 소문자 문자열 words에서 각 원소만 식별하는 가장 짧은 비어 있지 않은 접두사를 입력 순서로 반환하세요. 다른 원소가 그 접두사로 시작하면 고유하지 않습니다. 중복 단어·빈 단어·다른 단어의 접두사인 단어 등 고유 접두사가 없으면 None입니다. 입력은 보존합니다.

연습 초점
---------
트라이 통과 횟수와 종료 표식의 차이

구현할 함수
-----------
def hashing_bridge_shortest_unique_prefixes(words: list[str]) -> list[str | None]:

예시 및 필수 테스트
-------------------
- hashing_bridge_shortest_unique_prefixes([]) == [] and hashing_bridge_shortest_unique_prefixes(['dog', 'dove', 'cat']) == ['dog', 'dov', 'c']
- hashing_bridge_shortest_unique_prefixes(['a', 'ab', 'b']) == [None, 'ab', 'b']
- ((_bridge_1_arg_0 := ['x', 'x', '', 'y']), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := hashing_bridge_shortest_unique_prefixes(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [None, None, None, 'y']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0483 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_bridge_shortest_unique_prefixes(words: list[str]) -> list[str | None]:
    raise NotImplementedError("TODO: CI0483")


def self_test() -> None:
    assert hashing_bridge_shortest_unique_prefixes([]) == [] and hashing_bridge_shortest_unique_prefixes(['dog', 'dove', 'cat']) == ['dog', 'dov', 'c']
    assert hashing_bridge_shortest_unique_prefixes(['a', 'ab', 'b']) == [None, 'ab', 'b']
    assert ((_bridge_1_arg_0 := ['x', 'x', '', 'y']), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := hashing_bridge_shortest_unique_prefixes(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == [None, None, None, 'y']
