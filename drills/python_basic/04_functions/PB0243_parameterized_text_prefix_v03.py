"""
PB0243 — 접두부 길이 매개변수

Chapter: Functions
Topic: Parameters
Seed: 25 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
text의 앞에서 size글자를 반환한다.

연습 초점
---------
값 매개변수와 길이 매개변수 사용

구현할 함수
-----------
def take_text_prefix(text: str, size: int) -> str:

예시 및 필수 테스트
-------------------
- take_text_prefix('python', 3) == 'pyt'
- take_text_prefix('hi', 0) == ''
- take_text_prefix('hi', 5) == 'hi'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0243 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def take_text_prefix(text: str, size: int) -> str:
    raise NotImplementedError("TODO: PB0243")


def self_test() -> None:
    assert take_text_prefix('python', 3) == 'pyt'
    assert take_text_prefix('hi', 0) == ''
    assert take_text_prefix('hi', 5) == 'hi'
