"""
CI0123 — Python 연산 → XOR 두 그룹

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 03 / 20
Time cap: 600 seconds
Source checks:

문제
----
길이 2~202의 배열에서 서로 다른 두 값만 각각 1회, 나머지는 각각 정확히 2회 나옵니다. 한 번 나온 두 값을 오름차순 tuple로 반환하세요. 정수 범위는 -1000~1000, 입력은 보존합니다.

연습 초점
---------
최하위 비트로 XOR 그룹 분리

구현할 함수
-----------
def pythonic_bridge_two_unpaired(values: list[int]) -> tuple[int, int]:

예시 및 필수 테스트
-------------------
- pythonic_bridge_two_unpaired([2, 1]) == (1, 2)
- pythonic_bridge_two_unpaired([1, 2, 1, 3, 2, 5]) == (3, 5)
- ((_bridge_1_arg_0 := [0, -1, 4, 4]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := pythonic_bridge_two_unpaired(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (-1, 0) and ((_bridge_2_arg_0 := [-2, 3, 8, 8]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := pythonic_bridge_two_unpaired(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (-2, 3)

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0123 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_bridge_two_unpaired(values: list[int]) -> tuple[int, int]:
    raise NotImplementedError("TODO: CI0123")


def self_test() -> None:
    assert pythonic_bridge_two_unpaired([2, 1]) == (1, 2)
    assert pythonic_bridge_two_unpaired([1, 2, 1, 3, 2, 5]) == (3, 5)
    assert ((_bridge_1_arg_0 := [0, -1, 4, 4]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := pythonic_bridge_two_unpaired(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == (-1, 0) and ((_bridge_2_arg_0 := [-2, 3, 8, 8]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := pythonic_bridge_two_unpaired(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == (-2, 3)
