"""
PB0492 — 문자 코드 합계

Chapter: Strings
Topic: String Looping
Seed: 50 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks: for

문제
----
text의 모든 문자 ord 값을 순회해 합산한다.

연습 초점
---------
문자 단위 반복과 정수 누적 변수를 사용한다.

구현할 함수
-----------
def codepoint_total(text: str) -> int:

필수 구현 방식
--------------
- for문을 사용한다.

예시 및 필수 테스트
-------------------
- codepoint_total('AB') == 131
- codepoint_total('a') == 97
- codepoint_total('') == 0

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0492 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def codepoint_total(text: str) -> int:
    raise NotImplementedError("TODO: PB0492")


def self_test() -> None:
    assert codepoint_total('AB') == 131
    assert codepoint_total('a') == 97
    assert codepoint_total('') == 0
