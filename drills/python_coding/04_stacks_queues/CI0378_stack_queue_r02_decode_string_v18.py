"""
CI0378 — 반복 문자열 해독 — 반복 세트 2

Chapter: Stacks and Queues
Seed: 19 / 40
Variant: 18 / 20
Time cap: 240 seconds
Source checks: append_call, pop_call

문제
----
k[encoded] 중첩 형식의 문자열을 stack으로 해독하세요. k는 양의 정수입니다. 이 파일은 Stacks and Queues 챕터의 반복 세트 2이며, 같은 핵심 알고리즘을 다른 날 다시 재구현하는 문제입니다.

연습 초점
---------
중첩 상태 stack

구현할 함수
-----------
def stack_queue_r02_decode_string(text: str) -> str:

필수 구현 방식
--------------
- list.append()를 사용한다.
- list.pop()을 사용한다.

예시 및 필수 테스트
-------------------
- stack_queue_r02_decode_string('3[a2[c]]') == 'accaccacc'
- stack_queue_r02_decode_string('2[ab]') == 'abab'
- stack_queue_r02_decode_string('x') == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert를 모두 통과하고 필수 구현 방식을 지킨다.
3. 필요한 표준 라이브러리 import를 직접 작성한다.
4. 입력별 정답을 if문으로 나열하지 않는다.
5. 파일 마지막에 시간·공간복잡도를 주석으로 적는다.
6. 저장소 루트에서 `python3 -B -m python_coding CI0378 --strict`를 실행한다.
7. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


from __future__ import annotations


def stack_queue_r02_decode_string(text: str) -> str:
    raise NotImplementedError("TODO: CI0378")


def self_test() -> None:
    assert stack_queue_r02_decode_string('3[a2[c]]') == 'accaccacc'
    assert stack_queue_r02_decode_string('2[ab]') == 'abab'
    assert stack_queue_r02_decode_string('x') == 'x'
