"""
PB0555 — 첫 부분 문자열만 바꾸기

Chapter: Strings
Topic: Strings are Immutable
Seed: 56 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
old가 비어 있지 않다고 가정하고 처음 등장한 old만 new로 바꾸며, 없으면 text를 그대로 반환한다.

연습 초점
---------
원본 변경 없이 첫 일치 위치를 기준으로 새 문자열을 만든다.

구현할 함수
-----------
def replace_first_substring(text: str, old: str, new: str) -> str:

예시 및 필수 테스트
-------------------
- replace_first_substring('one one', 'one', 'two') == 'two one'
- replace_first_substring('banana', 'na', 'X') == 'baXna'
- replace_first_substring('abc', 'z', '!') == 'abc'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0555 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_first_substring(text: str, old: str, new: str) -> str:
    raise NotImplementedError("TODO: PB0555")


def self_test() -> None:
    assert replace_first_substring('one one', 'one', 'two') == 'two one'
    assert replace_first_substring('banana', 'na', 'X') == 'baXna'
    assert replace_first_substring('abc', 'z', '!') == 'abc'
