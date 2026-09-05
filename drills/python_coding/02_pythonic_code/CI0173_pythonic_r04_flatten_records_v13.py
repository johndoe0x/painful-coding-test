"""
CI0173 — 중첩 레코드 unpacking — 반복 세트 4

Chapter: Pythonic Code
Seed: 09 / 40
Variant: 13 / 20
Time cap: 240 seconds
Source checks: for, tuple_unpack

문제
----
중첩 tuple을 loop target에서 unpack해 평평한 tuple로 반환하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
중첩 unpacking

구현할 함수
-----------
def pythonic_r04_flatten_records(records: list[tuple[str, tuple[int, int]]]) -> list[tuple[str, int, int]]:

필수 구현 방식
--------------
- for문을 사용한다.
- 대입이나 for 문에서 tuple unpacking을 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r04_flatten_records([('a', (1, 2))]) == [('a', 1, 2)]
- pythonic_r04_flatten_records([]) == []
- pythonic_r04_flatten_records([('x', (0, -1)), ('y', (2, 3))]) == [('x', 0, -1), ('y', 2, 3)]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0173 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r04_flatten_records(records: list[tuple[str, tuple[int, int]]]) -> list[tuple[str, int, int]]:
    raise NotImplementedError("TODO: CI0173")


def self_test() -> None:
    assert pythonic_r04_flatten_records([('a', (1, 2))]) == [('a', 1, 2)]
    assert pythonic_r04_flatten_records([]) == []
    assert pythonic_r04_flatten_records([('x', (0, -1)), ('y', (2, 3))]) == [('x', 0, -1), ('y', 2, 3)]
