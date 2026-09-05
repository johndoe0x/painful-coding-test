"""
CI0487 — 집합 대칭 차집합

Chapter: Hashmaps and Hashsets
Seed: 25 / 40
Variant: 07 / 20
Time cap: 150 seconds
Source checks:

문제
----
set.symmetric_difference 또는 집합 ^ 연산으로 한쪽에만 속한 값을 반환하세요. 두 원본은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
합집합과 대칭 차집합

구현할 함수
-----------
def hashing_fluency_set_symmetric_difference(left: set[int], right: set[int]) -> set[int]:

예시 및 필수 테스트
-------------------
- hashing_fluency_set_symmetric_difference({1, 2}, {2, 3}) == {1, 3}
- hashing_fluency_set_symmetric_difference(set(), set()) == set()
- ((_practice_1_0 := {0, -1}), (_practice_1_1 := {0}), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_set_symmetric_difference(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {-1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0487 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def hashing_fluency_set_symmetric_difference(left: set[int], right: set[int]) -> set[int]:
    raise NotImplementedError("TODO: CI0487")


def self_test() -> None:
    assert hashing_fluency_set_symmetric_difference({1, 2}, {2, 3}) == {1, 3}
    assert hashing_fluency_set_symmetric_difference(set(), set()) == set()
    assert ((_practice_1_0 := {0, -1}), (_practice_1_1 := {0}), (_practice_1_before := repr((_practice_1_0, _practice_1_1))), (_practice_1_result := hashing_fluency_set_symmetric_difference(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0, _practice_1_1)) == _practice_1_before else object())[-1] == {-1}
