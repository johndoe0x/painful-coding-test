"""
PB0696 — 중첩 프로필 생성

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
name과 address 딕셔너리를 가진 중첩 프로필을 반환한다. address에는 city와 country를 넣는다.

연습 초점
---------
중첩 딕셔너리 구성

구현할 함수
-----------
def dict_nested_profile(name: str, city: str, country: str) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- dict_nested_profile('Ada', 'London', 'UK') == {'name': 'Ada', 'address': {'city': 'London', 'country': 'UK'}}
- dict_nested_profile('', '', '') == {'name': '', 'address': {'city': '', 'country': ''}}
- dict_nested_profile('Kim', 'Seoul', 'KR') == {'name': 'Kim', 'address': {'city': 'Seoul', 'country': 'KR'}}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0696 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_nested_profile(name: str, city: str, country: str) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0696")


def self_test() -> None:
    assert dict_nested_profile('Ada', 'London', 'UK') == {'name': 'Ada', 'address': {'city': 'London', 'country': 'UK'}}
    assert dict_nested_profile('', '', '') == {'name': '', 'address': {'city': '', 'country': ''}}
    assert dict_nested_profile('Kim', 'Seoul', 'KR') == {'name': 'Kim', 'address': {'city': 'Seoul', 'country': 'KR'}}
