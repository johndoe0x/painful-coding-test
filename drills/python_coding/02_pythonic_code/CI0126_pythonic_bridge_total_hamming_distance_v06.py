"""
CI0126 — Python 연산 → 모든 쌍 비트 거리

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 06 / 20
Time cap: 420 seconds
Source checks:

문제
----
길이 0~200, 원소 0<=x<2**16인 배열의 서로 다른 인덱스 쌍 i<j마다 다른 비트 수를 더해 반환하세요. 같은 값의 서로 다른 위치도 쌍에 포함합니다. 입력은 보존합니다.

연습 초점
---------
비트별 0과 1 빈도의 곱

구현할 함수
-----------
def pythonic_bridge_total_hamming_distance(values: list[int]) -> int:

예시 및 필수 테스트
-------------------
- pythonic_bridge_total_hamming_distance([]) == 0 and pythonic_bridge_total_hamming_distance([7]) == 0
- pythonic_bridge_total_hamming_distance([4, 14, 2]) == 6 and pythonic_bridge_total_hamming_distance([0, 0, 1]) == 2
- ((_bridge_1_arg_0 := [0, 65535]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := pythonic_bridge_total_hamming_distance(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 16 and ((_bridge_2_arg_0 := [1, 2, 3]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := pythonic_bridge_total_hamming_distance(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 4

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0126 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_bridge_total_hamming_distance(values: list[int]) -> int:
    raise NotImplementedError("TODO: CI0126")


def self_test() -> None:
    assert pythonic_bridge_total_hamming_distance([]) == 0 and pythonic_bridge_total_hamming_distance([7]) == 0
    assert pythonic_bridge_total_hamming_distance([4, 14, 2]) == 6 and pythonic_bridge_total_hamming_distance([0, 0, 1]) == 2
    assert ((_bridge_1_arg_0 := [0, 65535]), (_bridge_1_before := repr((_bridge_1_arg_0,))), (_bridge_1_result := pythonic_bridge_total_hamming_distance(_bridge_1_arg_0)), _bridge_1_result if repr((_bridge_1_arg_0,)) == _bridge_1_before else object())[-1] == 16 and ((_bridge_2_arg_0 := [1, 2, 3]), (_bridge_2_before := repr((_bridge_2_arg_0,))), (_bridge_2_result := pythonic_bridge_total_hamming_distance(_bridge_2_arg_0)), _bridge_2_result if repr((_bridge_2_arg_0,)) == _bridge_2_before else object())[-1] == 4
