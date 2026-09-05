"""
CI0270 — 정렬 리스트 두 수 합 — 반복 세트 3

Chapter: Lists
Seed: 14 / 40
Variant: 10 / 20
Time cap: 240 seconds
Source checks: while

문제
----
오름차순 values에서 두 포인터로 합이 target인 두 값의 인덱스를 반환하세요. 없으면 None입니다. 이 파일은 Lists 챕터의 반복 세트 3이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
양끝 포인터 이동

구현할 함수
-----------
def lists_r03_two_sum_sorted(values: list[int], target: int) -> tuple[int, int] | None:

필수 구현 방식
--------------
- while문을 사용한다.

예시 및 필수 테스트
-------------------
- lists_r03_two_sum_sorted([1, 2, 4, 6], 6) == (1, 2)
- lists_r03_two_sum_sorted([], 1) is None
- lists_r03_two_sum_sorted([1, 2, 3], 10) is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0270 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r03_two_sum_sorted(values: list[int], target: int) -> tuple[int, int] | None:
    raise NotImplementedError("TODO: CI0270")


def self_test() -> None:
    assert lists_r03_two_sum_sorted([1, 2, 4, 6], 6) == (1, 2)
    assert lists_r03_two_sum_sorted([], 1) is None
    assert lists_r03_two_sum_sorted([1, 2, 3], 10) is None
