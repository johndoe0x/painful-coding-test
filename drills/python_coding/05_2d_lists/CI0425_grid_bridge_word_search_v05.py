"""
CI0425 — 격자 → 재사용 없는 단어 탐색

Chapter: 2-D Lists
Seed: 22 / 40
Variant: 05 / 20
Time cap: 900 seconds
Source checks:

문제
----
0~5행/열의 직사각형 소문자 격자와 길이 0~10인 word가 주어집니다. 상하좌우 인접 셀을 이어 word를 만들 수 있는지 반환하세요. 한 경로에서 셀 재사용은 금지입니다. 빈 word는 빈 격자에서도 True, 입력은 보존합니다.

연습 초점
---------
DFS 백트래킹의 방문 해제

구현할 함수
-----------
def grid_bridge_word_search(board: list[list[str]], word: str) -> bool:

예시 및 필수 테스트
-------------------
- grid_bridge_word_search([], '') is True and grid_bridge_word_search([], 'a') is False
- grid_bridge_word_search([['a', 'b'], ['c', 'd']], 'abd') is True and grid_bridge_word_search([['a', 'b']], 'aba') is False
- ((_bridge_1_arg_0 := [['a', 'b'], ['a', 'a']]), (_bridge_1_arg_1 := 'aab'), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_word_search(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] is True and ((_bridge_2_arg_0 := [['a', 'b'], ['c', 'd']]), (_bridge_2_arg_1 := 'ad'), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_word_search(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0425 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def grid_bridge_word_search(board: list[list[str]], word: str) -> bool:
    raise NotImplementedError("TODO: CI0425")


def self_test() -> None:
    assert grid_bridge_word_search([], '') is True and grid_bridge_word_search([], 'a') is False
    assert grid_bridge_word_search([['a', 'b'], ['c', 'd']], 'abd') is True and grid_bridge_word_search([['a', 'b']], 'aba') is False
    assert ((_bridge_1_arg_0 := [['a', 'b'], ['a', 'a']]), (_bridge_1_arg_1 := 'aab'), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := grid_bridge_word_search(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] is True and ((_bridge_2_arg_0 := [['a', 'b'], ['c', 'd']]), (_bridge_2_arg_1 := 'ad'), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := grid_bridge_word_search(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] is False
