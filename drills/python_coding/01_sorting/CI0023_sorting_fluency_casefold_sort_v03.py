"""
CI0023 — 대소문자 무시 key와 원래 표기

Chapter: Sorting
Seed: 02 / 40
Variant: 03 / 20
Time cap: 150 seconds
Source checks: sorted_call

문제
----
sorted의 key에 str.casefold를 사용하세요. key가 같으면 입력 순서를 유지하고 원래 표기로 반환합니다. 입력은 보존합니다. 입력 컬렉션은 각각 1,000개 이하입니다.

연습 초점
---------
정렬 key와 반환 원소 분리

구현할 함수
-----------
def sorting_fluency_casefold_sort(words: list[str]) -> list[str]:

필수 구현 방식
--------------
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_fluency_casefold_sort(['b', 'A', 'a', 'B']) == ['A', 'a', 'b', 'B']
- sorting_fluency_casefold_sort([]) == []
- ((_practice_1_0 := ['SS', 'ß', 'ss', 'a']), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_casefold_sort(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['a', 'SS', 'ß', 'ss']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0023 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_fluency_casefold_sort(words: list[str]) -> list[str]:
    raise NotImplementedError("TODO: CI0023")


def self_test() -> None:
    assert sorting_fluency_casefold_sort(['b', 'A', 'a', 'B']) == ['A', 'a', 'b', 'B']
    assert sorting_fluency_casefold_sort([]) == []
    assert ((_practice_1_0 := ['SS', 'ß', 'ss', 'a']), (_practice_1_before := repr((_practice_1_0,))), (_practice_1_result := sorting_fluency_casefold_sort(_practice_1_0)), _practice_1_result if repr((_practice_1_0,)) == _practice_1_before else object())[-1] == ['a', 'SS', 'ß', 'ss']
