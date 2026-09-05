"""
CI0104 — 짝수 제곱 generator — 반복 세트 1

Chapter: Pythonic Code
Seed: 06 / 40
Variant: 04 / 20
Time cap: 240 seconds
Source checks: yield

문제
----
짝수의 제곱을 입력 순서대로 yield하는 generator function을 작성하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
yield와 lazy evaluation

구현할 함수
-----------
def pythonic_r01_yield_even_squares(values: list[int]) -> object:

필수 구현 방식
--------------
- yield 또는 yield from으로 generator를 만든다.

예시 및 필수 테스트
-------------------
- list(pythonic_r01_yield_even_squares([1, 2, 4])) == [4, 16]
- list(pythonic_r01_yield_even_squares([])) == []
- list(pythonic_r01_yield_even_squares([-2, 3, 0])) == [4, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0104 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r01_yield_even_squares(values: list[int]) -> object:
    raise NotImplementedError("TODO: CI0104")


def self_test() -> None:
    assert list(pythonic_r01_yield_even_squares([1, 2, 4])) == [4, 16]
    assert list(pythonic_r01_yield_even_squares([])) == []
    assert list(pythonic_r01_yield_even_squares([-2, 3, 0])) == [4, 0]
