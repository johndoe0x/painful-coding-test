"""
PB0695 — 선택 전화번호가 있는 연락처

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
항상 name을 넣고 phone이 None이 아닐 때만 phone key를 추가한다.

연습 초점
---------
조건부 key 추가

구현할 함수
-----------
def dict_contact_card(name: str, phone: str | None) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- dict_contact_card('Ada', '010') == {'name': 'Ada', 'phone': '010'}
- dict_contact_card('Ada', None) == {'name': 'Ada'}
- dict_contact_card('', '') == {'name': '', 'phone': ''}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0695 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_contact_card(name: str, phone: str | None) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0695")


def self_test() -> None:
    assert dict_contact_card('Ada', '010') == {'name': 'Ada', 'phone': '010'}
    assert dict_contact_card('Ada', None) == {'name': 'Ada'}
    assert dict_contact_card('', '') == {'name': '', 'phone': ''}
