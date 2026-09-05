"""
PB0196 — 알림 필요 여부

Chapter: Math
Topic: Boolean OR
Seed: 20 / 82
Variant: 06 / 10
Time cap: 120 seconds
Source checks: bool_or

문제
----
새 메시지 또는 경고가 하나라도 있으면 True를 반환하세요.

연습 초점
---------
두 이벤트 플래그 결합

구현할 함수
-----------
def should_notify(has_message: bool, has_alert: bool) -> bool:

필수 구현 방식
--------------
- 논리 연산자 or를 사용한다.

예시 및 필수 테스트
-------------------
- should_notify(True, False) is True
- should_notify(False, False) is False
- should_notify(True, True) is True and should_notify(False, True) is True

완료 조건
---------
1. 위 함수 이름과 시그니처를 유지한다.
2. 세 assert가 모두 통과하도록 문제의 규칙을 구현한다.
3. 입력별 정답을 if문으로 나열하지 않는다.
4. 저장소 루트에서 `python3 -B -m python_basic PB0196 --strict`를 실행한다.
5. 실행 코드에서 NotImplementedError를 모두 제거한다.
"""


def should_notify(has_message: bool, has_alert: bool) -> bool:
    raise NotImplementedError("TODO: PB0196")


def self_test() -> None:
    assert should_notify(True, False) is True
    assert should_notify(False, False) is False
    assert should_notify(True, True) is True and should_notify(False, True) is True
