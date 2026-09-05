"""
CI0220 — math 수치 도구 — 반복 세트 6

Chapter: Pythonic Code
Seed: 11 / 40
Variant: 20 / 20
Time cap: 270 seconds
Source checks: math_call

문제
----
math의 gcd, lcm, isqrt, ceil, inf를 사용해 지정된 다섯 결과를 딕셔너리로 반환하세요. isqrt에는 abs(a)를 사용합니다. 이 파일은 Pythonic Code 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
math 표준 라이브러리 조합

구현할 함수
-----------
def pythonic_r06_math_toolkit(a: int, b: int, value: float) -> dict[str, object]:

필수 구현 방식
--------------
- math 모듈의 함수 또는 상수를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r06_math_toolkit(12, 18, 2.1) == {'gcd': 6, 'lcm': 36, 'isqrt': 3, 'ceil': 3, 'sentinel': float('inf')}
- pythonic_r06_math_toolkit(0, 5, -1.2) == {'gcd': 5, 'lcm': 0, 'isqrt': 0, 'ceil': -1, 'sentinel': float('inf')}
- pythonic_r06_math_toolkit(-9, 6, 3.0) == {'gcd': 3, 'lcm': 18, 'isqrt': 3, 'ceil': 3, 'sentinel': float('inf')}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0220 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r06_math_toolkit(a: int, b: int, value: float) -> dict[str, object]:
    raise NotImplementedError("TODO: CI0220")


def self_test() -> None:
    assert pythonic_r06_math_toolkit(12, 18, 2.1) == {'gcd': 6, 'lcm': 36, 'isqrt': 3, 'ceil': 3, 'sentinel': float('inf')}
    assert pythonic_r06_math_toolkit(0, 5, -1.2) == {'gcd': 5, 'lcm': 0, 'isqrt': 0, 'ceil': -1, 'sentinel': float('inf')}
    assert pythonic_r06_math_toolkit(-9, 6, 3.0) == {'gcd': 3, 'lcm': 18, 'isqrt': 3, 'ceil': 3, 'sentinel': float('inf')}
