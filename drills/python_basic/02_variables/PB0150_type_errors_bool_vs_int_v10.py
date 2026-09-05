"""
PB0150 — bool과 int 구별

Chapter: Variables
Topic: Type Errors
Seed: 15 / 82
Variant: 10 / 10
Time cap: 120 seconds
Source checks:

문제
----
value의 타입이 정확히 int일 때만 True를 반환해 bool이 섞이는 오류를 방지하세요.

연습 초점
---------
상속 관계가 있는 타입의 정확한 검사

구현할 함수
-----------
def exact_integer_only(value: object) -> bool:

예시 및 필수 테스트
-------------------
- exact_integer_only(1) is True
- exact_integer_only(True) is False
- exact_integer_only(0.0) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0150 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def exact_integer_only(value: object) -> bool:
    raise NotImplementedError("TODO: PB0150")


def self_test() -> None:
    assert exact_integer_only(1) is True
    assert exact_integer_only(True) is False
    assert exact_integer_only(0.0) is False
