"""
PB0013 — 동적 타입 판별

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
typing_style의 앞뒤 공백과 대소문자를 무시했을 때 'dynamic'이면 True를 반환하세요.

연습 초점
---------
문자열 정규화와 개념 판별

구현할 함수
-----------
def is_dynamic_typing(typing_style: str) -> bool:

예시 및 필수 테스트
-------------------
- is_dynamic_typing('dynamic') is True
- is_dynamic_typing(' Static ') is False
- is_dynamic_typing('DYNAMIC') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0013 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_dynamic_typing(typing_style: str) -> bool:
    raise NotImplementedError("TODO: PB0013")


def self_test() -> None:
    assert is_dynamic_typing('dynamic') is True
    assert is_dynamic_typing(' Static ') is False
    assert is_dynamic_typing('DYNAMIC') is True
