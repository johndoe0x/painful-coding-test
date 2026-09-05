"""
PB0014 — 언어 사실 만들기

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 입력을 language와 typing 키에 담은 딕셔너리를 반환하세요.

연습 초점
---------
키가 명확한 딕셔너리 구성

구현할 함수
-----------
def build_language_fact(language: str, typing_style: str) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- build_language_fact('Python', 'dynamic') == {'language': 'Python', 'typing': 'dynamic'}
- build_language_fact('', '') == {'language': '', 'typing': ''}
- build_language_fact('C', 'static') == {'language': 'C', 'typing': 'static'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0014 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def build_language_fact(language: str, typing_style: str) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0014")


def self_test() -> None:
    assert build_language_fact('Python', 'dynamic') == {'language': 'Python', 'typing': 'dynamic'}
    assert build_language_fact('', '') == {'language': '', 'typing': ''}
    assert build_language_fact('C', 'static') == {'language': 'C', 'typing': 'static'}
