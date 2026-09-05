"""
PB0117 — 스칼라 여부

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 07 / 10
Time cap: 120 seconds
Source checks:

문제
----
value의 정확한 타입이 bool, int, float, str, NoneType 중 하나이면 True를 반환하세요.

연습 초점
---------
허용 타입 집합 검사

구현할 함수
-----------
def is_basic_scalar(value: object) -> bool:

예시 및 필수 테스트
-------------------
- is_basic_scalar(3.5) is True
- is_basic_scalar([]) is False
- is_basic_scalar(None) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0117 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def is_basic_scalar(value: object) -> bool:
    raise NotImplementedError("TODO: PB0117")


def self_test() -> None:
    assert is_basic_scalar(3.5) is True
    assert is_basic_scalar([]) is False
    assert is_basic_scalar(None) is True
