"""
PB0111 — 기본 타입 분류

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
bool, int, float, str, list, dict, None을 각각 그 타입 이름으로 반환하세요. bool을 int보다 먼저 구분하세요.

연습 초점
---------
런타임 타입과 bool의 특수성

구현할 함수
-----------
def classify_value(value: object) -> str:

예시 및 필수 테스트
-------------------
- classify_value(True) == 'bool'
- classify_value(3) == 'int'
- classify_value(None) == 'NoneType'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0111 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def classify_value(value: object) -> str:
    raise NotImplementedError("TODO: PB0111")


def self_test() -> None:
    assert classify_value(True) == 'bool'
    assert classify_value(3) == 'int'
    assert classify_value(None) == 'NoneType'
