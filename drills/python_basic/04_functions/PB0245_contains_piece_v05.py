"""
PB0245 — 부분 문자열 확인

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
piece가 text 안에 포함되는지 반환한다.

연습 초점
---------
대상과 검색어 매개변수 전달

구현할 함수
-----------
def contains_piece(text: str, piece: str) -> bool:

예시 및 필수 테스트
-------------------
- contains_piece('notebook', 'book') is True
- contains_piece('python', 'java') is False
- contains_piece('', '') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0245 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def contains_piece(text: str, piece: str) -> bool:
    raise NotImplementedError("TODO: PB0245")


def self_test() -> None:
    assert contains_piece('notebook', 'book') is True
    assert contains_piece('python', 'java') is False
    assert contains_piece('', '') is True
