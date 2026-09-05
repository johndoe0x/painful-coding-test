"""
CI0015 — 숫자 문자열 정렬 — 반복 세트 1

Chapter: Sorting
Seed: 01 / 40
Variant: 15 / 20
Time cap: 240 seconds
Source checks: sorted_call

문제
----
정수로 변환한 값을 기준으로 오름차순 정렬하되 같은 숫자는 입력 순서를 보존하세요. 이 파일은 Sorting 챕터의 반복 세트 1이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
표현과 정렬 key 분리

구현할 함수
-----------
def sorting_r01_numeric_text(texts: list[str]) -> list[str]:

필수 구현 방식
--------------
- sorted()를 사용한다.

예시 및 필수 테스트
-------------------
- sorting_r01_numeric_text(['10', '2', '-1']) == ['-1', '2', '10']
- sorting_r01_numeric_text(['02', '2', '1']) == ['1', '02', '2']
- sorting_r01_numeric_text([]) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0015 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def sorting_r01_numeric_text(texts: list[str]) -> list[str]:
    raise NotImplementedError("TODO: CI0015")


def self_test() -> None:
    assert sorting_r01_numeric_text(['10', '2', '-1']) == ['-1', '2', '10']
    assert sorting_r01_numeric_text(['02', '2', '1']) == ['1', '02', '2']
    assert sorting_r01_numeric_text([]) == []
