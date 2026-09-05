"""
PB0143 — 숫자를 문장에 넣기

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
age 때문에 문자열 결합 오류가 나지 않도록 '<name> is <age> years old.'를 반환하세요.

연습 초점
---------
숫자를 문자열 문맥으로 변환

구현할 함수
-----------
def format_age_sentence(name: str, age: int) -> str:

예시 및 필수 테스트
-------------------
- format_age_sentence('Ada', 36) == 'Ada is 36 years old.'
- format_age_sentence('', 0) == ' is 0 years old.'
- format_age_sentence('A', -1) == 'A is -1 years old.'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0143 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_age_sentence(name: str, age: int) -> str:
    raise NotImplementedError("TODO: PB0143")


def self_test() -> None:
    assert format_age_sentence('Ada', 36) == 'Ada is 36 years old.'
    assert format_age_sentence('', 0) == ' is 0 years old.'
    assert format_age_sentence('A', -1) == 'A is -1 years old.'
