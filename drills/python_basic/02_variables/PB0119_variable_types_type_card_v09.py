"""
PB0119 — 값의 타입 카드

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
value와 실제 타입 이름을 {'value': value, 'type': 이름}으로 반환하세요.

연습 초점
---------
값과 타입 메타데이터 함께 표현

구현할 함수
-----------
def make_type_card(value: object) -> dict[str, object]:

예시 및 필수 테스트
-------------------
- make_type_card(3) == {'value': 3, 'type': 'int'}
- make_type_card('') == {'value': '', 'type': 'str'}
- make_type_card(None) == {'value': None, 'type': 'NoneType'}

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0119 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def make_type_card(value: object) -> dict[str, object]:
    raise NotImplementedError("TODO: PB0119")


def self_test() -> None:
    assert make_type_card(3) == {'value': 3, 'type': 'int'}
    assert make_type_card('') == {'value': '', 'type': 'str'}
    assert make_type_card(None) == {'value': None, 'type': 'NoneType'}
