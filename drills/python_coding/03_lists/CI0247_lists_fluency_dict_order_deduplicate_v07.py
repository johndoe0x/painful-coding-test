"""
CI0247 — dict.fromkeys로 첫 출현 보존

Chapter: Lists
Seed: 13 / 40
Variant: 07 / 20
Time cap: 150 seconds
Source checks:

문제
----
dict.fromkeys로 중복을 제거하고 첫 출현 순서의 새 리스트를 반환하세요. 문자열은 그대로 비교하고 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
dict 삽입 순서와 set 정렬의 차이

구현할 함수
-----------
def lists_fluency_dict_order_deduplicate(values: list[str]) -> list[str]:

예시 및 필수 테스트
-------------------
- lists_fluency_dict_order_deduplicate(['b', 'a', 'b', 'c']) == ['b', 'a', 'c']
- lists_fluency_dict_order_deduplicate([]) == []
- ((_practice_1_0 := ['', 'A', 'a', '']), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := lists_fluency_dict_order_deduplicate(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['', 'A', 'a']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0247 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def lists_fluency_dict_order_deduplicate(values: list[str]) -> list[str]:
    raise NotImplementedError("TODO: CI0247")


def self_test() -> None:
    assert lists_fluency_dict_order_deduplicate(['b', 'a', 'b', 'c']) == ['b', 'a', 'c']
    assert lists_fluency_dict_order_deduplicate([]) == []
    assert ((_practice_1_0 := ['', 'A', 'a', '']), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := lists_fluency_dict_order_deduplicate(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['', 'A', 'a']
