"""
PB0005 — 인사말 반복

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
'Hello, world!'를 count개 담은 리스트를 반환하세요. count가 0이면 빈 리스트입니다.

연습 초점
---------
정해진 횟수만큼 값 만들기

구현할 함수
-----------
def repeat_hello(count: int) -> list[str]:

예시 및 필수 테스트
-------------------
- repeat_hello(3) == ['Hello, world!', 'Hello, world!', 'Hello, world!']
- repeat_hello(0) == []
- repeat_hello(1) == ['Hello, world!']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0005 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_hello(count: int) -> list[str]:
    raise NotImplementedError("TODO: PB0005")


def self_test() -> None:
    assert repeat_hello(3) == ['Hello, world!', 'Hello, world!', 'Hello, world!']
    assert repeat_hello(0) == []
    assert repeat_hello(1) == ['Hello, world!']
