"""
CI0094 — 자연스러운 코드 정렬 — 반복 세트 5

Chapter: Sorting
Seed: 05 / 40
Variant: 14 / 20
Time cap: 240 seconds
Source checks: re_call, sorted_call

문제
----
re로 각 문자열의 마지막 연속 숫자를 추출해 숫자 오름차순, 동률이면 문자열순으로 정렬하세요. 숫자가 없으면 0입니다. 이 파일은 Sorting 챕터의 반복 세트 5이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
정규표현식 추출과 자연 정렬 key

구현할 함수
-----------
def sorting_r05_natural_codes(codes: list[str]) -> list[str]:

필수 구현 방식
--------------
- re 모듈의 정규표현식 API를 사용한다.
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r05_natural_codes(['item10', 'item2', 'item1']) == ['item1', 'item2', 'item10']
- sorting_r05_natural_codes(['b', 'a']) == ['a', 'b']
- sorting_r05_natural_codes([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0094 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r05_natural_codes(codes: list[str]) -> list[str]:
    raise NotImplementedError("TODO: CI0094")


def self_test() -> None:
    assert sorting_r05_natural_codes(['item10', 'item2', 'item1']) == ['item1', 'item2', 'item10']
    assert sorting_r05_natural_codes(['b', 'a']) == ['a', 'b']
    assert sorting_r05_natural_codes([]) == []
