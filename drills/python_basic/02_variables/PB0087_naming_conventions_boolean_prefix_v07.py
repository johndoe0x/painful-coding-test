"""
PB0087 — 불리언 이름 접두사

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
subject를 소문자로 바꾸고 공백을 밑줄로 바꾼 뒤 'is_'를 앞에 붙이세요.

연습 초점
---------
불리언 의도를 나타내는 is_ 관례

구현할 함수
-----------
def boolean_variable_name(subject: str) -> str:

예시 및 필수 테스트
-------------------
- boolean_variable_name('Active User') == 'is_active_user'
- boolean_variable_name('') == 'is_'
- boolean_variable_name('READY') == 'is_ready'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0087 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def boolean_variable_name(subject: str) -> str:
    raise NotImplementedError("TODO: PB0087")


def self_test() -> None:
    assert boolean_variable_name('Active User') == 'is_active_user'
    assert boolean_variable_name('') == 'is_'
    assert boolean_variable_name('READY') == 'is_ready'
