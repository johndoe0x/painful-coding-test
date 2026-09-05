"""
CI0125 — Python 연산 → 정수 구간 AND

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 05 / 20
Time cap: 420 seconds
Source checks:

문제
----
0<=left<=right<2**31입니다. 닫힌 구간의 모든 정수를 비트 AND한 값을 반환하세요. 구간을 모두 순회하지 않는 공통 이진 접두사 관점으로 설계하세요.

연습 초점
---------
공통 상위 비트와 큰 정수 구간

구현할 함수
-----------
def pythonic_bridge_range_bitwise_and(left: int, right: int) -> int:

예시 및 필수 테스트
-------------------
- pythonic_bridge_range_bitwise_and(5, 7) == 4 and pythonic_bridge_range_bitwise_and(0, 0) == 0
- pythonic_bridge_range_bitwise_and(7, 8) == 0 and pythonic_bridge_range_bitwise_and(12, 15) == 12
- pythonic_bridge_range_bitwise_and(0, 2147483647) == 0 and pythonic_bridge_range_bitwise_and(9, 9) == 9

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0125 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_bridge_range_bitwise_and(left: int, right: int) -> int:
    raise NotImplementedError("TODO: CI0125")


def self_test() -> None:
    assert pythonic_bridge_range_bitwise_and(5, 7) == 4 and pythonic_bridge_range_bitwise_and(0, 0) == 0
    assert pythonic_bridge_range_bitwise_and(7, 8) == 0 and pythonic_bridge_range_bitwise_and(12, 15) == 12
    assert pythonic_bridge_range_bitwise_and(0, 2147483647) == 0 and pythonic_bridge_range_bitwise_and(9, 9) == 9
