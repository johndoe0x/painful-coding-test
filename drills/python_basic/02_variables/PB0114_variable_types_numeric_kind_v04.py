"""
PB0114 — 숫자 타입 세분화

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks:

문제
----
bool은 'boolean', int는 'integer', float는 'floating', 나머지는 'non-numeric'을 반환하세요.

연습 초점
---------
숫자 계층의 정확한 분기 순서

구현할 함수
-----------
def numeric_kind(value: object) -> str:

예시 및 필수 테스트
-------------------
- numeric_kind(True) == 'boolean'
- numeric_kind(0) == 'integer'
- numeric_kind('1') == 'non-numeric'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0114 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def numeric_kind(value: object) -> str:
    raise NotImplementedError("TODO: PB0114")


def self_test() -> None:
    assert numeric_kind(True) == 'boolean'
    assert numeric_kind(0) == 'integer'
    assert numeric_kind('1') == 'non-numeric'
