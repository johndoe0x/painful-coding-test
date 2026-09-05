"""
CI0786 — bisect key의 적용 대상

Chapter: Sorted Dicts and Sorted Sets
Seed: 40 / 40
Variant: 06 / 20
Time cap: 240 seconds
Source checks: bisect_call, lambda

문제
----
records는 첫 정수 필드 오름차순입니다. bisect_left(records, target, key=lambda item: item[0])로 같은 key의 첫 문자열을 반환하고 없으면 None입니다. target은 tuple이 아닌 정수이며 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
bisect와 insort의 key 적용 차이

구현할 함수
-----------
def sorted_structure_fluency_bisect_record_key(records: list[tuple[int, str]], target: int) -> str | None:

필수 구현 방식
--------------
- bisect API를 사용한다.
- lambda 표현식을 사용한다.

예시 및 필수 테스트
-------------------
- sorted_structure_fluency_bisect_record_key([(1, 'x'), (2, 'b'), (2, 'a')], 2) == 'b'
- sorted_structure_fluency_bisect_record_key([], 2) is None
- ((_practice_1_0 := [(1, 'x'), (3, 'y')]), (_practice_1_1 := 2), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_record_key(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0786 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorted_structure_fluency_bisect_record_key(records: list[tuple[int, str]], target: int) -> str | None:
    raise NotImplementedError("TODO: CI0786")


def self_test() -> None:
    assert sorted_structure_fluency_bisect_record_key([(1, 'x'), (2, 'b'), (2, 'a')], 2) == 'b'
    assert sorted_structure_fluency_bisect_record_key([], 2) is None
    assert ((_practice_1_0 := [(1, 'x'), (3, 'y')]), (_practice_1_1 := 2), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorted_structure_fluency_bisect_record_key(_practice_1_0, _practice_1_1)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] is None
