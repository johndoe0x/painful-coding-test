"""
CI0602 — 마지막 값 index — 반복 세트 8

Chapter: Hashmaps and Hashsets
Seed: 31 / 40
Variant: 02 / 20
Time cap: 240 seconds
Source checks:

문제
----
(key, value)를 순회해 key별 마지막 값을 저장하세요. 이 파일은 Hashmaps and Hashsets 챕터의 반복 세트 8이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
dict 삽입·갱신

구현할 함수
-----------
def hashing_r08_last_value_by_key(records: list[tuple[str, int]]) -> dict[str, int]:

예시 및 필수 테스트
-------------------
- hashing_r08_last_value_by_key([('a', 1), ('a', 2)]) == {'a': 2}
- hashing_r08_last_value_by_key([]) == {}
- hashing_r08_last_value_by_key([('x', -1), ('y', 0)]) == {'x': -1, 'y': 0}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0602 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_r08_last_value_by_key(records: list[tuple[str, int]]) -> dict[str, int]:
    raise NotImplementedError("TODO: CI0602")


def self_test() -> None:
    assert hashing_r08_last_value_by_key([('a', 1), ('a', 2)]) == {'a': 2}
    assert hashing_r08_last_value_by_key([]) == {}
    assert hashing_r08_last_value_by_key([('x', -1), ('y', 0)]) == {'x': -1, 'y': 0}
