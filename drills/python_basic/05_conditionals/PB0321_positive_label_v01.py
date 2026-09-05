"""
PB0321 — 양수 라벨

Chapter: Conditional Statements
Topic: If Statements
Seed: 33 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks: if

문제
----
기본 결과를 빈 문자열로 두고 number가 양수일 때만 'positive'로 바꿔 반환한다.

연습 초점
---------
단일 if가 실행되는 조건

구현할 함수
-----------
def positive_label(number: int) -> str:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- positive_label(3) == 'positive'
- positive_label(0) == ''
- positive_label(-2) == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0321 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def positive_label(number: int) -> str:
    raise NotImplementedError("TODO: PB0321")


def self_test() -> None:
    assert positive_label(3) == 'positive'
    assert positive_label(0) == ''
    assert positive_label(-2) == ''
