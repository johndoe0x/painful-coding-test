"""
CI0485 — dict.get의 누락과 None

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 05 / 20
Time cap: 150 seconds
Source checks:

문제
----
각 key에 mapping.get(key, default)를 적용한 값을 순서대로 반환하세요. 저장된 None이나 0을 default로 바꾸지 않습니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
누락 키와 falsy 값을 구분

구현할 함수
-----------
def hashing_fluency_mapping_missing_vs_none(mapping: dict[str, int | None], keys: list[str], default: int) -> list[int | None]:

예시 및 필수 테스트
-------------------
- hashing_fluency_mapping_missing_vs_none({'a': None, 'b': 0}, ['a', 'b', 'c'], 9) == [None, 0, 9]
- hashing_fluency_mapping_missing_vs_none({}, [], 1) == []
- ((_practice_1_0 := {}), (_practice_1_1 := ['x', 'x']), (_practice_1_2 := (-1)), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_mapping_missing_vs_none(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [-1, -1]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0485 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_fluency_mapping_missing_vs_none(mapping: dict[str, int | None], keys: list[str], default: int) -> list[int | None]:
    raise NotImplementedError("TODO: CI0485")


def self_test() -> None:
    assert hashing_fluency_mapping_missing_vs_none({'a': None, 'b': 0}, ['a', 'b', 'c'], 9) == [None, 0, 9]
    assert hashing_fluency_mapping_missing_vs_none({}, [], 1) == []
    assert ((_practice_1_0 := {}), (_practice_1_1 := ['x', 'x']), (_practice_1_2 := (-1)), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_mapping_missing_vs_none(_practice_1_0, _practice_1_1, _practice_1_2)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == [-1, -1]
