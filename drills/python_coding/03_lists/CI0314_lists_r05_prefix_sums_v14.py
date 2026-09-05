"""
CI0314 — Prefix Sum — 반복 세트 5

Chapter: Lists
Seed: 16 / 40
Variant: 14 / 20
Time cap: 240 seconds
Source checks: for, append_call

문제
----
첫 원소가 0이고 이후에 각 prefix 합이 오는 길이 n+1 리스트를 만드세요. 이 파일은 Lists 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
누적합 전처리

구현할 함수
-----------
def lists_r05_prefix_sums(values: list[int]) -> list[int]:

필수 구현 방식
--------------
- for문을 사용한다.
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- lists_r05_prefix_sums([2, -1, 3]) == [0, 2, 1, 4]
- lists_r05_prefix_sums([]) == [0]
- lists_r05_prefix_sums([0]) == [0, 0]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0314 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r05_prefix_sums(values: list[int]) -> list[int]:
    raise NotImplementedError("TODO: CI0314")


def self_test() -> None:
    assert lists_r05_prefix_sums([2, -1, 3]) == [0, 2, 1, 4]
    assert lists_r05_prefix_sums([]) == [0]
    assert lists_r05_prefix_sums([0]) == [0, 0]
