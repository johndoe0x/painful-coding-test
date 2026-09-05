"""
CI0161 — Zip — 기본 계약

Chapter: Pythonic Code
Seed: 09 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks: zip_call

문제
----
zip으로 두 열을 짝지으며 짧은 쪽 길이에 맞춘다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def pair_columns(names: list[str], scores: list[int]) -> list[tuple[str, int]]:

필수 구현 방식
--------------
- zip()을 사용한다.

예시 및 필수 테스트
-------------------
- pair_columns([], []) == []
- pair_columns(['A', 'B'], [10, 20, 30]) == [('A', 10), ('B', 20)]
- pair_columns(['A'], []) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0161 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pair_columns(names: list[str], scores: list[int]) -> list[tuple[str, int]]:
    raise NotImplementedError("TODO: CI0161")


def self_test() -> None:
    assert pair_columns([], []) == []
    assert pair_columns(['A', 'B'], [10, 20, 30]) == [('A', 10), ('B', 20)]
    assert pair_columns(['A'], []) == []
