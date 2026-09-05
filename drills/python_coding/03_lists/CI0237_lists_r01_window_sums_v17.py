"""
CI0237 — 고정 창 합 — 반복 세트 1

Chapter: Lists
Seed: 12 / 40
Variant: 17 / 20
Time cap: 240 seconds
Source checks: for

문제
----
size 길이의 모든 연속 구간 합을 O(n)에 반환하세요. 유효한 창이 없으면 빈 리스트입니다. 이 파일은 Lists 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
sliding window 갱신

구현할 함수
-----------
def lists_r01_window_sums(values: list[int], size: int) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- lists_r01_window_sums([1, 2, 3, 4], 2) == [3, 5, 7]
- lists_r01_window_sums([], 1) == []
- lists_r01_window_sums([1, 2], 3) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0237 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r01_window_sums(values: list[int], size: int) -> list[int]:
    raise NotImplementedError("TODO: CI0237")


def self_test() -> None:
    assert lists_r01_window_sums([1, 2, 3, 4], 2) == [3, 5, 7]
    assert lists_r01_window_sums([], 1) == []
    assert lists_r01_window_sums([1, 2], 3) == []
