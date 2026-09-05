"""
PB0339 — 느린 네트워크 타임아웃

Chapter: Conditional Statements
Topic: If Statement Scope
Seed: 34 / 82
Variant: 09 / 10
Time cap: 120 seconds
Source checks: if

문제
----
지역 seconds를 5로 정하고 느린 네트워크이면 if 안에서 30으로 바꿔 반환한다.

연습 초점
---------
if 내부에서 초기 지역값 변경

구현할 함수
-----------
def timeout_for_slow_network(is_slow: bool) -> int:

필수 구현 방식
--------------
- if문을 사용한다.

예시 및 필수 테스트
-------------------
- timeout_for_slow_network(True) == 30
- timeout_for_slow_network(False) == 5
- timeout_for_slow_network(not True) == 5

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0339 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def timeout_for_slow_network(is_slow: bool) -> int:
    raise NotImplementedError("TODO: PB0339")


def self_test() -> None:
    assert timeout_for_slow_network(True) == 30
    assert timeout_for_slow_network(False) == 5
    assert timeout_for_slow_network(not True) == 5
