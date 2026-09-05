"""
PB0086 — 안전한 변수명 정리

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞뒤 공백을 제거하고 소문자로 바꾼 뒤 공백과 하이픈을 밑줄로 바꾸세요.

연습 초점
---------
일관된 변수명 정규화

구현할 함수
-----------
def sanitize_identifier(text: str) -> str:

예시 및 필수 테스트
-------------------
- sanitize_identifier(' User-Name ') == 'user_name'
- sanitize_identifier('') == ''
- sanitize_identifier('A B-C') == 'a_b_c'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0086 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def sanitize_identifier(text: str) -> str:
    raise NotImplementedError("TODO: PB0086")


def self_test() -> None:
    assert sanitize_identifier(' User-Name ') == 'user_name'
    assert sanitize_identifier('') == ''
    assert sanitize_identifier('A B-C') == 'a_b_c'
