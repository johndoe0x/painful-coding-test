"""
PB0089 — 내부용 이름 표시

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
name의 기존 선행 밑줄을 제거하고 소문자로 바꾼 뒤 밑줄 하나를 앞에 붙이세요.

연습 초점
---------
비공개 용도를 나타내는 선행 밑줄

구현할 함수
-----------
def private_variable_name(name: str) -> str:

예시 및 필수 테스트
-------------------
- private_variable_name('Cache') == '_cache'
- private_variable_name('') == '_'
- private_variable_name('__TOKEN') == '_token'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0089 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def private_variable_name(name: str) -> str:
    raise NotImplementedError("TODO: PB0089")


def self_test() -> None:
    assert private_variable_name('Cache') == '_cache'
    assert private_variable_name('') == '_'
    assert private_variable_name('__TOKEN') == '_token'
