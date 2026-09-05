"""
CI0124 — Python 연산 → 고정 폭 비트 반전

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 04 / 20
Time cap: 360 seconds
Source checks:

문제
----
0<=width<=32, 0<=value<2**width입니다. 정확히 width개 비트의 순서를 뒤집은 정수를 반환하세요. 선행 0도 폭에 포함하며 width=0일 때 value=0이고 결과는 0입니다.

연습 초점
---------
시프트와 고정 폭의 선행 0

구현할 함수
-----------
def pythonic_bridge_reverse_fixed_bits(value: int, width: int) -> int:

예시 및 필수 테스트
-------------------
- pythonic_bridge_reverse_fixed_bits(0, 0) == 0 and pythonic_bridge_reverse_fixed_bits(1, 4) == 8
- pythonic_bridge_reverse_fixed_bits(6, 4) == 6 and pythonic_bridge_reverse_fixed_bits(11, 5) == 26
- pythonic_bridge_reverse_fixed_bits(255, 8) == 255 and pythonic_bridge_reverse_fixed_bits(2, 3) == 2

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0124 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_bridge_reverse_fixed_bits(value: int, width: int) -> int:
    raise NotImplementedError("TODO: CI0124")


def self_test() -> None:
    assert pythonic_bridge_reverse_fixed_bits(0, 0) == 0 and pythonic_bridge_reverse_fixed_bits(1, 4) == 8
    assert pythonic_bridge_reverse_fixed_bits(6, 4) == 6 and pythonic_bridge_reverse_fixed_bits(11, 5) == 26
    assert pythonic_bridge_reverse_fixed_bits(255, 8) == 255 and pythonic_bridge_reverse_fixed_bits(2, 3) == 2
