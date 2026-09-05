"""
PB0154 — 선택적 문자열 길이

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
text가 None이면 0, 아니면 빈 문자열을 포함해 실제 길이를 반환하세요.

연습 초점
---------
None 가드 후 안전한 연산

구현할 함수
-----------
def optional_text_length(text: str | None) -> int:

예시 및 필수 테스트
-------------------
- optional_text_length('abc') == 3
- optional_text_length(None) == 0
- optional_text_length('') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0154 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_text_length(text: str | None) -> int:
    raise NotImplementedError("TODO: PB0154")


def self_test() -> None:
    assert optional_text_length('abc') == 3
    assert optional_text_length(None) == 0
    assert optional_text_length('') == 0
