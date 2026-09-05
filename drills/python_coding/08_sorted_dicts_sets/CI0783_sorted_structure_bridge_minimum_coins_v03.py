"""
CI0783 — 정렬 구조 → 동전 최소 개수 DP

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 03 / 20
Time cap: 720 seconds
Source checks:

문제
----
coins는 최대 30개 양의 정수(각 1~100), 0<=amount<=1000입니다. 각 액면을 무제한 써서 amount를 만드는 최소 동전 개수를 반환하세요. 불가능하면 -1, amount=0이면 0입니다. 중복 액면은 새 종류가 아니며 입력은 보존합니다.

연습 초점
---------
그리디가 실패하는 액면과 최소화 점화식

구현할 함수
-----------
def sorted_structure_bridge_minimum_coins(coins: list[int], amount: int) -> int:

예시 및 필수 테스트
-------------------
- sorted_structure_bridge_minimum_coins([], 0) == 0 and sorted_structure_bridge_minimum_coins([], 3) == -1
- sorted_structure_bridge_minimum_coins([1, 3, 4], 6) == 2 and sorted_structure_bridge_minimum_coins([2], 3) == -1
- ((_bridge_1_arg_0 := [2, 2, 5]), (_bridge_1_arg_1 := 10), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_minimum_coins(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [7]), (_bridge_2_arg_1 := 14), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_minimum_coins(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0783 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_bridge_minimum_coins(coins: list[int], amount: int) -> int:
    raise NotImplementedError("TODO: CI0783")


def self_test() -> None:
    assert sorted_structure_bridge_minimum_coins([], 0) == 0 and sorted_structure_bridge_minimum_coins([], 3) == -1
    assert sorted_structure_bridge_minimum_coins([1, 3, 4], 6) == 2 and sorted_structure_bridge_minimum_coins([2], 3) == -1
    assert ((_bridge_1_arg_0 := [2, 2, 5]), (_bridge_1_arg_1 := 10), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := sorted_structure_bridge_minimum_coins(_bridge_1_arg_0, _bridge_1_arg_1)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 2 and ((_bridge_2_arg_0 := [7]), (_bridge_2_arg_1 := 14), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := sorted_structure_bridge_minimum_coins(_bridge_2_arg_0, _bridge_2_arg_1)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 2
