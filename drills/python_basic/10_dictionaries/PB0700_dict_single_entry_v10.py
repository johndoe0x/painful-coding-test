"""
PB0700 — 동적 key 한 개 만들기

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
주어진 key와 value 하나만 가진 딕셔너리를 반환한다.

연습 초점
---------
변수를 딕셔너리 key로 사용

구현할 함수
-----------
def dict_single_entry(key: str, value: object) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- dict_single_entry('score', 10) == {'score': 10}
- dict_single_entry('', None) == {'': None}
- dict_single_entry('active', False) == {'active': False}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0700 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_single_entry(key: str, value: object) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0700")


def self_test() -> None:
    assert dict_single_entry('score', 10) == {'score': 10}
    assert dict_single_entry('', None) == {'': None}
    assert dict_single_entry('active', False) == {'active': False}
