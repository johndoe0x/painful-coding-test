"""
PB0151 — 비어 있는 라벨

Chapter: Variables
Topic: Empty Variable
Seed: 16 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
label이 None 또는 빈 문자열이면 'unknown', 아니면 label을 반환하세요.

연습 초점
---------
None과 빈 문자열의 기본값 처리

구현할 함수
-----------
def optional_label(label: str | None) -> str:

예시 및 필수 테스트
-------------------
- optional_label(None) == 'unknown'
- optional_label('') == 'unknown'
- optional_label('x') == 'x'

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0151 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def optional_label(label: str | None) -> str:
    raise NotImplementedError("TODO: PB0151")


def self_test() -> None:
    assert optional_label(None) == 'unknown'
    assert optional_label('') == 'unknown'
    assert optional_label('x') == 'x'
