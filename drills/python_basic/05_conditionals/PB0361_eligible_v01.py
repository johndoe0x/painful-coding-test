"""
PB0361 — 신분 확인 입장 조건

Chapter: Conditional Statements
Topic: Logic Condition
Seed: 37 / 82
Variant: 01 / 10
Time cap: 120 seconds
Source checks:

문제
----
성인이고 신분증이 있으며 차단되지 않은 경우만 True를 반환한다.

연습 초점
---------
and와 not을 결합한 조건

구현할 함수
-----------
def eligible(age: int, has_id: bool, banned: bool) -> bool:

예시 및 필수 테스트
-------------------
- eligible(20, True, False) is True
- eligible(17, True, False) is False
- eligible(30, True, True) is False

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0361 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def eligible(age: int, has_id: bool, banned: bool) -> bool:
    raise NotImplementedError("TODO: PB0361")


def self_test() -> None:
    assert eligible(20, True, False) is True
    assert eligible(17, True, False) is False
    assert eligible(30, True, True) is False
