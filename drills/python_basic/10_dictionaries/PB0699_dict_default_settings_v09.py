"""
PB0699 — 기본 설정 딕셔너리

Chapter: Dictionaries
Topic: Intro to Dictionaries
Seed: 70 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
theme과 notifications를 가진 설정 딕셔너리를 반환한다.

연습 초점
---------
기본 인자와 딕셔너리 value

구현할 함수
-----------
def dict_default_settings(theme: str = 'light', notifications: bool = True) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- dict_default_settings() == {'theme': 'light', 'notifications': True}
- dict_default_settings('dark') == {'theme': 'dark', 'notifications': True}
- dict_default_settings('dark', False) == {'theme': 'dark', 'notifications': False}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0699 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_default_settings(theme: str = 'light', notifications: bool = True) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0699")


def self_test() -> None:
    assert dict_default_settings() == {'theme': 'light', 'notifications': True}
    assert dict_default_settings('dark') == {'theme': 'dark', 'notifications': True}
    assert dict_default_settings('dark', False) == {'theme': 'dark', 'notifications': False}
