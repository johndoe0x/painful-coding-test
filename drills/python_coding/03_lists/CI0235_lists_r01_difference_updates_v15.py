"""
CI0235 — Difference Array 구간 갱신 — 반복 세트 1

Chapter: Lists
Seed: 12 / 40
Variant: 15 / 20
Time cap: 240 seconds
Source checks: for

문제
----
0으로 시작한 length 배열에 각 (start, end, delta)를 양끝 포함 구간으로 더한 최종 배열을 반환하세요. 이 파일은 Lists 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
차분 배열과 prefix 복원

구현할 함수
-----------
def lists_r01_difference_updates(length: int, updates: list[tuple[int, int, int]]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- lists_r01_difference_updates(5, [(1, 3, 2), (2, 4, 1)]) == [0, 2, 3, 3, 1]
- lists_r01_difference_updates(0, []) == []
- lists_r01_difference_updates(3, [(0, 2, -1)]) == [-1, -1, -1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0235 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r01_difference_updates(length: int, updates: list[tuple[int, int, int]]) -> list[int]:
    raise NotImplementedError("TODO: CI0235")


def self_test() -> None:
    assert lists_r01_difference_updates(5, [(1, 3, 2), (2, 4, 1)]) == [0, 2, 3, 3, 1]
    assert lists_r01_difference_updates(0, []) == []
    assert lists_r01_difference_updates(3, [(0, 2, -1)]) == [-1, -1, -1]
