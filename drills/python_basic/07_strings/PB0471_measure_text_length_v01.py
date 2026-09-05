"""
PB0471 — 문자열 길이 재기

Chapter: Strings
Topic: Length Function
Seed: 48 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
text에 들어 있는 문자의 개수를 반환한다.

연습 초점
---------
len으로 빈 문자열과 유니코드 문자열의 길이를 일관되게 구한다.

구현할 함수
-----------
def string_length(text: str) -> int:

예시 및 필수 테스트
-------------------
- string_length('python') == 6
- string_length('') == 0
- string_length('한글!') == 3

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0471 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def string_length(text: str) -> int:
    raise NotImplementedError("TODO: PB0471")


def self_test() -> None:
    assert string_length('python') == 6
    assert string_length('') == 0
    assert string_length('한글!') == 3
