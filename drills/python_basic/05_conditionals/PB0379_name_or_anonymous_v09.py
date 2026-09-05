"""
PB0379 — 익명 이름 대체

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: if

문제
----
name이 truthy면 앞뒤 공백을 제거해 반환하고, falsy면 'anonymous'를 반환한다.

연습 초점
---------
조건 평가 뒤 값 정규화

구현할 함수
-----------
def name_or_anonymous(name: str | None) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- name_or_anonymous(' Ada ') == 'Ada'
- name_or_anonymous('') == 'anonymous'
- name_or_anonymous(None) == 'anonymous'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0379 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def name_or_anonymous(name: str | None) -> str:
    raise NotImplementedError("TODO: PB0379")


def self_test() -> None:
    assert name_or_anonymous(' Ada ') == 'Ada'
    assert name_or_anonymous('') == 'anonymous'
    assert name_or_anonymous(None) == 'anonymous'
