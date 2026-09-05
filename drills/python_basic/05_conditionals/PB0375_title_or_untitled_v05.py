"""
PB0375 — 제목 기본 문자열

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks: if

문제
----
title이 truthy면 그대로, 빈 문자열이나 None이면 'Untitled'을 반환한다.

연습 초점
---------
문자열의 truthiness

구현할 함수
-----------
def title_or_untitled(title: str | None) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- title_or_untitled('Report') == 'Report'
- title_or_untitled('') == 'Untitled'
- title_or_untitled(None) == 'Untitled'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0375 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def title_or_untitled(title: str | None) -> str:
    raise NotImplementedError("TODO: PB0375")


def self_test() -> None:
    assert title_or_untitled('Report') == 'Report'
    assert title_or_untitled('') == 'Untitled'
    assert title_or_untitled(None) == 'Untitled'
