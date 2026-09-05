"""
PB0011 — Python 핵심 정보

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
Python의 언어 이름과 동적 타입 특성을 {'language': 'Python', 'typing': 'dynamic'}으로 반환하세요.

연습 초점
---------
딕셔너리 리터럴과 핵심 용어

구현할 함수
-----------
def python_summary() -> dict[str, str]:

예시 및 필수 테스트
-------------------
- python_summary() == {'language': 'Python', 'typing': 'dynamic'}
- python_summary()['language'] == 'Python'
- set(python_summary()) == {'language', 'typing'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0011 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def python_summary() -> dict[str, str]:
    raise NotImplementedError("TODO: PB0011")


def self_test() -> None:
    assert python_summary() == {'language': 'Python', 'typing': 'dynamic'}
    assert python_summary()['language'] == 'Python'
    assert set(python_summary()) == {'language', 'typing'}
