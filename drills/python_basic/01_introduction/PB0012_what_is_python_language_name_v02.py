"""
PB0012 — 언어 이름 확인

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
프로그래밍 언어 이름 'Python'을 정확히 반환하세요.

연습 초점
---------
대소문자를 지킨 문자열 반환

구현할 함수
-----------
def python_language_name() -> str:

예시 및 필수 테스트
-------------------
- python_language_name() == 'Python'
- python_language_name().startswith('Py')
- len(python_language_name()) == 6

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0012 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def python_language_name() -> str:
    raise NotImplementedError("TODO: PB0012")


def self_test() -> None:
    assert python_language_name() == 'Python'
    assert python_language_name().startswith('Py')
    assert len(python_language_name()) == 6
