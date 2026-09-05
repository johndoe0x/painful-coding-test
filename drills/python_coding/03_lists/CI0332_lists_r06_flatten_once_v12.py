"""
CI0332 — 한 단계 평탄화 — 반복 세트 6

Chapter: Lists
Seed: 17 / 40
Variant: 12 / 20
Time cap: 240 seconds
Source checks: nested_loop, append_call

문제
----
각 내부 리스트를 입력 순서대로 한 단계만 펼치세요. 이 파일은 Lists 챕터의 반복 세트 6이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
중첩 loop와 append

구현할 함수
-----------
def lists_r06_flatten_once(groups: list[list[int]]) -> list[int]:

필수 구현 방식
--------------
- 반복문 안에 반복문을 중첩해 사용한다.
- list.append()를 사용한다.

예시 및 필수 테스트
-------------------
- lists_r06_flatten_once([[1, 2], [], [3]]) == [1, 2, 3]
- lists_r06_flatten_once([]) == []
- lists_r06_flatten_once([[-1]]) == [-1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0332 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_r06_flatten_once(groups: list[list[int]]) -> list[int]:
    raise NotImplementedError("TODO: CI0332")


def self_test() -> None:
    assert lists_r06_flatten_once([[1, 2], [], [3]]) == [1, 2, 3]
    assert lists_r06_flatten_once([]) == []
    assert lists_r06_flatten_once([[-1]]) == [-1]
