"""
CI0198 — 누적 합 — 반복 세트 5

Chapter: Pythonic Code
Seed: 10 / 40
Variant: 18 / 20
Time cap: 240 seconds
Source checks: itertools_call

문제
----
itertools.accumulate로 prefix sum 리스트를 반환하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
lazy 누적 연산

구현할 함수
-----------
def pythonic_r05_accumulated_totals(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- itertools API를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r05_accumulated_totals([1, 2, 3]) == [1, 3, 6]
- pythonic_r05_accumulated_totals([]) == []
- pythonic_r05_accumulated_totals([-1, 2]) == [-1, 1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0198 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r05_accumulated_totals(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0198")


def self_test() -> None:
    assert pythonic_r05_accumulated_totals([1, 2, 3]) == [1, 3, 6]
    assert pythonic_r05_accumulated_totals([]) == []
    assert pythonic_r05_accumulated_totals([-1, 2]) == [-1, 1]
