"""
PB0551 — 한 글자를 바꾼 새 문자열

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 유효하고 replacement가 한 글자라고 가정해 해당 위치만 바꾼 새 문자열을 반환한다.

연습 초점
---------
문자열은 수정할 수 없으므로 앞·대체 글자·뒤를 재결합한다.

구현할 함수
-----------
def replace_character(text: str, index: int, replacement: str) -> str:

예시 및 필수 테스트
-------------------
- replace_character('cat', 0, 'b') == 'bat'
- replace_character('code', 2, 'v') == 'cove'
- replace_character('A', 0, 'Z') == 'Z'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0551 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_character(text: str, index: int, replacement: str) -> str:
    raise NotImplementedError("TODO: PB0551")


def self_test() -> None:
    assert replace_character('cat', 0, 'b') == 'bat'
    assert replace_character('code', 2, 'v') == 'cove'
    assert replace_character('A', 0, 'Z') == 'Z'
