"""
PB0032 — 이름표 한 줄

Chapter: Introduction
Topic: Printing Text
Seed: 04 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
'[<role>] <name>' 형식의 이름표를 반환하세요.

연습 초점
---------
여러 값을 한 줄에 배치

구현할 함수
-----------
def format_name_badge(name: str, role: str) -> str:

예시 및 필수 테스트
-------------------
- format_name_badge('Ada', 'Admin') == '[Admin] Ada'
- format_name_badge('', '') == '[] '
- format_name_badge('Lin', 'User') == '[User] Lin'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0032 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def format_name_badge(name: str, role: str) -> str:
    raise NotImplementedError("TODO: PB0032")


def self_test() -> None:
    assert format_name_badge('Ada', 'Admin') == '[Admin] Ada'
    assert format_name_badge('', '') == '[] '
    assert format_name_badge('Lin', 'User') == '[User] Lin'
