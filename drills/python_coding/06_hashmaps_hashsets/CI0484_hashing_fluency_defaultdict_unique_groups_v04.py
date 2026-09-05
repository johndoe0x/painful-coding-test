"""
CI0484 — defaultdict(set)과 반환 변환

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 04 / 20
Time cap: 180 seconds
Source checks: defaultdict_call, sorted_call

문제
----
defaultdict(set)으로 key별 value 중복을 제거한 뒤 각 집합을 sorted로 바꿔 dict로 반환하세요. 빈 문자열도 유효하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
기본 factory와 반환 자료형

구현할 함수
-----------
def hashing_fluency_defaultdict_unique_groups(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:

필수 구현 방식
--------------
- collections.defaultdict를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_fluency_defaultdict_unique_groups([('a', 'z'), ('a', 'b'), ('a', 'z'), ('b', 'x')]) == {'a': ['b', 'z'], 'b': ['x']}
- hashing_fluency_defaultdict_unique_groups([]) == {}
- ((_practice_1_0 := [('', ''), ('', 'a')]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := hashing_fluency_defaultdict_unique_groups(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == {'': ['', 'a']}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0484 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_fluency_defaultdict_unique_groups(pairs: list[tuple[str, str]]) -> dict[str, list[str]]:
    raise NotImplementedError("TODO: CI0484")


def self_test() -> None:
    assert hashing_fluency_defaultdict_unique_groups([('a', 'z'), ('a', 'b'), ('a', 'z'), ('b', 'x')]) == {'a': ['b', 'z'], 'b': ['x']}
    assert hashing_fluency_defaultdict_unique_groups([]) == {}
    assert ((_practice_1_0 := [('', ''), ('', 'a')]), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := hashing_fluency_defaultdict_unique_groups(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == {'': ['', 'a']}
