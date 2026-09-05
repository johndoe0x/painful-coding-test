"""
PB0706 — 없는 key만 설정

Chapter: Dictionaries
Topic: Dict Operations
Seed: 71 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks:

문제
----
원본을 바꾸지 않고 key가 없을 때만 value를 추가한다.

연습 초점
---------
setdefault 또는 조건부 할당

구현할 함수
-----------
def dict_set_if_absent(mapping: dict[str, str], key: str, value: str) -> dict[str, str]:

예시 및 필수 테스트
-------------------
- dict_set_if_absent({'a': 'old'}, 'a', 'new') == {'a': 'old'}
- ((items := {}), dict_set_if_absent(items, 'a', 'new') == {'a': 'new'} and items == {})[-1] is True
- dict_set_if_absent({'x': ''}, 'x', 'v') == {'x': ''}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0706 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def dict_set_if_absent(mapping: dict[str, str], key: str, value: str) -> dict[str, str]:
    raise NotImplementedError("TODO: PB0706")


def self_test() -> None:
    assert dict_set_if_absent({'a': 'old'}, 'a', 'new') == {'a': 'old'}
    assert ((items := {}), dict_set_if_absent(items, 'a', 'new') == {'a': 'new'} and items == {})[-1] is True
    assert dict_set_if_absent({'x': ''}, 'x', 'v') == {'x': ''}
