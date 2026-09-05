"""
PB0250 — 이름과 나이 서식

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
이름과 나이를 '<name> (<age>)' 형식으로 반환한다.

연습 초점
---------
서로 다른 타입의 매개변수 사용

구현할 함수
-----------
def format_person_age(name: str, age: int) -> str:

예시 및 필수 테스트
-------------------
- format_person_age('Ada', 36) == 'Ada (36)'
- format_person_age('', 0) == ' (0)'
- format_person_age('Kim', 100) == 'Kim (100)'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0250 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_person_age(name: str, age: int) -> str:
    raise NotImplementedError("TODO: PB0250")


def self_test() -> None:
    assert format_person_age('Ada', 36) == 'Ada (36)'
    assert format_person_age('', 0) == ' (0)'
    assert format_person_age('Kim', 100) == 'Kim (100)'
