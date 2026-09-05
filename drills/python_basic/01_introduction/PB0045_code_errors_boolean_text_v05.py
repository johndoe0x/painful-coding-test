"""
PB0045 — 문자열 truthiness 오류 고치기

Chapter: Introduction
Topic: Code Errors
Seed: 05 / 82
Variant: 05 / 10
Time cap: 120 seconds
Source checks:

문제
----
starter는 bool(text)를 사용해 비어 있지 않은 모든 문자열을 True로 봅니다. strip과 소문자화를 적용한 내용이 정확히 'true'일 때만 True를 반환하세요.

연습 초점
---------
문자열의 존재 여부와 문자열이 표현하는 불리언 의미 구분

구현할 함수
-----------
def corrected_boolean(text: str) -> bool:

예시 및 필수 테스트
-------------------
- corrected_boolean('True') is True
- corrected_boolean('') is False
- corrected_boolean(' FALSE ') is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0045 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def corrected_boolean(text: str) -> bool:
    return bool(text)


def self_test() -> None:
    assert corrected_boolean('True') is True
    assert corrected_boolean('') is False
    assert corrected_boolean(' FALSE ') is False
