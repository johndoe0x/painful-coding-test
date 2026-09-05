"""
CI0134 — filter-map 파이프라인 — 반복 세트 2

Chapter: Pythonic Code
Seed: 07 / 40
Variant: 14 / 20
Time cap: 240 seconds
Source checks: comprehension

문제
----
양수만 고른 뒤 제곱하는 generator expression을 만들고 마지막에 리스트로 소비하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
lazy filter-map 파이프라인

구현할 함수
-----------
def pythonic_r02_positive_square_pipeline(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- comprehension 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r02_positive_square_pipeline([-1, 2, 3]) == [4, 9]
- pythonic_r02_positive_square_pipeline([]) == []
- pythonic_r02_positive_square_pipeline([0, 1]) == [1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0134 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r02_positive_square_pipeline(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0134")


def self_test() -> None:
    assert pythonic_r02_positive_square_pipeline([-1, 2, 3]) == [4, 9]
    assert pythonic_r02_positive_square_pipeline([]) == []
    assert pythonic_r02_positive_square_pipeline([0, 1]) == [1]
