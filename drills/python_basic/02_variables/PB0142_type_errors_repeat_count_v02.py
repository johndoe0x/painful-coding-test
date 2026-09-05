"""
PB0142 — 문자열 반복 횟수 변환

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
count_text를 int로 변환한 뒤 text를 그 횟수만큼 반복하세요.

연습 초점
---------
str과 int가 필요한 연산 구분

구현할 함수
-----------
def repeat_with_text_count(text: str, count_text: str) -> str:

예시 및 필수 테스트
-------------------
- repeat_with_text_count('ab', '3') == 'ababab'
- repeat_with_text_count('x', '0') == ''
- repeat_with_text_count('', '5') == ''

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0142 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def repeat_with_text_count(text: str, count_text: str) -> str:
    raise NotImplementedError("TODO: PB0142")


def self_test() -> None:
    assert repeat_with_text_count('ab', '3') == 'ababab'
    assert repeat_with_text_count('x', '0') == ''
    assert repeat_with_text_count('', '5') == ''
