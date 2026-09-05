"""
PB0083 — kebab-case 바꾸기

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
하이픈을 밑줄로 바꿔 snake_case 모양으로 반환하세요.

연습 초점
---------
언어별 명명 관례 변환

구현할 함수
-----------
def kebab_to_snake(identifier: str) -> str:

예시 및 필수 테스트
-------------------
- kebab_to_snake('user-name') == 'user_name'
- kebab_to_snake('') == ''
- kebab_to_snake('a-b-c') == 'a_b_c'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0083 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def kebab_to_snake(identifier: str) -> str:
    raise NotImplementedError("TODO: PB0083")


def self_test() -> None:
    assert kebab_to_snake('user-name') == 'user_name'
    assert kebab_to_snake('') == ''
    assert kebab_to_snake('a-b-c') == 'a_b_c'
