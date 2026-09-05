"""
PB0691 — 사용자 딕셔너리

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 01 / 10
Time cap: 60 seconds
Source checks:

문제
----
name과 age key를 가진 딕셔너리를 반환한다.

연습 초점
---------
딕셔너리 리터럴 생성

구현할 함수
-----------
def make_user(name: str, age: int) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- make_user('Ada', 36) == {'name': 'Ada', 'age': 36}
- make_user('', 0) == {'name': '', 'age': 0}
- make_user('Kim', 1) == {'name': 'Kim', 'age': 1}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0691 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_user(name: str, age: int) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0691")


def self_test() -> None:
    assert make_user('Ada', 36) == {'name': 'Ada', 'age': 36}
    assert make_user('', 0) == {'name': '', 'age': 0}
    assert make_user('Kim', 1) == {'name': 'Kim', 'age': 1}
