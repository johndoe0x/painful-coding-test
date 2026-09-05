"""
PB0580 — 참·거짓 패턴 리스트

Chapter: Lists
Topic: Intro to Lists
Seed: 58 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
length가 0 이상이라고 가정해 인덱스 0부터 짝수 위치는 True, 홀수 위치는 False인 리스트를 반환한다.

연습 초점
---------
리스트 원소의 위치에 따라 값을 생성한다.

구현할 함수
-----------
def boolean_pattern(length: int) -> list[bool]:

예시 및 필수 테스트
-------------------
- boolean_pattern(5) == [True, False, True, False, True]
- boolean_pattern(2) == [True, False]
- boolean_pattern(0) == []

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0580 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def boolean_pattern(length: int) -> list[bool]:
    raise NotImplementedError("TODO: PB0580")


def self_test() -> None:
    assert boolean_pattern(5) == [True, False, True, False, True]
    assert boolean_pattern(2) == [True, False]
    assert boolean_pattern(0) == []
