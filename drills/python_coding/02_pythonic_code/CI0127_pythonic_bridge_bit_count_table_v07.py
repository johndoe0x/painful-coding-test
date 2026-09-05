"""
CI0127 — Python 연산 → 비트 수 DP 표

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 07 / 20
Time cap: 300 seconds
Source checks:

문제
----
0<=n<=10000입니다. 각 i=0..n의 이진수 1 개수를 순서대로 담은 길이 n+1 리스트를 반환하세요.

연습 초점
---------
하위 문제 재사용과 비트 점화식

구현할 함수
-----------
def pythonic_bridge_bit_count_table(n: int) -> list[int]:

예시 및 필수 테스트
-------------------
- pythonic_bridge_bit_count_table(0) == [0] and pythonic_bridge_bit_count_table(1) == [0, 1]
- pythonic_bridge_bit_count_table(5) == [0, 1, 1, 2, 1, 2]
- pythonic_bridge_bit_count_table(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0127 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_bridge_bit_count_table(n: int) -> list[int]:
    raise NotImplementedError("TODO: CI0127")


def self_test() -> None:
    assert pythonic_bridge_bit_count_table(0) == [0] and pythonic_bridge_bit_count_table(1) == [0, 1]
    assert pythonic_bridge_bit_count_table(5) == [0, 1, 1, 2, 1, 2]
    assert pythonic_bridge_bit_count_table(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]
