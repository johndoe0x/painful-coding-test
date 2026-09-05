"""
CI0175 — lazy 앞부분 취하기 — 반복 세트 4

Chapter: Pythonic Code
Seed: 09 / 40
Variant: 15 / 20
Time cap: 240 seconds
Source checks: itertools_call

문제
----
itertools.islice로 iterable의 앞 count개만 소비해 리스트로 반환하세요. 이 파일은 Pythonic Code 챕터의 반복 세트 4이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
부분 소비와 무한 iterable 대응

구현할 함수
-----------
def pythonic_r04_take_islice(values: object, count: int) -> list[object]:

필수 구현 방식
--------------
- itertools API를 사용한다.

예시 및 필수 테스트
-------------------
- pythonic_r04_take_islice([1, 2, 3], 2) == [1, 2]
- pythonic_r04_take_islice([], 3) == []
- pythonic_r04_take_islice((x for x in range(5)), 0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0175 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def pythonic_r04_take_islice(values: object, count: int) -> list[object]:
    raise NotImplementedError("TODO: CI0175")


def self_test() -> None:
    assert pythonic_r04_take_islice([1, 2, 3], 2) == [1, 2]
    assert pythonic_r04_take_islice([], 3) == []
    assert pythonic_r04_take_islice((x for x in range(5)), 0) == []
