"""
PB0113 — 정확히 같은 타입

Chapter: Variables
Topic: Variable Types
Seed: 12 / 82
Variant: 03 / 10
Time cap: 120 seconds
Source checks:

문제
----
두 값의 실제 타입 객체가 같을 때만 True를 반환하세요. 값의 동등성은 보지 않습니다.

연습 초점
---------
타입 동일성과 값 동일성 구분

구현할 함수
-----------
def have_same_exact_type(left: object, right: object) -> bool:

예시 및 필수 테스트
-------------------
- have_same_exact_type(1, 2) is True
- have_same_exact_type(1, True) is False
- have_same_exact_type([], {}) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0113 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def have_same_exact_type(left: object, right: object) -> bool:
    raise NotImplementedError("TODO: PB0113")


def self_test() -> None:
    assert have_same_exact_type(1, 2) is True
    assert have_same_exact_type(1, True) is False
    assert have_same_exact_type([], {}) is False
