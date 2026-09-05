"""
CI0313 — 고정 크기 청크 — 반복 세트 5

Chapter: Lists
Seed: 16 / 40
Variant: 13 / 20
Time cap: 240 seconds
Source checks: range, slice

문제
----
양수 size 단위로 연속 청크를 만들고 마지막의 짧은 청크도 포함하세요. 이 파일은 Lists 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
range step과 slicing

구현할 함수
-----------
def lists_r05_chunk_by_size(values: list[int], size: int) -> list[list[int]]:

필수 구현 방식
--------------
- range()를 사용한다.
- 슬라이스 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- lists_r05_chunk_by_size([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
- lists_r05_chunk_by_size([], 3) == []
- lists_r05_chunk_by_size([1, 2], 5) == [[1, 2]]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0313 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r05_chunk_by_size(values: list[int], size: int) -> list[list[int]]:
    raise NotImplementedError("TODO: CI0313")


def self_test() -> None:
    assert lists_r05_chunk_by_size([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
    assert lists_r05_chunk_by_size([], 3) == []
    assert lists_r05_chunk_by_size([1, 2], 5) == [[1, 2]]
