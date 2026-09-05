"""
CI0181 — Inequality — 기본 계약

Chapter: Pythonic Code
Seed: 10 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks:

문제
----
연쇄 비교와 논리 부정으로 닫힌 구간 밖인지 판정한다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def outside_range(value: int, low: int, high: int) -> bool:

예시 및 필수 테스트
-------------------
- outside_range(5, 1, 4) is True
- outside_range(1, 1, 4) is False
- outside_range(4, 1, 4) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0181 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def outside_range(value: int, low: int, high: int) -> bool:
    raise NotImplementedError("TODO: CI0181")


def self_test() -> None:
    assert outside_range(5, 1, 4) is True
    assert outside_range(1, 1, 4) is False
    assert outside_range(4, 1, 4) is False
