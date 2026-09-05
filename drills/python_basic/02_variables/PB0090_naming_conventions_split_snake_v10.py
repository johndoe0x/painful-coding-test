"""
PB0090 — snake_case 읽기

Chapter: Variables
Topic: Naming Conventions
Seed: 09 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
밑줄로 식별자를 나누고 빈 조각은 제외한 단어 리스트를 반환하세요.

연습 초점
---------
snake_case 구성 요소 이해

구현할 함수
-----------
def split_snake_case(identifier: str) -> list[str]:

예시 및 필수 테스트
-------------------
- split_snake_case('first_user_name') == ['first', 'user', 'name']
- split_snake_case('') == []
- split_snake_case('_a__b_') == ['a', 'b']

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0090 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def split_snake_case(identifier: str) -> list[str]:
    raise NotImplementedError("TODO: PB0090")


def self_test() -> None:
    assert split_snake_case('first_user_name') == ['first', 'user', 'name']
    assert split_snake_case('') == []
    assert split_snake_case('_a__b_') == ['a', 'b']
