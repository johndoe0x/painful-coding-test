"""
PB0710 — bool 설정 반전

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 key의 bool 값을 반전한다. 없는 key는 False로 본 뒤 True로 추가한다.

연습 초점
---------
get 기본값, 논리 부정, 갱신

구현할 함수
-----------
def dict_toggle_flag(settings: dict[str, bool], key: str) -> dict[str, bool]:

예시 및 필수 테스트
-------------------
- ((items := {'dark': True}), dict_toggle_flag(items, 'dark') == {'dark': False} and items == {'dark': True})[-1] is True
- dict_toggle_flag({}, 'dark') == {'dark': True}
- dict_toggle_flag({'a': False}, 'b') == {'a': False, 'b': True}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0710 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_toggle_flag(settings: dict[str, bool], key: str) -> dict[str, bool]:
    raise NotImplementedError("TODO: PB0710")


def self_test() -> None:
    assert ((items := {'dark': True}), dict_toggle_flag(items, 'dark') == {'dark': False} and items == {'dark': True})[-1] is True
    assert dict_toggle_flag({}, 'dark') == {'dark': True}
    assert dict_toggle_flag({'a': False}, 'b') == {'a': False, 'b': True}
