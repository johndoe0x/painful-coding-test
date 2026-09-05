"""
CI0126 — yield의 지연 실행

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 06 / 20
Time cap: 180 seconds
Source checks: yield

문제
----
yield로 짝수의 제곱을 순서대로 생성하는 generator를 반환하세요. 리스트를 미리 만들지 않습니다. 입력을 바꾸지 않으며 첫 next 전에 입력에 추가된 값도 순회에 포함합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
generator 시작 시점과 한 번만 소비되는 iterator

구현할 함수
-----------
def pythonic_fluency_yield_even_squares(values: list[int]) -> object:

필수 구현 방식
--------------
- yield 또는 yield from으로 generator를 만든다.

예시 및 필수 테스트
-------------------
- list(pythonic_fluency_yield_even_squares([1, 2, -4])) == [4, 16]
- list(pythonic_fluency_yield_even_squares([])) == []
- ((v := [2]), (g := pythonic_fluency_yield_even_squares(v)), v.append(4), list(g), list(g), v)[3:] == ([4, 16], [], [2, 4])

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


def pythonic_fluency_yield_even_squares(values: list[int]) -> object:
    raise NotImplementedError("TODO: CI0126")


def self_test() -> None:
    assert list(pythonic_fluency_yield_even_squares([1, 2, -4])) == [4, 16]
    assert list(pythonic_fluency_yield_even_squares([])) == []
    assert ((v := [2]), (g := pythonic_fluency_yield_even_squares(v)), v.append(4), list(g), list(g), v)[3:] == ([4, 16], [], [2, 4])
