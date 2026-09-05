"""
PB0268 — 예·아니오 변환 반환

Chapter: Functions
Topic: Return Statement
Seed: 27 / 82
Variant: 08 / 10
Time cap: 120 seconds
Source checks:

문제
----
대소문자를 무시해 yes는 True, no는 False, 나머지는 None을 반환한다.

연습 초점
---------
세 가지 반환 경로 설계

구현할 함수
-----------
def parse_yes_no(text: str) -> bool | None:

예시 및 필수 테스트
-------------------
- parse_yes_no('YES') is True
- parse_yes_no('no') is False
- parse_yes_no('maybe') is None

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0268 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def parse_yes_no(text: str) -> bool | None:
    raise NotImplementedError("TODO: PB0268")


def self_test() -> None:
    assert parse_yes_no('YES') is True
    assert parse_yes_no('no') is False
    assert parse_yes_no('maybe') is None
