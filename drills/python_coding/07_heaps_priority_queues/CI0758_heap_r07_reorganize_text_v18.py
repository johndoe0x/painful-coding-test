"""
CI0758 — 인접 중복 없는 문자열 — 반복 세트 7

Chapter: Heaps / Priority Queues
Seed: 38 / 40
Variant: 18 / 20
Time cap: 300 seconds
Source checks: heapq_call, counter_call

문제
----
Counter와 max heap으로 같은 문자가 인접하지 않는 문자열을 만들고 불가능하면 ''를 반환하세요. 동률이면 문자순을 사용하세요. 이 파일은 Heaps / Priority Queues 챕터의 반복 세트 7이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
빈도 max heap과 이전 문자 보류

구현할 함수
-----------
def heap_r07_reorganize_text(text: str) -> str:

필수 구현 방식
--------------
- heapq API를 사용한다.
- collections.Counter를 사용한다.

예시 및 필수 테스트
-------------------
- heap_r07_reorganize_text('aab') == 'aba'
- heap_r07_reorganize_text('aaab') == ''
- heap_r07_reorganize_text('') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0758 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def heap_r07_reorganize_text(text: str) -> str:
    raise NotImplementedError("TODO: CI0758")


def self_test() -> None:
    assert heap_r07_reorganize_text('aab') == 'aba'
    assert heap_r07_reorganize_text('aaab') == ''
    assert heap_r07_reorganize_text('') == ''
