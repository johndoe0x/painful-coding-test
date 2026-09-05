"""
PB0426 — 시작 위치 이후 치환

Chapter: Loops
Topic: For Loops Start
Seed: 43 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: for, range

문제
----
0 <= start <= len(text)라고 가정합니다. start 전 문자는 유지하고 for와 range(start, len(text))로 이후 각 문자를 replacement로 바꾼 문자열을 반환한다.

연습 초점
---------
유효한 start 경계부터 결과 구성

구현할 함수
-----------
def replace_from_index(text: str, start: int, replacement: str) -> str:

필수 구현 방식
--------------
- for문을 사용한다.
- range()를 사용한다.

예시 및 필수 테스트
-------------------
- replace_from_index('abcdef', 3, '*') == 'abc***'
- replace_from_index('abc', 3, '*') == 'abc'
- replace_from_index('', 0, 'x') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0426 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def replace_from_index(text: str, start: int, replacement: str) -> str:
    raise NotImplementedError("TODO: PB0426")


def self_test() -> None:
    assert replace_from_index('abcdef', 3, '*') == 'abc***'
    assert replace_from_index('abc', 3, '*') == 'abc'
    assert replace_from_index('', 0, 'x') == ''
