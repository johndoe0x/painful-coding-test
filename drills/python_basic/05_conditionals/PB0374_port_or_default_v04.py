"""
PB0374 — 포트 기본값

Chapter: Conditional Statements
Topic: Truthy and Falsy
Seed: 38 / 82
Variant: 04 / 10
Time cap: 120 seconds
Source checks: if

문제
----
port가 truthy면 그대로, 0이나 None이면 8080을 반환한다.

연습 초점
---------
숫자 0과 None의 falsy 처리

구현할 함수
-----------
def port_or_default(port: int | None) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- port_or_default(3000) == 3000
- port_or_default(0) == 8080
- port_or_default(None) == 8080

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0374 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def port_or_default(port: int | None) -> int:
    raise NotImplementedError("TODO: PB0374")


def self_test() -> None:
    assert port_or_default(3000) == 3000
    assert port_or_default(0) == 8080
    assert port_or_default(None) == 8080
