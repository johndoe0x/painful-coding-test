"""
PB0483 — 두 번째 글자 읽기

Chapter: Strings
Topic: String Indexing
Seed: 49 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
text에 글자가 두 개 이상이면 두 번째 글자를, 아니면 None을 반환한다.

연습 초점
---------
길이를 먼저 확인한 뒤 고정 인덱스 1에 접근한다.

구현할 함수
-----------
def second_character(text: str) -> str | None:

예시 및 필수 테스트
-------------------
- second_character('cat') == 'a'
- second_character('x') is None
- second_character('') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0483 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def second_character(text: str) -> str | None:
    raise NotImplementedError("TODO: PB0483")


def self_test() -> None:
    assert second_character('cat') == 'a'
    assert second_character('x') is None
    assert second_character('') is None
