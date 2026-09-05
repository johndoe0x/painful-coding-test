"""
CI0483 — Counter 교집합 최소 빈도

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 03 / 20
Time cap: 150 seconds
Source checks: counter_call

문제
----
두 Counter의 & 연산으로 공통 원소의 최소 양수 빈도만 dict로 반환하세요. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
set 교집합과 multiset 빈도 차이

구현할 함수
-----------
def hashing_fluency_counter_intersection(left: list[str], right: list[str]) -> dict[str, int]:

필수 구현 방식
--------------
- collections.Counter를 사용한다.

예시 및 필수 테스트
-------------------
- hashing_fluency_counter_intersection(['a', 'a', 'b'], ['a', 'b', 'b']) == {'a': 1, 'b': 1}
- hashing_fluency_counter_intersection([], ['a']) == {}
- ((_practice_1_0 := ['x', 'x', 'x']), (_practice_1_1 := ['x', 'x']), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_counter_intersection(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {'x': 2}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0483 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_fluency_counter_intersection(left: list[str], right: list[str]) -> dict[str, int]:
    raise NotImplementedError("TODO: CI0483")


def self_test() -> None:
    assert hashing_fluency_counter_intersection(['a', 'a', 'b'], ['a', 'b', 'b']) == {'a': 1, 'b': 1}
    assert hashing_fluency_counter_intersection([], ['a']) == {}
    assert ((_practice_1_0 := ['x', 'x', 'x']), (_practice_1_1 := ['x', 'x']), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_counter_intersection(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {'x': 2}
