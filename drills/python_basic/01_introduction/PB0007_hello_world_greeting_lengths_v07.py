"""
PB0007 — 인사말 길이

Chapter: Introduction
Topic: Hello, World
Seed: 01 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
각 이름으로 만든 'Hello, <name>!' 문자열의 길이를 리스트로 반환하세요.

연습 초점
---------
문자열 생성 결과의 길이 계산

구현할 함수
-----------
def greeting_lengths(names: list[str]) -> list[int]:

예시 및 필수 테스트
-------------------
- greeting_lengths(['Ada', 'Bo']) == [11, 10]
- greeting_lengths([]) == []
- greeting_lengths(['']) == [8]

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0007 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def greeting_lengths(names: list[str]) -> list[int]:
    raise NotImplementedError("TODO: PB0007")


def self_test() -> None:
    assert greeting_lengths(['Ada', 'Bo']) == [11, 10]
    assert greeting_lengths([]) == []
    assert greeting_lengths(['']) == [8]
