"""
PB0482 — 안전하게 글자 읽기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
index가 text의 유효한 양수 또는 음수 인덱스면 해당 글자를, 아니면 default를 반환한다.

연습 초점
---------
문자열 인덱스의 양수·음수 유효 범위를 직접 판단한다.

구현할 함수
-----------
def character_or(text: str, index: int, default: str) -> str:

예시 및 필수 테스트
-------------------
- character_or('python', 2, '?') == 't'
- character_or('python', -1, '?') == 'n'
- character_or('python', 8, '?') == '?'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0482 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def character_or(text: str, index: int, default: str) -> str:
    raise NotImplementedError("TODO: PB0482")


def self_test() -> None:
    assert character_or('python', 2, '?') == 't'
    assert character_or('python', -1, '?') == 'n'
    assert character_or('python', 8, '?') == '?'
