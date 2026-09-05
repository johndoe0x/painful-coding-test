"""
PB0133 — 텍스트를 bool로

Chapter: Variables
Topic: Type Casting
Seed: 14 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
앞뒤 공백과 대소문자를 무시해 'true'와 '1'이면 True, 그 외에는 False를 반환하세요.

연습 초점
---------
문자열 규칙에 따른 bool 변환

구현할 함수
-----------
def cast_boolean_text(text: str) -> bool:

예시 및 필수 테스트
-------------------
- cast_boolean_text(' TRUE ') is True
- cast_boolean_text('') is False
- cast_boolean_text('0') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0133 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def cast_boolean_text(text: str) -> bool:
    raise NotImplementedError("TODO: PB0133")


def self_test() -> None:
    assert cast_boolean_text(' TRUE ') is True
    assert cast_boolean_text('') is False
    assert cast_boolean_text('0') is False
