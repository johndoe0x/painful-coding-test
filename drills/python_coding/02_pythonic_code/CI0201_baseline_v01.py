"""
CI0201 — Min Max Shortcut — 기본 계약

Chapter: Pythonic Code
Seed: 11 / 40
Variant: 01 / 20
Time cap: 180 seconds
Source checks:

문제
----
min과 max를 조합해 값을 구간 안으로 제한한다.

연습 초점
---------
핵심 Python API와 대표 경계값을 빈 화면에서 재구현

구현할 함수
-----------
def clamp(value: int, low: int, high: int) -> int:

예시 및 필수 테스트
-------------------
- clamp(12, 0, 10) == 10
- clamp(-1, 0, 10) == 0
- clamp(5, 0, 10) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0201 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def clamp(value: int, low: int, high: int) -> int:
    raise NotImplementedError("TODO: CI0201")


def self_test() -> None:
    assert clamp(12, 0, 10) == 10
    assert clamp(-1, 0, 10) == 0
    assert clamp(5, 0, 10) == 5
