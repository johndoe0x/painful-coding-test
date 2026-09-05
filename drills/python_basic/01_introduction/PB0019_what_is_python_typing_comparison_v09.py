"""
PB0019 — 타입 방식 비교

Chapter: Introduction
Topic: What is Python?
Seed: 02 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 딕셔너리의 typing 값이 같으면 True를 반환하세요. 키가 없으면 빈 문자열로 취급하세요.

연습 초점
---------
딕셔너리 기본값과 값 비교

구현할 함수
-----------
def compare_typing_style(left: dict[str, str], right: dict[str, str]) -> bool:

예시 및 필수 테스트
-------------------
- compare_typing_style({'typing': 'dynamic'}, {'typing': 'dynamic'}) is True
- compare_typing_style({}, {}) is True
- compare_typing_style({'typing': 'dynamic'}, {'typing': 'static'}) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0019 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def compare_typing_style(left: dict[str, str], right: dict[str, str]) -> bool:
    raise NotImplementedError("TODO: PB0019")


def self_test() -> None:
    assert compare_typing_style({'typing': 'dynamic'}, {'typing': 'dynamic'}) is True
    assert compare_typing_style({}, {}) is True
    assert compare_typing_style({'typing': 'dynamic'}, {'typing': 'static'}) is False
