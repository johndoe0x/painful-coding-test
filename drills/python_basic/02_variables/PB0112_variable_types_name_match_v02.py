"""
PB0112 — 타입 이름과 정확히 일치하는지

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 02 / 10
Time cap: 120 seconds
Source checks:

문제
----
type(value).__name__이 expected와 정확히 같을 때만 True를 반환하세요. 대소문자를 바꾸지 말고 bool과 int를 별도 타입으로 취급하세요.

연습 초점
---------
타입 객체의 __name__과 외부 문자열 비교

구현할 함수
-----------
def has_runtime_type_name(value: object, expected: str) -> bool:

예시 및 필수 테스트
-------------------
- has_runtime_type_name(1, 'int') is True
- has_runtime_type_name(True, 'int') is False
- has_runtime_type_name(None, 'NoneType') is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0112 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def has_runtime_type_name(value: object, expected: str) -> bool:
    raise NotImplementedError("TODO: PB0112")


def self_test() -> None:
    assert has_runtime_type_name(1, 'int') is True
    assert has_runtime_type_name(True, 'int') is False
    assert has_runtime_type_name(None, 'NoneType') is True
