"""
PB0141 — 숫자 문자열 덧셈

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
문자열 연결이나 TypeError 없이 두 입력을 int로 변환해 더하세요.

연습 초점
---------
연산 전에 호환 타입으로 변환

구현할 함수
-----------
def add_numeric_strings(left: str, right: str) -> int:

예시 및 필수 테스트
-------------------
- add_numeric_strings('10', '5') == 15
- add_numeric_strings('0', '0') == 0
- add_numeric_strings('-2', '3') == 1

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0141 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def add_numeric_strings(left: str, right: str) -> int:
    raise NotImplementedError("TODO: PB0141")


def self_test() -> None:
    assert add_numeric_strings('10', '5') == 15
    assert add_numeric_strings('0', '0') == 0
    assert add_numeric_strings('-2', '3') == 1
